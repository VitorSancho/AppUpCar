from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivymd.uix.floatlayout import FloatLayout
from kivymd.uix.button import MDRaisedButton
from kivy.lang import Builder
from kivymd.uix.behaviors import FocusBehavior


KV = '''
Screen:
    MDBoxLayout:
        orientation: 'vertical'
        MDToolbar:
            size_hint:1,.05
            title: 'Agende seu Serviço Conosco!'  
            font_size: 10
            anchor_title: "center"
        MDBoxLayout:
            size_hint:.5,.12
            pos_hint: {'center_x': .5, 'center_y': 1}
            Image:
                source:"marcadagua2.png"

        FloatLayout:  
            size_hint: 1,.05
            pos_hint: {'center_x': .5, 'center_y': 1}  

            ButtonFocus:
                pos_hint: {'center_x': .15, 'center_y': .9} 
                size_hint: .2,.45
                text: '<'
                focus_color: app.theme_cls.accent_color
                unfocus_color: app.theme_cls.primary_color              
            
            Label:
                pos_hint: {'center_x': .5, 'center_y': .9} 
                text: 'Mês'
                color: 0,0,0,1
                font_size: 20

            ButtonFocus:
                pos_hint: {'center_x': 0.85, 'center_y': .9} 
                size_hint: 0.2,.45
                text: '>'
                focus_color: app.theme_cls.accent_color
                unfocus_color: app.theme_cls.primary_color
             

        TelaLogin:

<TelaLogin>: 
    pos_hint: {'center_x':.5, 'center_y': 0.02}
    size_hint:1,0.25
    ButtonFocus:
        pos_hint: {'center_x': .5, 'center_y': 1}
        size_hint_x: .12 
        size_hint_y: .05
        text: 'Q'
        focus_color: app.theme_cls.accent_color
        unfocus_color: app.theme_cls.primary_color
    ButtonFocus:
        pos_hint: {'center_x': .63, 'center_y': 1}
        size_hint_x: .12 
        size_hint_y: .05
        text: 'Q'
        focus_color: app.theme_cls.accent_color
        unfocus_color: app.theme_cls.primary_color
    ButtonFocus:
        pos_hint: {'center_x': .76, 'center_y': 1}
        size_hint_x: .12
        size_hint_y: .05
        text: 'S'
        focus_color: app.theme_cls.accent_color
        unfocus_color: app.theme_cls.primary_color
    ButtonFocus:
        pos_hint: {'center_x': .89, 'center_y': 1}
        size_hint_x: .12
        size_hint_y: .05
        text: 'S'
        focus_color: app.theme_cls.accent_color
        unfocus_color: app.theme_cls.primary_color         
    ButtonFocus:
        pos_hint: {'center_x': .37, 'center_y': 1}
        size_hint_x: .12
        size_hint_y: .05
        text: 'T'
        focus_color: app.theme_cls.accent_color
        unfocus_color: app.theme_cls.primary_color
    ButtonFocus:
        pos_hint: {'center_x': .24, 'center_y': 1}
        size_hint_x: .12
        size_hint_y: .05
        text: 'S'
        focus_color: app.theme_cls.accent_color
        unfocus_color: app.theme_cls.primary_color
    ButtonFocus:
        pos_hint: {'center_x': .11, 'center_y': 1}
        size_hint_x: .12
        size_hint_y: .05
        text: 'D'
        focus_color: app.theme_cls.accent_color
        unfocus_color: app.theme_cls.primary_color    
    
    ButtonFocus:
        pos_hint: {'center_x': .5, 'center_y': .9}
        size_hint_x: .12 
        size_hint_y: .12
        text: '1'
        focus_color: app.theme_cls.accent_color
        unfocus_color: app.theme_cls.primary_color
    ButtonFocus:
        pos_hint: {'center_x': .63, 'center_y': .9}
        size_hint_x: .12 
        size_hint_y: .12
        text: '1'
        focus_color: app.theme_cls.accent_color
        unfocus_color: app.theme_cls.primary_color
    ButtonFocus:
        pos_hint: {'center_x': .76, 'center_y': .9}
        size_hint_x: .12
        size_hint_y: .12
        text: '1'
        focus_color: app.theme_cls.accent_color
        unfocus_color: app.theme_cls.primary_color
    ButtonFocus:
        pos_hint: {'center_x': .89, 'center_y': .9}
        size_hint_x: .12
        size_hint_y: .12
        text: '1'
        focus_color: app.theme_cls.accent_color
        unfocus_color: app.theme_cls.primary_color         
    ButtonFocus:
        pos_hint: {'center_x': .37, 'center_y': .9}
        size_hint_x: .12
        size_hint_y: .12
        text: '1'
        focus_color: app.theme_cls.accent_color
        unfocus_color: app.theme_cls.primary_color
    ButtonFocus:
        pos_hint: {'center_x': .24, 'center_y': .9}
        size_hint_x: .12
        size_hint_y: .12
        text: '1'
        focus_color: app.theme_cls.accent_color
        unfocus_color: app.theme_cls.primary_color
    ButtonFocus:
        pos_hint: {'center_x': .11, 'center_y': .9}
        size_hint_x: .12
        size_hint_y: .12
        text: '1'
        focus_color: app.theme_cls.accent_color
        unfocus_color: app.theme_cls.primary_color
    ButtonFocus:
        pos_hint: {'center_x': .5, 'center_y':.77}
        size_hint_x: .12
        size_hint_y: .12
        text: '1'
        focus_color: app.theme_cls.accent_color
        unfocus_color: app.theme_cls.primary_color
    ButtonFocus:
        pos_hint: {'center_x': .63, 'center_y':.77}
        size_hint_x: .12
        size_hint_y: .12
        text: '1'
        focus_color: app.theme_cls.accent_color
        unfocus_color: app.theme_cls.primary_color
    ButtonFocus:
        pos_hint: {'center_x': .76, 'center_y':.77}
        size_hint_x: .12
        size_hint_y: .12
        text: '1'
        focus_color: app.theme_cls.accent_color
        unfocus_color: app.theme_cls.primary_color
    ButtonFocus:
        pos_hint: {'center_x': .89, 'center_y':.77}
        size_hint_x: .12
        size_hint_y: .12
        text: '1'
        focus_color: app.theme_cls.accent_color
        unfocus_color: app.theme_cls.primary_color         
    ButtonFocus:
        pos_hint: {'center_x': .37, 'center_y':.77}
        size_hint_x: .12
        size_hint_y: .12
        text: '1'
        focus_color: app.theme_cls.accent_color
        unfocus_color: app.theme_cls.primary_color
    ButtonFocus:
        pos_hint: {'center_x': .24, 'center_y':.77}
        size_hint_x: .12
        size_hint_y: .12
        text: '1'
        focus_color: app.theme_cls.accent_color
        unfocus_color: app.theme_cls.primary_color
    ButtonFocus:
        pos_hint: {'center_x': .11, 'center_y':.77}
        size_hint_x: .12
        size_hint_y: .12
        text: '1'
        focus_color: app.theme_cls.accent_color
        unfocus_color: app.theme_cls.primary_color
    ButtonFocus:
        pos_hint: {'center_x': .5, 'center_y': 0.64}
        size_hint_x: .12
        size_hint_y: .12
        text: '1'
        focus_color: app.theme_cls.accent_color
        unfocus_color: app.theme_cls.primary_color
    ButtonFocus:
        pos_hint: {'center_x': .63, 'center_y': 0.64}
        size_hint_x: .12
        size_hint_y: .12
        text: '1'
        focus_color: app.theme_cls.accent_color
        unfocus_color: app.theme_cls.primary_color
    ButtonFocus:
        pos_hint: {'center_x': .76, 'center_y': 0.64}
        size_hint_x: .12
        size_hint_y: .12
        text: '1'
        focus_color: app.theme_cls.accent_color
        unfocus_color: app.theme_cls.primary_color
    ButtonFocus:
        pos_hint: {'center_x': .89, 'center_y': 0.64}
        size_hint_x: .12
        size_hint_y: .12
        text: '1'
        focus_color: app.theme_cls.accent_color
        unfocus_color: app.theme_cls.primary_color 
    ButtonFocus:
        pos_hint: {'center_x': .37, 'center_y': 0.64}
        size_hint_x: .12
        size_hint_y: .12
        text: '1'
        focus_color: app.theme_cls.accent_color
        unfocus_color: app.theme_cls.primary_color
    ButtonFocus:
        pos_hint: {'center_x': .24, 'center_y': 0.64}
        size_hint_x: .12
        size_hint_y: .12
        text: '1'
        focus_color: app.theme_cls.accent_color
        unfocus_color: app.theme_cls.primary_color
    ButtonFocus:
        pos_hint: {'center_x': .11, 'center_y':0.64}
        size_hint_x: .12
        size_hint_y: .12
        text: '1'
        focus_color: app.theme_cls.accent_color
        unfocus_color: app.theme_cls.primary_color   
    ButtonFocus:
        pos_hint: {'center_x': .5, 'center_y': 0.51}
        size_hint_x: .12
        size_hint_y: .12
        text: '1'
        focus_color: app.theme_cls.accent_color
        unfocus_color: app.theme_cls.primary_color
    ButtonFocus:
        pos_hint: {'center_x': .63, 'center_y': 0.51}
        size_hint_x: .12
        size_hint_y: .12
        text: '1'
        focus_color: app.theme_cls.accent_color
        unfocus_color: app.theme_cls.primary_color
    ButtonFocus:
        pos_hint: {'center_x': .76, 'center_y': 0.51}
        size_hint_x: .12
        size_hint_y: .12
        text: '1'
        focus_color: app.theme_cls.accent_color
        unfocus_color: app.theme_cls.primary_color
    ButtonFocus:
        pos_hint: {'center_x': .89, 'center_y': 0.51}
        size_hint_x: .12
        size_hint_y: .12
        text: '1'
        focus_color: app.theme_cls.accent_color
        unfocus_color: app.theme_cls.primary_color 
    ButtonFocus:
        pos_hint: {'center_x': .37, 'center_y': 0.51}
        size_hint_x: .12
        size_hint_y: .12
        text: '1'
        focus_color: app.theme_cls.accent_color
        unfocus_color: app.theme_cls.primary_color
    ButtonFocus:
        pos_hint: {'center_x': .24, 'center_y': 0.51}
        size_hint_x: .12
        size_hint_y: .12
        text: '1'
        focus_color: app.theme_cls.accent_color
        unfocus_color: app.theme_cls.primary_color
    ButtonFocus:
        pos_hint: {'center_x': .11, 'center_y':0.51}
        size_hint_x: .12
        size_hint_y: .12
        text: '1'
        focus_color: app.theme_cls.accent_color
        unfocus_color: app.theme_cls.primary_color
    ButtonFocus:
        pos_hint: {'center_x': .5, 'center_y': .38}
        size_hint_x: .12
        size_hint_y: .12
        text: '1'
        focus_color: app.theme_cls.accent_color
        unfocus_color: app.theme_cls.primary_color
    ButtonFocus:
        pos_hint: {'center_x': .63, 'center_y': .38}
        size_hint_x: .12
        size_hint_y: .12
        text: '1'
        focus_color: app.theme_cls.accent_color
        unfocus_color: app.theme_cls.primary_color
    ButtonFocus:
        pos_hint: {'center_x': .76, 'center_y': .38}
        size_hint_x: .12
        size_hint_y: .12
        text: '1'
        focus_color: app.theme_cls.accent_color
        unfocus_color: app.theme_cls.primary_color
    ButtonFocus:
        pos_hint: {'center_x': .89, 'center_y': .38}
        size_hint_x: .12
        size_hint_y: .12
        text: '1'
        focus_color: app.theme_cls.accent_color
        unfocus_color: app.theme_cls.primary_color 
    ButtonFocus:
        pos_hint: {'center_x': .37, 'center_y': .38}
        size_hint_x: .12
        size_hint_y: .12
        text: '1'
        focus_color: app.theme_cls.accent_color
        unfocus_color: app.theme_cls.primary_color
    ButtonFocus:
        pos_hint: {'center_x': .24, 'center_y': .38}
        size_hint_x: .12
        size_hint_y: .12
        text: '1'
        focus_color: app.theme_cls.accent_color
        unfocus_color: app.theme_cls.primary_color
    ButtonFocus:
        pos_hint: {'center_x': .11, 'center_y':.38}
        size_hint_x: .12
        size_hint_y: .12
        text: '1'
        focus_color: app.theme_cls.accent_color
        unfocus_color: app.theme_cls.primary_color    
    ButtonFocus:
        pos_hint: {'center_x': .5, 'center_y': .25}
        size_hint_x: .12
        size_hint_y: .12
        text: '1'
        focus_color: app.theme_cls.accent_color
        unfocus_color: app.theme_cls.primary_color
    ButtonFocus:
        pos_hint: {'center_x': .63, 'center_y': .25}
        size_hint_x: .12
        size_hint_y: .12
        text: '1'
        focus_color: app.theme_cls.accent_color
        unfocus_color: app.theme_cls.primary_color
    ButtonFocus:
        pos_hint: {'center_x': .76, 'center_y': .25}
        size_hint_x: .12
        size_hint_y: .12
        text: '1'
        focus_color: app.theme_cls.accent_color
        unfocus_color: app.theme_cls.primary_color
    ButtonFocus:
        pos_hint: {'center_x': .89, 'center_y': .25}
        size_hint_x: .12
        size_hint_y: .12
        text: '1'
        focus_color: app.theme_cls.accent_color
        unfocus_color: app.theme_cls.primary_color 
    ButtonFocus:
        pos_hint: {'center_x': .37, 'center_y': .25}
        size_hint_x: .12
        size_hint_y: .12
        text: '1'
        focus_color: app.theme_cls.accent_color
        unfocus_color: app.theme_cls.primary_color
    ButtonFocus:
        pos_hint: {'center_x': .24, 'center_y': .25}
        size_hint_x: .12
        size_hint_y: .12
        text: '1'
        focus_color: app.theme_cls.accent_color
        unfocus_color: app.theme_cls.primary_color
    ButtonFocus:
        pos_hint: {'center_x': .11, 'center_y':.25}
        size_hint_x: .12
        size_hint_y: .12
        text: '1'
        focus_color: app.theme_cls.accent_color
        unfocus_color: app.theme_cls.primary_color 
                             
    
    
'''


class ButtonFocus(MDRaisedButton, FocusBehavior):
    ...


class TelaLogin(FloatLayout):
    def abrir_card(self):
        self.add_widget()


class MyApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Yellow'
        self.theme_cls.accent_palette = 'DeepOrange'
        self.theme_cls.primary_hue = 'A200'

        # self.theme_cls.theme_style = 'Dark'

        return Builder.load_string(KV)


MyApp().run()
