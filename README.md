# מעקב מניות - אפליקציה לניתוח טכני מקצועי

אפליקציה מתקדמת למעקב וניתוח מניות עם כלים טכניים מקצועיים, המלצות קנייה ומכירה, וסקירת שווקים בזמן אמת.

## 🌟 תכונות עיקריות

### 📊 ניתוח טכני מתקדם
- **RSI (Relative Strength Index)** - זיהוי מצבי overbought/oversold
- **MACD (Moving Average Convergence Divergence)** - זיהוי מגמות ושינויי כיוון
- **רמות פיבונצי** - זיהוי רמות תמיכה והתנגדות
- **Bollinger Bands** - זיהוי תנודתיות וזרוזים
- **ממוצעים נעים** - SMA 20, SMA 50, EMA 12, EMA 26

### 💡 המלצות חכמות
- מערכת המלצות אוטומטית מבוססת על ניתוח טכני
- רמות ביטחון ברורות (גבוהה/בינונית)
- אותות מסחר מפורטים עם הסברים

### 📈 נתונים בזמן אמת
- מידע מעודכן מ-Yahoo Finance
- גרפים אינטראקטיביים עם Plotly
- עדכון אוטומטי כל 30 שניות

### 🌍 סקירת שווקים
- מעקב אחר מדדי הבורסה האמריקאית
- S&P 500, Dow Jones, NASDAQ, VIX
- שינויים יומיים ואחוזים

### 🔐 אבטחה מלאה
- מערכת הרשמה והתחברות מאובטחת
- הצפנת סיסמאות
- הגנה על נתונים אישיים

## 🚀 התקנה והפעלה

### דרישות מערכת
- Python 3.8 או גרסה חדשה יותר
- pip (מנהל החבילות של Python)

### שלבי התקנה

1. **שכפול הפרויקט**
```bash
git clone <repository-url>
cd stock-tracker
```

2. **יצירת סביבה וירטואלית**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# או
venv\Scripts\activate  # Windows
```

3. **התקנת תלויות**
```bash
pip install -r requirements.txt
```

4. **הגדרת משתני סביבה**
```bash
cp .env.example .env
# ערוך את הקובץ .env והוסף את המפתח הסודי שלך
```

5. **יצירת מסד נתונים**
```bash
python app.py
```

6. **הפעלת האפליקציה**
```bash
python app.py
```

האפליקציה תהיה זמינה בכתובת: `http://localhost:5000`

## 📱 שימוש באפליקציה

### 1. הרשמה והתחברות
- הירשם עם שם משתמש, אימייל וסיסמה
- התחבר לחשבון שלך

### 2. הוספת מניות
- לחץ על "הוסף מניה" בלוח הבקרה
- הכנס את סימול המניה (לדוגמה: AAPL, TSLA, MSFT)
- הכנס את כמות המניות ומחיר הרכישה הממוצע

### 3. ניתוח טכני
- לחץ על אייקון הגרף ליד כל מניה
- צפה בניתוח טכני מפורט עם:
  - גרף מחירים עם אינדיקטורים
  - רמות פיבונצי
  - המלצת קנייה/מכירה
  - אותות מסחר

### 4. מעקב שווקים
- צפה במצב השווקים האמריקאיים
- מעקב אחר מדדי הבורסה העיקריים

## 🛠️ טכנולוגיות

### Backend
- **Flask** - מסגרת עבודה ל-Python
- **SQLAlchemy** - ORM למסד נתונים
- **Flask-Login** - ניהול משתמשים
- **yfinance** - קבלת נתוני מניות
- **ta** - חישוב אינדיקטורים טכניים
- **Plotly** - יצירת גרפים אינטראקטיביים

### Frontend
- **Bootstrap 5** - מסגרת CSS
- **Font Awesome** - אייקונים
- **JavaScript** - אינטראקציה דינמית
- **Plotly.js** - גרפים אינטראקטיביים

### מסד נתונים
- **SQLite** - מסד נתונים קל משקל

## 📊 אינדיקטורים טכניים

### RSI (Relative Strength Index)
- **מטרה**: זיהוי מצבי overbought/oversold
- **טווח**: 0-100
- **אותות**: 
  - RSI < 30: מצב oversold (קנייה)
  - RSI > 70: מצב overbought (מכירה)

### MACD (Moving Average Convergence Divergence)
- **מטרה**: זיהוי מגמות ושינויי כיוון
- **רכיבים**: MACD Line, Signal Line, Histogram
- **אותות**: 
  - MACD > Signal: מגמה חיובית
  - MACD < Signal: מגמה שלילית

### רמות פיבונצי
- **מטרה**: זיהוי רמות תמיכה והתנגדות
- **רמות**: 0%, 23.6%, 38.2%, 50%, 61.8%, 78.6%, 100%
- **שימוש**: זיהוי נקודות כניסה ויציאה

### Bollinger Bands
- **מטרה**: זיהוי תנודתיות וזרוזים
- **רכיבים**: Upper Band, Middle Band, Lower Band
- **אותות**: 
  - מחיר נוגע ב-Upper Band: אפשרות למכירה
  - מחיר נוגע ב-Lower Band: אפשרות לקנייה

## 🔧 API Endpoints

### נתוני מניות
```
GET /api/stock_data/<symbol>
```
מחזיר נתונים נוכחיים של מניה כולל מחיר, שינוי, RSI והמלצה.

### ניתוח טכני
```
GET /analyze/<symbol>
```
מציג דף ניתוח טכני מלא עם גרפים והמלצות.

## 🚀 פריסה (Deployment)

### Heroku
1. צור קובץ `Procfile`:
```
web: gunicorn app:app
```

2. הוסף את האפליקציה ל-Heroku:
```bash
heroku create your-app-name
git push heroku main
```

### Docker
1. צור קובץ `Dockerfile`:
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["gunicorn", "app:app"]
```

2. בנייה והפעלה:
```bash
docker build -t stock-tracker .
docker run -p 5000:5000 stock-tracker
```

## 🔒 אבטחה

- סיסמאות מוצפנות עם bcrypt
- הגנה מפני CSRF
- אימות משתמשים עם Flask-Login
- הגנה על נתונים אישיים

## 🤝 תרומה לפרויקט

1. Fork את הפרויקט
2. צור branch חדש (`git checkout -b feature/amazing-feature`)
3. Commit את השינויים (`git commit -m 'Add amazing feature'`)
4. Push ל-branch (`git push origin feature/amazing-feature`)
5. פתח Pull Request

## 📄 רישיון

פרויקט זה מוגן תחת רישיון MIT. ראה קובץ `LICENSE` לפרטים.

## 📞 תמיכה

אם יש לך שאלות או בעיות:
- פתח Issue ב-GitHub
- שלח אימייל לתמיכה
- בדוק את התיעוד

## 🔮 תכונות עתידיות

- [ ] התראות מחיר
- [ ] ניתוח פונדמנטלי
- [ ] מסחר אוטומטי
- [ ] אפליקציה למובייל
- [ ] אינטגרציה עם ברוקרים
- [ ] ניתוח פורטפוליו מתקדם
- [ ] דוחות PDF
- [ ] API ציבורי

---

**הערה חשובה**: האפליקציה מיועדת למטרות לימוד ומידע בלבד. אין לראות בהמלצות ייעוץ השקעות מקצועי. תמיד התייעץ עם יועץ השקעות מוסמך לפני קבלת החלטות השקעה.
