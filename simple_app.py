from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.lang import Builder

# Set window size for testing
Window.size = (400, 700)

KV = '''
BoxLayout:
    orientation: 'vertical'
    padding: 20
    spacing: 20
    
    Label:
        text: 'מעקב מניות'
        font_size: '24sp'
        size_hint_y: None
        height: '50dp'
        color: 0.2, 0.6, 1, 1
    
    TextInput:
        id: username
        hint_text: 'שם משתמש'
        multiline: False
        size_hint_y: None
        height: '50dp'
        font_size: '16sp'
    
    TextInput:
        id: password
        hint_text: 'סיסמה'
        multiline: False
        password: True
        size_hint_y: None
        height: '50dp'
        font_size: '16sp'
    
    Button:
        text: 'התחבר'
        size_hint_y: None
        height: '50dp'
        background_color: 0.2, 0.6, 1, 1
        on_press: root.login()
    
    Button:
        text: 'הוסף מניה'
        size_hint_y: None
        height: '50dp'
        background_color: 0.3, 0.7, 0.3, 1
        on_press: root.add_stock()
    
    Label:
        id: status
        text: 'ברוך הבא למעקב מניות'
        font_size: '16sp'
        size_hint_y: None
        height: '50dp'
    
    Widget:
        size_hint_y: 1
'''

class StockApp(App):
    def build(self):
        return Builder.load_string(KV)
    
    def login(self):
        username = self.root.ids.username.text
        password = self.root.ids.password.text
        
        if username and password:
            self.root.ids.status.text = f'ברוך הבא, {username}!'
            self.show_popup('הצלחה', 'התחברת בהצלחה!')
        else:
            self.show_popup('שגיאה', 'אנא מלא את כל השדות')
    
    def add_stock(self):
        self.show_popup('הוספת מניה', 'פונקציה זו תתווסף בקרוב')
    
    def show_popup(self, title, message):
        popup = Popup(title=title, content=Label(text=message), size_hint=(None, None), size=(300, 200))
        popup.open()

if __name__ == '__main__':
    StockApp().run()