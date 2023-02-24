from kivymd.uix.screen import MDScreen
from kivy.network.urlrequest import UrlRequest
import json
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDIconButton
from kivy.uix.scrollview import ScrollView
from kivymd.uix.card import MDCard
from kivymd.uix.list import MDList, OneLineListItem

class ProductScreen(MDScreen):
  url = "https://jsonplaceholder.typicode.com/users"
  
  def on_pre_enter(self, **args):
    self.get_data()  

  def get_data(self):
    req = UrlRequest(self.url)
    req.wait()
    # print(req.result)

    def got_json(req, result):

     

       
    
        


        # self.ids.mdlabel_name.add_widget(MDLabel(text=(i['name'])))


 
      print('ok patrao')

    req = UrlRequest(self.url, got_json)

  
 