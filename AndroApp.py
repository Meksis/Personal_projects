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
#from kivy.uix.textinput import TextInput

Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '650')
Config.set('graphics', 'height', '800')

width, height = 9, 9

connection_status=1
working_status=1

active_color=[.17, .49, .9, 1] #[0.43, 1.24, 2.29, 1]
inactive_color=[.78, .78, .78, 1] #[1.99, 1.99, 1.99, 1]
hover_color=[.54, .69, .88, 1] #[1.38, 1.76, 2.25, 1]
hover_path='J:/Самописное/AndroApp/Buttons/button_down.png'

class HelperWidget(Widget):
    def draw_text(self, pos_x=0, pos_y=0, text="ERROR"):
        label_text=Label(text, pos=(pos_x, pos_y))

#class ConnectionStatusWidget(Widget):






class ControlWidget(Widget):


    #def if_hover(instance):
    #    instance.text='HUY'

    def __init__(self, **kwargs):
        c_x, c_y, c_w, c_h=850, 900, 50, 50

        super(ControlWidget, self).__init__(**kwargs)

        with self.canvas:
            if connection_status:
                r, g, b = active_color[0], active_color[1], active_color[2]
                Color(r, g, b)
            else:
                r, g, b = inactive_color[0], inactive_color[1], inactive_color[2]
                Color(r, g, b)
            Ellipse(pos=(500, 735), size=(50, 50))

            if working_status:
                r, g, b = active_color[0], active_color[1], active_color[2]
                Color(r, g, b)
            else:
                r, g, b = inactive_color[0], inactive_color[1], inactive_color[2]
                Color(r, g, b)

            Ellipse(pos=(575, 735), size=(50, 50))

    def control():

        float_lay=FloatLayout(size=(.8, .8))

        onoff=Button(background_normal='', text="OFF" if connection_status else "ON", background_color=active_color if connection_status else inactive_color, background_down=hover_path, size_hint=(.1, .1), pos=(680-680*.1*2,250))

        saturation=Slider(min=0, max=100, value=100, size=[0, 0], pos=(0, 50), sensitivity='handle', padding=25)
        #sliders_layout.add_widget(brightness)
        brightness=Slider(min=0, max=100, value=75, size=[.25, .1], pos=(0,200), sensitivity='handle', padding=25)
        #sliders_layout.add_widget(saturation)
        saturation_label=Label(text='Saturation', pos=(0, 175), size_hint=(.25, 0))
        brightness_label=Label(text='Brightness', pos=(0, 200), size_hint=(.25, 0))

        float_lay.add_widget(onoff)
        float_lay.add_widget(brightness_label)
        float_lay.add_widget(brightness)
        float_lay.add_widget(saturation_label)
        float_lay.add_widget(saturation)

        return float_lay


class TestApp(App):

    def build(self):

        return ControlWidget.control()
        #return ControlWidget()

        #return ControlWidget.control()


        #print(slider.on_touch_down())
        #print(saturation.value)



x=1

if x!=1:
    exapp().run()
else:
    TestApp().run()

#HBoxLayoutExample().run()
#ButtonApp().run()
