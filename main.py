# from kivy.app import App
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivymd.uix.floatlayout import FloatLayout
from kivymd.uix.button import MDRaisedButton
from kivy.lang import Builder
# from myfirebase import MyFirebase
from kivymd.uix.behaviors import FocusBehavior
import requests
import json


KV = '''
Screen:
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'App da Upcar'
            left_action_items: [['menu', lambda x: x]]
            right_action_items: [['dots-vertical', lambda x: x]]
        MDBoxLayout:
            size_hint_y: 1
            Image:
                source:"marcadagua2.png"

        TelaLogin:
          
<SenhaCard>:
    id: card
    orientation: 'vertical'
    size_hint: .7, .7
    pos_hint: {'center_x': .5, 'center_y': .5}
    MDBoxLayout:
        size_hint_y: .2
        padding: [25, 0, 25, 0]
        md_bg_color: app.theme_cls.primary_color
        MDLabel:
            text: 'Cadastre-se'
            theme_text_color: 'Custom'
            color: 0,0,0,1
        MDIconButton:
            theme_text_color: 'Custom'
            icon: 'close'
            text_color: 1, 1, 1, 1
            on_release: root.fechar()
    MDFloatLayout:
        MDTextField:
            id: email_cadastro
            pos_hint: {'center_x': .5, 'center_y': .8}
            size_hint_x: .9
            hint_text: 'Digite seu Email'
        MDTextField:
            id:senha_cadastro
            pos_hint: {'center_x': .5, 'center_y': .6}
            size_hint_x: .9
            hint_text: 'Senha:'
        MDTextField:
            id: senha_cadastro_confirmacao
            pos_hint: {'center_x': .5, 'center_y': .4}
            size_hint_x: .9
            hint_text: 'Confirmar sua senha:'
        ButtonFocus:
            pos_hint: {'center_x': .5, 'center_y': .2}
            size_hint_x: .9
            text: 'Recadastrar!'
            focus_color: app.theme_cls.accent_color
            on_release: root.cadastrar(email_cadastro.text,senha_cadastro.text,senha_cadastro_confirmacao.text)
<TelaLogin>: 
    MDTextField:
        id: login
        size_hint_x: .9
        hint_text: 'Email:'
        line_color_focus: 0, 0, 0, 1
        pos_hint: {'center_x': .5, 'center_y': .7}
    MDTextField:
        id: senha
        size_hint_x: .9
        hint_text: 'Senha:'
        line_color_focus: 0, 0, 0, 1
        password: True
        pos_hint: {'center_x': .5, 'center_y': .6}
    ButtonFocus:
        size_hint_x: .9
        pos_hint: {'center_x': .5, 'center_y': .5}
        text: 'Login'
        focus_color: app.theme_cls.accent_color
        unfocus_color: app.theme_cls.primary_color
        on_release: root.autentica_login(login.text,senha.text)
    MDLabel:
        pos_hint: {'center_y': .4}
        halign: 'center'
        text: 'Primeir Acesso ou Esqueceu sua senha?'
    MDTextButton:
        pos_hint: {'center_x': .5, 'center_y': .3}
        text: 'Clique Aqui!'
        color: 0,0,0,1
        on_release: root.abrir_card_cadastro()
'''


class MyFirebase():
    webAPIkey = "AIzaSyBW9ug6HoPcTkPwgibMIho7U0hcCYXKF-s"


class ButtonFocus(MDRaisedButton, FocusBehavior):
    ...


class SenhaCard(MDCard):
    my_firebase = MyFirebase()

    def fechar(self):
        self.parent.remove_widget(self)

    def cadastrar(self, email, senha, senha_confirmacao):

        mdapp = MDApp.get_running_app()

        webAPIkey = "AIzaSyBW9ug6HoPcTkPwgibMIho7U0hcCYXKF-s"
        print(email)
        signup_url = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/signupNewUser?key=" + webAPIkey
        signup_payload = {"email": email,
                          "password": senha, "returnSecureToken": True}
        sign_up_request = requests.post(signup_url, data=signup_payload)
        print(sign_up_request.ok)
        sign_up_data = json.loads(sign_up_request.content.decode())
        print(sign_up_data)

        print(sign_up_data)

        if sign_up_request.ok == True:
            refresh_token = sign_up_data['refreshToken']
            localId = sign_up_data['localId']
            idToken = sign_up_data['idToken']
            print(idToken)
            print(localId)
            # Save refreshToken to a file
            with open("refresh_token.txt", "w") as f:
                f.write(refresh_token)

            # Save localId to a variable in main app class
            # Save idToken to a variable in main app class
            mdapp.local_id = localId
            mdapp.id_token = idToken

            # Create new key in database from localId
            # Get friend ID
            # Get request on firebase to get the next friend id
            my_data = '{"datas": "teste"}'
            post_request = requests.patch(
                "https://upcar-1824a-default-rtdb.firebaseio.com/" + localId + ".json?auth=" + idToken, data=my_data)

            print(post_request.ok)
            print(json.loads(post_request.content.decode()))

            self.fechar()

        # inserir confirmacoa de senha


class TelaLogin(FloatLayout):
    webAPIkey = "AIzaSyBW9ug6HoPcTkPwgibMIho7U0hcCYXKF-s"

    def abrir_card_cadastro(self):
        self.add_widget(SenhaCard())

    def abrir_card_esqueci_senha(self):
        self.add_widget(SenhaCard())

    def abrir_ambiente_interno(self):
        self.add_widget(SenhaCard())

    def autentica_login(self, email, senha):
        print("testando" + email)
        signin_url = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key=" + self.webAPIkey
        signin_payload = {"email": email,
                          "password": senha, "returnSecureToken": True}
        signin_request = requests.post(signin_url, data=signin_payload)
        sign_up_data = json.loads(signin_request.content.decode())

        mdapp = MDApp.get_running_app()

        print(signin_request.ok)
        print(json.loads(signin_request.content.decode()))

        if signin_request.ok == True:
            print("logado")
            refresh_token = sign_up_data['refreshToken']
            localId = sign_up_data['localId']
            idToken = sign_up_data['idToken']
            # Save refreshToken to a file
            with open("refresh_token.txt", "w") as f:
                f.write(refresh_token)

        # elif signin_request.ok == False:
            # error_data = json.loads(signin_request.content.decode())
            # error_message = error_data["error"]['message']
            # mdapp.root.ids['login_screen'].ids['login_message'].text = "EMAIL EXISTS - " + \
            #     error_message.replace("_", " ")


class MyApp(MDApp):
    def build(self):
        self.my_firebase = MyFirebase()
        self.theme_cls.primary_palette = 'Yellow'
        self.theme_cls.accent_palette = 'Yellow'
        self.theme_cls.primary_hue = 'A200'

        # self.theme_cls.theme_style = 'Dark'

        return Builder.load_string(KV)


MyApp().run()
