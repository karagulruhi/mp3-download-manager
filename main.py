from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException



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
        print(self.music)

        self.tarayici = webdriver.Chrome('C:\\Users\\Ruhi\\Desktop\\Selenium\\chromedriver.exe')

        self.tarayici.get("https://www.mp3indirdur.pro/")
        time.sleep(1)
        print(self.music)
        self.elem=self.tarayici.find_element(By.CLASS_NAME, "ui-autocomplete-input")
        self.elem.click()
        self.elem.send_keys(self.music)
        time.sleep(0.1)
        self.tarayici.find_element(By.XPATH, "//input[@value='ARA']").click()

        time.sleep(5)  # Bekleme süresi eklendi
        links = self.tarayici.find_elements(By.TAG_NAME, "a")
        link_href_list = []
        for link in links:
            try:
                if "link" in link.get_attribute("class"):
                    href = link.get_attribute("href")
                    link_href_list.append(href)
            except StaleElementReferenceException:
                continue
        for href in link_href_list:
            print(href)
         
        if len(link_href_list) >= 6:
            fifth_link = link_href_list[5] 
            print(fifth_link) # 5. link (indeks 4) alma
            self.tarayici.get(fifth_link)
        time.sleep(5) 
        self.download=self.tarayici.find_element(By.ID, "download").click()
class mp3_downloader(App):      
    def build(self):
        sm= ScreenManager()

        sm.add_widget(SearchScreen(name='search'))
        return sm
if __name__ == "__main__":
    mp3_downloader().run()