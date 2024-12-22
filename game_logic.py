import pygame
import time
import random
from songs_dictionaries import *


# Initialize the mixer
pygame.mixer.init()






# Function to play the middle part of the song for a specific duration
def play_middle_part(file_path, duration=10):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play(start=30)  # Starts playback at 30 seconds
    time.sleep(duration)
    pygame.mixer.music.stop()



# Main game function
def play_game():
    print("Hello Gamefreak, Welcome to the ultimate game of guessing songs!")
    print("Let's start the game by asking your preferences!")

    # User inputs
    try:
        rounds = int(input("How many rounds would you like to play?\n(1) 3\n(2) 5\n(3) 7\n"))
        language = input("Select the language you prefer:\n'e' for English\n'h' for Hindi\n'p' for Punjabi\n'm' for Mixed:\n").strip().lower()
    except ValueError:
        print("Invalid input. Please restart the game.")
        return

    print("""
Rules:
1. Guess either the song title or the movie name.
2. Artist name could also be guessed.
3. Spelling mistakes are not allowed.
4. Correct guesses give you points on time taken basis(30 for <4 seconds|20 for <7 seconds|15 for <10 seconds).
5. Answers after the 10 seconds time frame are not accepted
""")

    input("Press Enter to start the game!")

    # Select dictionary based on language choice
    if language == "h":
        selected_songs = list(Hindi.items())
    elif language == "e":
        selected_songs = list(English.items())
    elif language == "p":
        selected_songs = list(Punjabi.items())
    elif language == "m":
        selected_songs = list(mixed.items())
    else:
        print("Invalid language choice. Please restart the game.")
        return

    # Shuffle the songs
    random.shuffle(selected_songs)

    # Game logic
    score = 0
    for i in range(rounds):
        if i >= len(selected_songs):
            print("No more songs available. Ending game!")
            break

        song_path, valid_answers = selected_songs[i]
        print(f"Round {i + 1}:🎶🎵.....Playing music...🎶🎵")

        # Play the middle part of the song
        play_middle_part(song_path, duration=10)

        start_time = time.time()
        guess = input("Guess the song name: ").strip().lower()
        elapsed_time = time.time() - start_time

        if elapsed_time > 10:
            print("Time's up! No points for this round.")
        elif guess in [answer.lower() for answer in valid_answers]:
            if elapsed_time < 4:
                score += 30
                print(f"Wohoo! You got 30 points!\nTime taken: {round(elapsed_time, 2)} seconds")
            elif elapsed_time < 7:
                score += 20
                print(f"Great! You got 20 points!\nTime taken: {round(elapsed_time, 2)} seconds")
            elif elapsed_time <= 10:
                score += 15
                print(f"Nice! You got 15 points!\nTime taken: {round(elapsed_time, 2)} seconds")
        else:
            print(f"Better luck next time.")
        
        print(f"Your current score is: {score}\n")

    print(f"Game Over! Your total score is: {score}")

# Replay loop
while True:
    play_game()
    replay = input("Do you want to play again? (y/n): ").strip().lower()
    if replay != 'y':
        print("Thanks for playing! Goodbye!")
        break
