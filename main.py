import random

try:
    from kivy.app import App
    from kivy.uix.button import Button
    from kivy.core.window import Window
    from kivy.uix.label import Label
    from kivy.uix.boxlayout import BoxLayout
except ImportError as e:
    print(f"Ошибка импорта: {e}")
    print("\nНеобходимые зависимости:")
    print("  - kivy (установите: pip install kivy)")
    print("\nПроверьте установку Kivy и его зависимостей:")
    print("  pip install kivy[base] kivy_examples")
    exit()

Window.size = (400, 400)

class Clicker(App):
    def __init__(self):
        super().__init__()
        self.btn = Button(text="Нажми на меня")
        self.label = Label(text="Нажми на кнопку")
        self.btn.bind(on_press=self.button_pressed)

    def button_pressed(self, *args):
        self.label.text = str(random.randint(0, 100))


    def build(self):
        self.title = "Генератор чисел"
        layout = BoxLayout(orientation='vertical')

        layout.add_widget(self.label)
        layout.add_widget(self.btn)

        return layout

if __name__ == '__main__':
    Clicker().run()

