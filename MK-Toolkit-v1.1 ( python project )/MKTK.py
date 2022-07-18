from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from pytube import YouTube
from pytube import Playlist
from kivy.config import Config
from kivy.lang import Builder
import os
import re
import clipboard
from _thread import start_new_thread as snt
import time
import sys

Config.set('graphics', 'resizable', False)
Config.set('graphics', 'height', '600')
Config.set('graphics', 'width', '900')


Builder.load_string("""

<Button>:
    font_size: root.height * 0.26
    color: 0.5, 0.75, 0.75, 1
    size_hint: None, None
    background_color: 1,1,1,0.75
    color: 1,1,1,0.90
<MyApp>
    bg: bg
    txti: txti
    txto: txto
    pet1: pet1
    pet2: pet2
    lov1: lov1
    lov2: lov2
    pet_sad: pet_sad
        
    FloatLayout:
        size: root.width, root.height

        Image:
            id: bg
            size: root.height*3, root.height
            size_hint_x: None
            pos_hint: {"center_x": 0.5}
            keep_ratio: True
            allow_stretch: True

        TextInput:
            id: txti
            size_hint: None, None
            height: root.height * 0.05
            width: self.height * 10
            background_color: 1,1,1,0.1
            color: 1,1,1,0.75
            font_size: self.height * 0.5
            pos_hint: {"center_y": 0.36, "center_x": 0.5}
            hint_text: " Cole o link aqui"
        Label:
            size_hint: None, None
            pos_hint: {"center_y": 0.47, "center_x": 0.5}
            height: root.height *0.3
            padding_y: 10
            width: self.height * 1.7
            text_size: self.size
            halign: 'left'
            valign: 'top'
            font_size: self.height * 0.1
            id: txto
            color: 1,1,1,0.5
            canvas.before:
                Color:
                    rgba: 0,0,0,0
                Rectangle:
                    size: self.size
                    pos: self.pos
                    
        Button:
            background_color: 0.1,0.1,0.1,0.5
            size: self.height * 1.8, root.height * 0.09
            pos_hint: {"center_y": 0.47, "center_x": 0.192}
            text: "Paste"
            on_press: root.paste()

        Button:
            background_color: 0.1,0.1,0.1,0.5
            size: self.height * 1.8, root.height * 0.09
            pos_hint: {"center_y": 0.57, "center_x": 0.192}
            text: "Copy"
            on_press: root.copy(txto.text)

        Button:
            background_color: 0.1,0.1,0.1,0.5
            size: self.height * 1.8, root.height * 0.09
            pos_hint: {"center_y": 0.37, "center_x": 0.192}
            text: "Clear"
            on_press: txto.text = ""
            on_press: txti.text = ""
            on_press: root.gethappy()
            on_press: root.pisca()

        Button:
            size: self.height * 2.5, root.height * 0.09
            pos_hint: {"center_y": 0.155, "center_x": 0.775}
            text: "Link Extract"
            on_press: root.links(txti.text)

        Button:
            size: self.height * 2.5, root.height * 0.09
            pos_hint: {"center_y": 0.055, "center_x": 0.775}
            text: "Exit"
            on_press: app.stop()

        Button:
            size: self.height * 2.5, root.height * 0.09
            pos_hint: {"center_y": 0.155, "center_x": 0.225}
            text: "Video Dowload"
            on_press: root.nt(True, txti.text)

        Button:
            size: self.height * 2.5, root.height * 0.09
            pos_hint: {"center_y": 0.055, "center_x": 0.225}
            text: "Music Download"
            on_press: root.nt(False, txti.text)
        
        Image:
            size_hint: None, None
            pos_hint: {"center_y": 0.445,"center_x": 0.8}
            size: self.height, root.height * 0.25
            id: pet1
            color: 1,1,1,0
            
        Image:
            size_hint: None, None
            id: pet2
            pos_hint: {"center_y": 0.445,"center_x": 0.8}
            size: self.height, root.height * 0.25
            color: 1,1,1,0
            
        Image:
            size_hint: None, None
            id: pet_sad
            pos_hint: {"center_y": 0.445,"center_x": 0.8}
            size: self.height, root.height * 0.25
            color: 1,1,1,0
            
        Image:
            size_hint: None, None
            id: lov1
            pos_hint: {"center_y": 0.445,"center_x": 0.8}
            size: self.height, root.height * 0.282
            color: 1,1,1,0
            
        Image:
            size_hint: None, None
            id: lov2
            pos_hint: {"center_y": 0.445,"center_x": 0.8}
            size: self.height, root.height * 0.282
            color: 1,1,1,0
""")


