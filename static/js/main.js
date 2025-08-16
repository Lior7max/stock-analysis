// Main JavaScript for Stock Tracking App

// Utility Functions
const StockTracker = {
    // Format currency
    formatCurrency: function(amount) {
        return new Intl.NumberFormat('en-US', {
            style: 'currency',
            currency: 'USD'
        }).format(amount);
    },

    // Format percentage
    formatPercentage: function(value) {
        return `${value >= 0 ? '+' : ''}${value.toFixed(2)}%`;
    },

    // Format number with commas
    formatNumber: function(num) {
        return new Intl.NumberFormat('en-US').format(num);
    },

    // Show loading spinner
    showLoading: function(element) {
        element.innerHTML = '<div class="loading"></div>';
    },

    // Show error message
    showError: function(element, message) {
        element.innerHTML = `<span class="text-danger"><i class="fas fa-exclamation-triangle me-1"></i>${message}</span>`;
    },

    // Animate number counting
    animateNumber: function(element, start, end, duration = 1000) {
        const startTime = performance.now();
        const difference = end - start;
        
        function updateNumber(currentTime) {
            const elapsed = currentTime - startTime;
            const progress = Math.min(elapsed / duration, 1);
            
            const current = start + (difference * progress);
            element.textContent = StockTracker.formatCurrency(current);
            
            if (progress < 1) {
                requestAnimationFrame(updateNumber);
            }
        }
        
        requestAnimationFrame(updateNumber);
    },

    // Validate stock symbol
    validateSymbol: function(symbol) {
        const symbolRegex = /^[A-Z]{1,5}$/;
        return symbolRegex.test(symbol);
    },

    // Debounce function
    debounce: function(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    },

    // Throttle function
    throttle: function(func, limit) {
        let inThrottle;
        return function() {
            const args = arguments;
            const context = this;
            if (!inThrottle) {
                func.apply(context, args);
                inThrottle = true;
                setTimeout(() => inThrottle = false, limit);
            }
        };
    }
};

// Chart Utilities
const ChartUtils = {
    // Create candlestick chart
    createCandlestickChart: function(containerId, data) {
        const trace = {
            x: data.dates,
            open: data.open,
            high: data.high,
            low: data.low,
            close: data.close,
            type: 'candlestick',
            name: 'Price'
        };

        const layout = {
            title: 'Stock Price Chart',
            xaxis: { title: 'Date' },
            yaxis: { title: 'Price ($)' },
            template: 'plotly_white'
        };

        Plotly.newPlot(containerId, [trace], layout, {responsive: true});
    },

    // Create line chart
    createLineChart: function(containerId, data, title) {
        const trace = {
            x: data.x,
            y: data.y,
            type: 'scatter',
            mode: 'lines',
            name: data.name,
            line: { color: data.color || '#0d6efd' }
        };

        const layout = {
            title: title,
            xaxis: { title: 'Date' },
            yaxis: { title: 'Value' },
            template: 'plotly_white'
        };

        Plotly.newPlot(containerId, [trace], layout, {responsive: true});
    }
};

// Form Validation
const FormValidator = {
    // Validate stock form
    validateStockForm: function(form) {
        const symbol = form.querySelector('#symbol').value.trim().toUpperCase();
        const quantity = parseFloat(form.querySelector('#quantity').value);
        const avgPrice = parseFloat(form.querySelector('#avg_price').value);

        let isValid = true;
        let errors = [];

        // Validate symbol
        if (!symbol) {
            errors.push('סימול מניה הוא שדה חובה');
            isValid = false;
        } else if (!StockTracker.validateSymbol(symbol)) {
            errors.push('סימול מניה חייב להיות 1-5 אותיות באנגלית');
            isValid = false;
        }

        // Validate quantity
        if (isNaN(quantity) || quantity <= 0) {
            errors.push('כמות מניות חייבת להיות מספר חיובי');
            isValid = false;
        }

        // Validate average price
        if (isNaN(avgPrice) || avgPrice <= 0) {
            errors.push('מחיר ממוצע חייב להיות מספר חיובי');
            isValid = false;
        }

        return { isValid, errors };
    },

    // Show form errors
    showErrors: function(errors) {
        const alertContainer = document.createElement('div');
        alertContainer.className = 'alert alert-danger alert-dismissible fade show';
        alertContainer.innerHTML = `
            <ul class="mb-0">
                ${errors.map(error => `<li>${error}</li>`).join('')}
            </ul>
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        `;

        const container = document.querySelector('.container');
        container.insertBefore(alertContainer, container.firstChild);
    }
};

// API Utilities
const API = {
    // Fetch stock data
    fetchStockData: async function(symbol) {
        try {
            const response = await fetch(`/api/stock_data/${symbol}`);
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return await response.json();
        } catch (error) {
            console.error('Error fetching stock data:', error);
            throw error;
        }
    },

    // Search stocks
    searchStocks: async function(query) {
        try {
            const response = await fetch(`/api/search_stocks?q=${encodeURIComponent(query)}`);
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return await response.json();
        } catch (error) {
            console.error('Error searching stocks:', error);
            throw error;
        }
    }
};

// Event Listeners
document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function(tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Initialize popovers
    const popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    popoverTriggerList.map(function(popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl);
    });

    // Form validation
    const stockForm = document.querySelector('form[action*="add_stock"]');
    if (stockForm) {
        stockForm.addEventListener('submit', function(e) {
            const validation = FormValidator.validateStockForm(this);
            if (!validation.isValid) {
                e.preventDefault();
                FormValidator.showErrors(validation.errors);
            }
        });
    }

    // Auto-refresh portfolio data
    const portfolioTable = document.getElementById('portfolioTable');
    if (portfolioTable) {
        // Refresh every 30 seconds
        setInterval(() => {
            updatePortfolioData();
        }, 30000);
    }

    // Symbol input auto-uppercase
    const symbolInputs = document.querySelectorAll('input[name="symbol"]');
    symbolInputs.forEach(input => {
        input.addEventListener('input', function() {
            this.value = this.value.toUpperCase();
        });
    });

    // Number input formatting
    const numberInputs = document.querySelectorAll('input[type="number"]');
    numberInputs.forEach(input => {
        input.addEventListener('blur', function() {
            if (this.value && !isNaN(this.value)) {
                this.value = parseFloat(this.value).toFixed(2);
            }
        });
    });

    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Add fade-in animation to cards
    const cards = document.querySelectorAll('.card');
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
            }
        });
    });

    cards.forEach(card => {
        observer.observe(card);
    });
});

// Keyboard shortcuts
document.addEventListener('keydown', function(e) {
    // Ctrl/Cmd + K to focus search
    if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
        e.preventDefault();
        const searchInput = document.querySelector('input[type="search"], input[placeholder*="search"]');
        if (searchInput) {
            searchInput.focus();
        }
    }

    // Escape to close modals
    if (e.key === 'Escape') {
        const modals = document.querySelectorAll('.modal.show');
        modals.forEach(modal => {
            const modalInstance = bootstrap.Modal.getInstance(modal);
            if (modalInstance) {
                modalInstance.hide();
            }
        });
    }
});

// Service Worker Registration (for PWA features)
if ('serviceWorker' in navigator) {
    window.addEventListener('load', function() {
        navigator.serviceWorker.register('/sw.js')
            .then(function(registration) {
                console.log('SW registered: ', registration);
            })
            .catch(function(registrationError) {
                console.log('SW registration failed: ', registrationError);
            });
    });
}

// Export utilities for global use
window.StockTracker = StockTracker;
window.ChartUtils = ChartUtils;
window.FormValidator = FormValidator;
window.API = API;