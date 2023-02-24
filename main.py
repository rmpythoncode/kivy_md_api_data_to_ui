from kaki.app import App
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.factory import Factory
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout

Window.size = (250, 450)
Window.top = 240
Window.left = 1024


class ProductScreen(MDScreen):
  pass

class HomeScreen(MDScreen):
  pass

class MainMDScreenManager(MDScreenManager):
  pass

class MainApp(App, MDApp):
  DEBUG=1

  CLASSES = {
    "HomeScreen": "screens.homescreen",
    "ProductScreen": "screens.productscreen",
  }

  KV_FILES = {
    ("mainmdscreenmanager.kv"),
    ("screens/homescreen.kv"),
    ("screens/productscreen.kv"),
  }

  AUTORELOADER_PATHS = [
    (".", {"recursive": True}),
  ]
  
  def build_app(self):
    def build(self):
      sm = MDScreenManager()
      sm.add_widget(HomeScreen(name="homescreen"))
      sm.add_widget(ProductScreen(name="productscreen"))
      return sm
    return Factory.MainMDScreenManager()

if __name__ == "__main__":
  MainApp().run()