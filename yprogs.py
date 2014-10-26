from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import NumericProperty
from kivy.lang import Builder
from kivy.config import Config

from subprocess import Popen
from platform import system
import configparser

window_size = (293, 192)
Config.set('graphics', 'width', window_size[0])
Config.set('graphics', 'height', window_size[1])
Config.set('graphics', 'resizable', 0)

config = configparser.ConfigParser()
config.read('yprogs.ini')

os = system()
if os == 'Windows':
    import ctypes
    user32 = ctypes.windll.user32
    screen_size = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    Config.set('graphics', 'position', 'custom')
    Config.set('graphics', 'left', screen_size[0] / 2 - window_size[0] / 2)
    Config.set('graphics', 'top', screen_size[1] / 2 - window_size[1] / 2)
    run_app = 'explorer.exe'
elif os == 'Linux':
    Config.set('graphics', 'position', 'auto')
    run_app = 'xdg-open'


class Controller(StackLayout):
    sys_app = run_app  # So the kv-file can access the variable
    xhint = NumericProperty(.321)
    yhint = NumericProperty(.2)
    btn_font = 14
    btn_color = 0, 1, 8, .8
    btn1_text = config.get('Button1', 'Caption')
    btn1_action, btn1_arg = sys_app, '%s' % config.get('Button1', 'Path')
    btn2_text = config.get('Button2', 'Caption')
    btn2_action, btn2_arg = sys_app, '%s' % config.get('Button2', 'Path')
    btn3_text = config.get('Button3', 'Caption')
    btn3_action, btn3_arg = sys_app, '%s' % config.get('Button3', 'Path')
    btn4_text = config.get('Button4', 'Caption')
    btn4_action, btn4_arg = sys_app, '%s' % config.get('Button4', 'Path')
    btn5_text = config.get('Button5', 'Caption')
    btn5_action, btn5_arg = sys_app, '%s' % config.get('Button5', 'Path')
    btn6_text = config.get('Button6', 'Caption')
    btn6_action, btn6_arg = sys_app, '%s' % config.get('Button6', 'Path')

    btn_edit_text = 'Edit'
    btn_exit_text = 'Exit'

    def btn_action(self, btn_action, btn_arg):
        Popen([btn_action, btn_arg])
        exit()


class YProgsApp(App):
    def build(self):
        self.icon = 'yprogs.ico'
        return Controller()

if __name__ == '__main__':
    YProgsApp().run()