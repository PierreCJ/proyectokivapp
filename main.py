import kivy
kivy.require('1.9.0')

from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config

Config.set('graphics','width',400)
Config.set('graphics','height',200) 
class Contenedor_01(BoxLayout):
    None

class MainApp(App): 
    title= "Mi primera app"
    #esto es lo que busca kivy para saber que hacer. es la funcion principal

    def build(self):
        return Contenedor_01() 

#lo siguiente tambien es obligatorio para kivy y para android. es por simple conveción(no se necesita )
if __name__  == '__main__' :
    MainApp().run()
 
