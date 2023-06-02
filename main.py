from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from selenium import webdriver
import time
Builder.load_file("main.kv")



class SearchScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.music=None

    
    
    def takeMusic(self):
        self.music =self.ids.musictext.text
        

        self.download_music()
        self.ids.musictext.text = ''
    
    def download_music(self):
        self.tarayici = webdriver.Chrome()
        self.tarayici.get("https://www.mp3indirdur.pro/")
     
        time.sleep(3)


class mp3_downloader(App):
    def build(self):
        sm= ScreenManager()

        sm.add_widget(SearchScreen(name='search'))
        return sm
if __name__ == "__main__":
    mp3_downloader().run()