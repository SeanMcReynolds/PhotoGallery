from kivy.app import App
from kivy.uix.screenmanager import Screen

class PhotoGalleryApp(App):
    pass

class Display(Screen):
    def display_images(self):
        return images[index]
    def advance(self):
        global index
        if index < len(images)-1:
            index += 1
        else:
            index = 0
        self.ids.image.source = self.display_images()

images = ["lake.jpg","vancouver.jpg","cat.jpg"]
index = 0

PhotoGalleryApp().run()