class MyApp(Widget):
    txti = ObjectProperty(None)
    txto = ObjectProperty(None)
    pet1 = ObjectProperty(None)
    pet2 = ObjectProperty(None)
    pet_sad = ObjectProperty(None)
    lov1 = ObjectProperty(None)
    lov2 = ObjectProperty(None)
    bg = ObjectProperty(None)

    def __init__(self):
        super().__init__()
        path = os.getcwd()
        #path = sys._MEIPASS
        self.txto.text += ""
        self.piscando = False
        self.happy = False
        self.love = False
        self.pisca()
        self.gethappy()
        self.pet1.source = path + "\imag\pet1.png"
        self.pet2.source = path + "\imag\pet2.png"
        self.pet_sad.source = path + "\imag\pet3.png"
        self.lov1.source = path + "\imag\lov1.png"
        self.lov2.source = path + "\imag\lov2.png"
        self.bg.source = path + "\imag\_bg.png"

    def fallinlove(self):
        self.happy = False
        self.love = True
        snt(self.fllv, ())

    def fllv(self):
        self.pet_sad.color = (1, 1, 1, 0)
        while self.love:
            self.lov1.color = (1, 1, 1, 1)
            time.sleep(0.5)
            if not self.love: break
            self.lov1.color = (1, 1, 1, 0)
            self.lov2.color = (1, 1, 1, 1)
            time.sleep(0.5)
            if not self.love: break
            self.lov1.color = (1, 1, 1, 1)
            self.lov2.color = (1, 1, 1, 0)
        self.lov1.color = (1, 1, 1, 0)
        self.lov2.color = (1, 1, 1, 0)

    def getsad(self):
        self.happy = False
        self.love = False
        self.pet_sad.color = (1, 1, 1, 1)

    def gethappy(self):
        self.happy = True
        self.love = False
        snt(self.gthp, ())

    def gthp(self):
        self.pet_sad.color = (1, 1, 1, 0)
        while self.happy:
            self.pet1.color = (1, 1, 1, 1)
            time.sleep(0.5)
            if not self.happy: break
            self.pet1.color = (1, 1, 1, 0)
            self.pet2.color = (1, 1, 1, 1)
            time.sleep(0.5)
            if not self.happy: break
            self.pet1.color = (1, 1, 1, 1)
            self.pet2.color = (1, 1, 1, 0)

        self.pet1.color = (1, 1, 1, 0)
        self.pet2.color = (1, 1, 1, 0)

    def pisca(self):
        snt(self.psc, ())

    def psc(self):
        self.piscando = True
        while self.piscando:
            self.txto.text += "_"
            time.sleep(0.5)
            if not self.piscando: break
            self.txto.text = self.txto.text[:-1]
            time.sleep(0.5)

    def paste(self):
        self.txti.text = clipboard.paste()

    def copy(self, x):
        clipboard.copy(x)

    def nt(self, vd, link=None):
        if vd:
            self.piscando = False
            self.txto.text = ""
            self.gethappy()
            snt(self.vd, (link,))
        else:
            self.piscando = False
            self.txto.text = ""
            self.gethappy()
            snt(self.mp3, (link,))

    def vd(self, link=None):
        self.txto.text = "Download Status: \n"
        try:
            if 'playlist' in link:
                ypl = Playlist(link)
                self.txto.text = "Baixando Playlist...\n"
                status = 0
                fails = []
                for url in ypl:
                    yt = YouTube(url)
                    try:
                        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(output_path='videos/')
                        status += 1
                        self.txto.text = f"Baixando Playlist...\nStatus: {status}/{len(ypl)}"
                    except:
                        fails.append(str(yt.title))

                if len(fails) < 1:
                    self.txto.text = "Downloads conluidos com sucesso !"
                    self.fallinlove()
                else:
                    self.txto.text = "Downloads conluidos !\nFalha ao baixar video(s):\n"
                    for x in fails:
                        self.txto.text += x + ', '
                    self.fallinlove()
            else:
                yt = YouTube(link)
                try:
                    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(output_path='videos/')
                    self.txto.text += '\n' + str(yt.title) + ' - Download Successful'
                    self.fallinlove()
                except:
                    self.txto.text += '\n' + str(yt.title) + ' - Download Fail'
                    self.getsad()

        except:
            self.getsad()
            self.txto.text = "Operation fail"

    def mp3(self, link=None):
        try:
            if 'playlist' in link:
                ypl = Playlist(link)
                self.txto.text = "Baixando Playlist...\n"
                status = 0
                fails = []
                for url in ypl:
                    yt = YouTube(url)
                    try:
                        out_file = yt.streams.get_audio_only().download(output_path='musicas/')
                        base, ext = os.path.splitext(out_file)
                        new_file = base + '.mp3'
                        os.rename(out_file, new_file)
                        status += 1
                        self.txto.text = f"Baixando Playlist...\nStatus: {status}/{len(ypl)}"
                    except:
                        fails.append(str(yt.title))

                if len(fails) < 1:
                    self.txto.text = "Downloads conluidos com sucesso !"
                    self.fallinlove()
                else:
                    self.txto.text = "Downloads conluidos !\nFalha ao baixar musica(s):\n"
                    for x in fails:
                        self.txto.text += x[0:10] + ', '
                    self.fallinlove()
            else:
                self.txto.text = "Download Status: \n"
                yt = YouTube(link)
                try:
                    out_file = yt.streams.get_audio_only().download(output_path='musicas/')
                    base, ext = os.path.splitext(out_file)
                    new_file = base + '.mp3'
                    os.rename(out_file, new_file)
                    self.txto.text += '\n' + str(yt.title) + ' - Download Successful'
                    self.fallinlove()
                except:
                    self.txto.text += '\n' + str(yt.title) + ' - Download Fail'
                    self.getsad()

        except:
            self.txto.text = "Operation fail"
            self.getsad()

    def links(self, s):
        self.piscando = False
        self.txto.text = ""
        a = re.findall(r'(https?://\S+)', s)
        for x in a:
            self.txto.text += x + '\n'
        if len(self.txto.text) > 1:
            self.fallinlove()
        else:
            self.gethappy()


class GuiApp(App):

    def build(self):
        return MyApp()


if __name__ == '__main__':
    GuiApp().run()
