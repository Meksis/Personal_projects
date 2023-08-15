import kivy
import random
from kivy.app import App
from kivy.uix.label import Label
#from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.slider import Slider
from kivy.uix.widget import Widget
from kivy.graphics import *
from kivy.uix.stacklayout import StackLayout
from kivy.config import Config
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import *
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
#from kivy.uix.textinput import TextInput


monitor_width=650
monitor_height=800


Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', str(monitor_width))
Config.set('graphics', 'height', str(monitor_height))

width, height = 9, 9

connection_status=1
working_status=1

active_color=[.17, .49, .9, 1] #[0.43, 1.24, 2.29, 1]
inactive_color=[.78, .78, .78, 1] #[1.99, 1.99, 1.99, 1]
hover_color=[.54, .69, .88, 1] #[1.38, 1.76, 2.25, 1]
hover_path='J:/Самописное/AndroApp/Buttons/button_down.png'
not_hover_path='J:/Самописное/AndroApp/Buttons/button_up.png'

class HelperWidget(Widget):
    def draw_text(self, pos_x=0, pos_y=0, text="ERROR"):
        label_text=Label(text, pos=(pos_x, pos_y))

#class ConnectionStatusWidget(Widget):

class ControlWidget(Widget):
    control_layout=FloatLayout(size=(0.2, 0.2))
    pass


class NavigationWidget(Widget):
    def control():
        navigation_layout=FloatLayout(size=(monitor_width, monitor_height*0.05))
        home_button=Button(text="Home", font_size=5, background_normal=not_hover_path, background_down=hover_path, size=(monitor_width/3, monitor_height*0.05), pos=(0, 0))
        effects_button=Button(text="Effects")
        settings_button=Button(text="Settings")

        navigation_layout.add_widget(home_button)
        navigation_layout.add_widget(effects_button)


        return navigation_layout

    #Button(background_normal='', background_down=hover_path, size_hint=(.2, .2))

class TestApp(App):

    def build(self):

        navigation_layout=FloatLayout(size=(monitor_width, monitor_height*0.05), pos=(0, 0))
        #home_button=Button(text="Home", font_size=5, background_normal='', background_down=hover_path, size=(monitor_width/3, monitor_height*0.05), pos=(0, 0))
        effects_button=Button(text="Effects", font_size=25, background_normal='', background_down=hover_path)
        settings_button=Button(text="Settings")



        #navigation_layout.add_widget(home_button)
        navigation_layout.add_widget(effects_button)


        return navigation_layout

        #return NavigationWidget.control()

TestApp().run()

#HBoxLayoutExample().run()
#ButtonApp().run()
