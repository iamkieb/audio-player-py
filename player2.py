from tkinter import *
from tkinter import filedialog
from pygame import mixer

class Player:
    def __init__(self, window):
        window.geometry('400x100'); window.title("Python Play"); window.resizable(0,0)
        Load = Button(window, text = 'Load', width = 10, font = ('Times',10), command =self.load)
        Play = Button(window, text = 'Play', width = 10, font = ('Times',10), command =self.play)
        Stop = Button(window, text = 'Stop', width = 10, font = ('Times',10), command =self.stop)
        Pause = Button(window, text = 'Pause', width = 10, font = ('Times',10), command =self.pause)
        Load.place(x=40,y=20); Play.place(x=150,y=20); Pause.place(x=270,y=20); Stop.place(x=150,y=60)
        self.music_file = False
        self.playing_state = False

    def load(self):
        self.music_file = filedialog.askopenfilename()
    def play(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()
    def pause(self):
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state = True
        else:
            mixer.music.pause()
            self.playing_state = False
    def stop(self):
        mixer.music.stop()

new_root = Tk()
player_app = Player(new_root)
new_root.mainloop()