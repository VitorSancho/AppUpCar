from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput


def on_press(botao):
    botao.text = "PAU NO CU DO CURIOSO!"
    botao.font_size = 80


class Myapp(App):
    def build(self):
        textinput = TextInput()
        box = BoxLayout(orientation='vertical')
        botao = Button(text='Nome no botão', on_press=on_press)
        label = Label(text='texto no label')
        label.font_size = 50

        box.add_widget(label)
        box.add_widget(botao)
        box.add_widget(textinput)

        return box


Myapp().run()
