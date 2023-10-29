import os
import random
from random import randint

def play_songs():
    n = random.randint(0,14)
    music_dir = 'c:/Users/Dani/Downloads/odaj/aj/Music/English/Awesome Vol. AJTG'
    songs = os.listdir(music_dir)
    os.startfile(os.path.join(music_dir,songs[n]))


