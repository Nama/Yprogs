from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import NumericProperty
from kivy.lang import Builder
from kivy.config import Config

from subprocess import Popen
import configparser

Config.set('graphics', 'width', '293')
Config.set('graphics', 'height', '192')

config = configparser.ConfigParser()
config.read('yprogs.ini')


class Controller(StackLayout):
    xhint = NumericProperty(.321)
    yhint = NumericProperty(.2)
    btn_font = 14
    btn_color = 0, 1, 8, .8
    btn1_text = config.get('Button1', 'Caption')
    btn1_action = 'explorer.exe %s' % config.get('Button1', 'Path')
    btn2_text = config.get('Button2', 'Caption')
    btn2_action = 'explorer.exe %s' % config.get('Button2', 'Path')
    btn3_text = config.get('Button3', 'Caption')
    btn3_action = 'explorer.exe %s' % config.get('Button3', 'Path')
    btn4_text = config.get('Button4', 'Caption')
    btn4_action = 'explorer.exe %s' % config.get('Button4', 'Path')
    btn5_text = config.get('Button5', 'Caption')
    btn5_action = 'explorer.exe %s' % config.get('Button5', 'Path')
    btn6_text = config.get('Button6', 'Caption')
    btn6_action = 'explorer.exe %s' % config.get('Button6', 'Path')

    btn_edit_text = 'Edit'
    btn_exit_text = 'Exit'

    def btn_action(self, btn_action):
        Popen(btn_action)
        exit()


class YProgsApp(App):
    def build(self):
        return Controller()

if __name__ == '__main__':
    YProgsApp().run()