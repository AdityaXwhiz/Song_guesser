import pygame
import time
import random
from songs_dictionaries import *
'''import tkinter as tk

def countdown_timer(count):
    mins, secs = divmod(count, 60)
    timer_label.config(text=f"{mins:02d}:{secs:02d}")
    if count > 0:
        root.after(1000, countdown_timer, count - 1)
    else:
        timer_label.config(text="Time's up!")'''

pygame.mixer.init()


# Hindi= {
#     r"D:\Music_guesser\songs\[Songs.PK] Kick - 13 - Tu Hi Tu (House Mix).mp3":"kick",
#            r"D:\Music_guesser\songs\01 Baarish - Half Girlfriend (Ash King) 190Kbps(1).mp3": "baarish",
#            r"D:\Music_guesser\songs\01 Ban Ja Rani - Tumhari Sulu (Guru) 320Kbps.mp3":"ban ja tu meri rani",
#            r"D:\Music_guesser\songs\01 Chalti Hai Kya 9 Se 12 - Judwaa 2 - 190Kbps.mp3":"chalti hai kya 9 se 12",
#            r"D:\Music_guesser\songs\01 Ik Vaari Aa - Raabta (Arijit Singh) 190Kbps.mp3":"ik vaari aa",
#            r"D:\Music_guesser\songs\01 Ok Jaanu - Title Song (AR Rehman) 190Kbps.mp3":"ok jaanu",
#            r"D:\Music_guesser\songs\02 Darkhaast - Shivaay (Arijit Singh) 190Kbps-1.mp3":"darkhaast",
#            r"D:\Music_guesser\songs\02 Raabta - Title Song (Arijit Singh) 190Kbps.mp3":"raabta",
#            r"D:\Music_guesser\songs\01. Oh Girl You're Mine.mp3":"o girl you are mine"
# }

# Hinglish={ r"D:\Music_guesser\songs\[Songs.PK] Kick - 13 - Tu Hi Tu (House Mix).mp3":"kick",
#            r"D:\Music_guesser\songs\01 Baarish - Half Girlfriend (Ash King) 190Kbps(1).mp3":"baarish",
#            r"D:\Music_guesser\songs\01 Ban Ja Rani - Tumhari Sulu (Guru) 320Kbps.mp3":"ban ja tu meri rani",
#            r"D:\Music_guesser\songs\01 Chalti Hai Kya 9 Se 12 - Judwaa 2 - 190Kbps.mp3":"chalti hai kya 9 se 12",
#            r"D:\Music_guesser\songs\01 Ik Vaari Aa - Raabta (Arijit Singh) 190Kbps.mp3":"ik vaari aa",
#            r"D:\Music_guesser\songs\01 Ok Jaanu - Title Song (AR Rehman) 190Kbps.mp3":"ok jaanu",
#            r"D:\Music_guesser\songs\02 Darkhaast - Shivaay (Arijit Singh) 190Kbps-1.mp3":"darkhaast",
#            r"D:\Music_guesser\songs\02 Raabta - Title Song (Arijit Singh) 190Kbps.mp3":"raabta",
#            r"D:\Music_guesser\songs\01. Oh Girl You're Mine.mp3":"o girl you are mine",
#            r"songs/WhatsApp Audio 2024-12-07 at 19.37.21_7cea9fce.mp3":"faded",
#          r"D:\Music_guesser\songs\WhatsApp Audio 2024-12-07 at 19.37.22_66de4d6e.mp3":"bad boy",
#          r"songs/WhatsApp Audio 2024-12-07 at 19.37.25_328d6a2d.mp3":"worth it",
#          r"songs/WhatsApp Audio 2024-12-07 at 19.37.25_328d6a2d.mp3":"believer",
#          r"D:\Music_guesser\songs\WhatsApp Audio 2024-12-07 at 19.37.26_dd986468.mp3":"no lies",
#          r"D:\Music_guesser\songs\WhatsApp Audio 2024-12-07 at 19.37.27_19f266ce.mp3":"perfect",
#          r"D:\Music_guesser\songs\WhatsApp Audio 2024-12-07 at 19.37.28_2b4b43c6.mp3":"without me",
#          r"D:\Music_guesser\songs\WhatsApp Audio 2024-12-07 at 19.37.28_9509977e.mp3":"hey mamma"

# }
    

# English={r"songs/WhatsApp Audio 2024-12-07 at 19.37.21_7cea9fce.mp3":"faded",
#          r"D:\Music_guesser\songs\WhatsApp Audio 2024-12-07 at 19.37.22_66de4d6e.mp3":"bad boy",
#          r"songs/WhatsApp Audio 2024-12-07 at 19.37.25_328d6a2d.mp3":"worth it",
#          r"songs/WhatsApp Audio 2024-12-07 at 19.37.25_328d6a2d.mp3":"believer",
#          r"D:\Music_guesser\songs\WhatsApp Audio 2024-12-07 at 19.37.26_dd986468.mp3":"no lies",
#          r"D:\Music_guesser\songs\WhatsApp Audio 2024-12-07 at 19.37.27_19f266ce.mp3":"perfect",
#          r"D:\Music_guesser\songs\WhatsApp Audio 2024-12-07 at 19.37.28_2b4b43c6.mp3":"without me",
#          r"D:\Music_guesser\songs\WhatsApp Audio 2024-12-07 at 19.37.28_9509977e.mp3":"hey mamma"
        

# }

random.shuffle(Hindi.items())
random.shuffle(English.items())
random.shuffle(Hinglish.items())

print("Hello Gamefreak , Welcome to the ultimate game of guessing songs!")
print("Lets start the game asking your preferences!")
a=int(input("How many rounds would you like to play?\n(1)3 \n(2)5\n(3)7\n"))
b=input("Select the language you prefer\n 'e' for English \n 'Hi' for Hindi \n 'h' for Hinglish:\n")
print("Rules:\n(1)Guess either the song title or the movie name. \3n3(2)Time limit of 10 seconds is given to guess.\n(3)Spelling mistakes are not accountable\n(4)Correct guess gives you certain points depending upon the time taken\n(5)Answers after the alloted time are not accepted)")
print("You Are ready to start the game!\n Press Enter to start the game!")
c=input()

tpd=1
while tpd<=a:
    tpd+=1
    if b=="Hi":
        for track in Hindi:
            print("Playing Music...........")
            pygame.mixer.music.load(track)
            pygame.mixer.music.play()
            time.sleep(10)
            pygame.mixer.music.stop()
            guess=input("Guess the song name:")
            if guess in Hindi.values():
                print("Wohoo!You get 10 points")
            else:
                print("Better luck next time")
        
    elif b=="e":
        for track in English:
            print("Playing Music...........")
            pygame.mixer.music.load(track)
            pygame.mixer.music.play()
            time.sleep(10)
            pygame.mixer.music.stop()
            guess=input("Guess the song name:")
            if guess in English.values():
                 print("Wohoo!You get 10 points")
            else:
                 print("Better luck next time")
        
    elif b=="h":
            for track in Hinglish:
                print("Playing Music...........")
                pygame.mixer.music.load(track)
                pygame.mixer.music.play()
                time.sleep(10)
                pygame.mixer.music.stop()
                guess=input("Guess the song name:")

                if guess in Hinglish.values():             
                    print("Wohoo!You get 10 points")
                else:
                    print("Better luck next time")
           
