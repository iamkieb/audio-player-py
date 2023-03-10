from pygame import mixer


mixer.init() #init pygame mixer

mixer.music.load('[Asset Path Goes Here]')

mixer.music.play()
mixer.music.stop()
