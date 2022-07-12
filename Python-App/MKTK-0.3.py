from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from pytube import YouTube
from pytube import Playlist
import os
import re
from kivy.lang import Builder
import clipboard
from _thread import start_new_thread

Builder.load_string("""
<Button>:
    font_size: root.height * 0.25
    color: 0.5, 0.75, 0.75, 1
    size_hint: 0.45,0.1
    background_color: 1,1,1,0.75
    color: 1,1,1,0.90

<MyApp>
    txti: txti
    txto: txto
    FloatLayout:
        size: root.width, root.height

        Image:
            size: root.height*2.26, root.height
            size_hint_x: None
            pos_hint: {"center_x": 0.5}
            source: '.data/bg.png'
            keep_ratio: True
            allow_stretch: True

        TextInput:
            id: txti
            background_color: 1,1,1,0.5
            color: 1,1,1,0.75
            font_size: root.height * 0.04
            size_hint: 0.9, 0.1
            pos_hint: {"top": 0.95, "x": 0.05}

        Label:
            size_hint: 0.6, None
            pos_hint: {"top": 0.845, "x": 0.05}
            height: root.height *0.59
            text_size: self.size
            halign: 'left'
            valign: 'top'
            id: txto

            canvas.before:
                Color:
                    rgba: 0.1,0.1,0.1,0.5
                Rectangle:
                    size: self.size
                    pos: self.pos

        Button:
            background_color: 0.1,0.1,0.1,0.5
            text: "Copy"
            pos_hint: {"top": 0.451, "x": 0.655}
            size_hint_x: 0.2949
            on_press: root.copy(txto.text)

        Button:
            background_color: 0.1,0.1,0.1,0.5
            text: "Clear"
            pos_hint: {"top": 0.35, "x": 0.655}
            size_hint_x: 0.2949
            on_press: txto.text = ""
            on_press: txti.text = ""

        Label:
            size_hint: None, 0.5
            width: self.height * 0.5
            pos_hint: {"top": 0.755, "x": 0.65}
            height: root.height *0.59
            text_size: self.size
            halign: 'left'
            valign: 'top'
            id: kuroki3
            keep_ratio: True
            canvas.before:
                Rectangle:
                    source: ".data/kuroki_3.png"
                    size: self.size
                    pos: self.pos

        Label:
            size_hint: None, 0.5
            width: self.height * 0.5
            pos_hint: {"top": 0.845, "x": 0.65}
            height: root.height *0.59
            text_size: self.size
            halign: 'left'
            valign: 'top'
            id: kuroki1
            keep_ratio: True
            canvas.before:
                Rectangle:
                    source: ".data/kuroki_1.png"
                    size: self.size
                    pos: self.pos
        Label:
            size_hint: None, 0.5
            width: self.height * 0.5
            pos_hint: {"top": 0.845, "right": 0.65}
            height: root.height *0.59
            text_size: self.size
            halign: 'left'
            valign: 'top'
            id: kuroki2
            keep_ratio: True
            canvas.before:
                Rectangle:
                    source: ".data/kuroki_2.png"
                    size: self.size
                    pos: self.pos

        Button:
            pos_hint: {"y": 0.1501, "x": 0.05}
            text: "Video Dowload"
            on_press: root.nt(True, txti.text)

        Button:
            pos_hint: {"y": 0.1501, "x": 0.5}
            text: "Music Download"
            on_press: root.nt(False, txti.text)

        Button:
            pos_hint: {"y": 0.05, "x": 0.05}
            text: "Link Extract"
            on_press: root.links(txti.text)

        Button:
            pos_hint: {"y": 0.05, "x": 0.5}
            text: "Exit"
            on_press: app.stop()



""")


class MyApp(Widget):

    txti = ObjectProperty(None)
    txto = ObjectProperty(None)


    def __init__(self):
        super().__init__()
        self.txto.text += ""

    def copy(self, x):
        clipboard.copy(x)

    def nt(self, vd, link=None):
        if vd:
            start_new_thread(self.vd, (link,))
        else:
            start_new_thread(self.mp3, (link,))

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
                else:
                    self.txto.text = "Downloads conluidos !\nFalha ao baixar video(s):\n"
                    for x in fails:
                        self.txto.text += x + '\n'
            else:
                yt = YouTube(link)
                try:
                    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(output_path='videos/')
                    self.txto.text += '\n' + str(yt.title) + ' - Download Successful'
                except:
                    self.txto.text += '\n' + str(yt.title) + ' - Download Fail'
        except:
            self.txto.text = "Operation fail :("

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
                else:
                    self.txto.text = "Downloads conluidos !\nFalha ao baixar musica(s):\n"
                    for x in fails:
                        self.txto.text += x + '\n'
            else:
                self.txto.text = "Download Status: \n"
                yt = YouTube(link)
                try:
                    out_file = yt.streams.get_audio_only().download(output_path='musicas/')
                    base, ext = os.path.splitext(out_file)
                    new_file = base + '.mp3'
                    os.rename(out_file, new_file)
                    self.txto.text += '\n' + str(yt.title) + ' - Download Successful'
                except:
                    self.txto.text += '\n' + str(yt.title) + ' - Download Fail'

        except:
            self.txto.text = "Operation fail :("

    def links(self, s):

        a = re.findall(r'(https?://\S+)', s)

        for x in a:
            self.txto.text += x + '\n'


class GuiApp(App):

    def __init__(self):
        super().__init__()

    def build(self):
        return MyApp()


if __name__ == '__main__':
    GuiApp().run()
