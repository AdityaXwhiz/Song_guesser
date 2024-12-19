'''import pygame
import time
import random

# Initialize the mixer
pygame.mixer.init()

# Define a function to play the middle part of a song
def play_middle_part(song_path, duration=10):
    """
    Plays the middle part of the song for a specified duration.
    """
    try:
        # Load the song
        pygame.mixer.music.load(song_path)
        
        # Get the total length of the song
        pygame.mixer.music.play(start=0)  # Start playing to calculate the length
        time.sleep(0.5)  # Small delay to ensure song information is loaded
        total_length = pygame.mixer.Sound(song_path).get_length()
        pygame.mixer.music.stop()  # Stop playing

        # Calculate the starting point (middle part)
        start_time = total_length / 2 - duration / 2
        start_time = max(0, start_time)  # Ensure start_time is not negative

        # Play the middle part
        pygame.mixer.music.play(start=start_time)
        time.sleep(duration)
        pygame.mixer.music.stop()
    except Exception as e:
        print(f"Error playing song: {e}")

# Song dictionaries
Hindi = {
    r"D:\Music_guesser\songs\[Songs.PK] Kick - 13 - Tu Hi Tu (House Mix).mp3":"kick",
    r"D:\Music_guesser\songs\01 Baarish - Half Girlfriend (Ash King) 190Kbps(1).mp3": "baarish",
    r"D:\Music_guesser\songs\01 Ban Ja Rani - Tumhari Sulu (Guru) 320Kbps.mp3":"ban ja tu meri rani",
    r"D:\Music_guesser\songs\01 Chalti Hai Kya 9 Se 12 - Judwaa 2 - 190Kbps.mp3":"chalti hai kya 9 se 12",
    r"D:\Music_guesser\songs\01 Ik Vaari Aa - Raabta (Arijit Singh) 190Kbps.mp3":"ik vaari aa",
    r"D:\Music_guesser\songs\01 Ok Jaanu - Title Song (AR Rehman) 190Kbps.mp3":"ok jaanu",
    r"D:\Music_guesser\songs\02 Darkhaast - Shivaay (Arijit Singh) 190Kbps-1.mp3":"darkhaast",
    r"D:\Music_guesser\songs\02 Raabta - Title Song (Arijit Singh) 190Kbps.mp3":"raabta",
    r"D:\Music_guesser\songs\01. Oh Girl You're Mine.mp3":"o girl you are mine"
}

Hinglish = { 
           r"D:\Music_guesser\songs\[Songs.PK] Kick - 13 - Tu Hi Tu (House Mix).mp3":"kick",
           r"D:\Music_guesser\songs\01 Baarish - Half Girlfriend (Ash King) 190Kbps(1).mp3":"baarish",
           r"D:\Music_guesser\songs\01 Ban Ja Rani - Tumhari Sulu (Guru) 320Kbps.mp3":"ban ja tu meri rani",
           r"D:\Music_guesser\songs\01 Chalti Hai Kya 9 Se 12 - Judwaa 2 - 190Kbps.mp3":"chalti hai kya 9 se 12",
           r"D:\Music_guesser\songs\01 Ik Vaari Aa - Raabta (Arijit Singh) 190Kbps.mp3":"ik vaari aa",
           r"D:\Music_guesser\songs\01 Ok Jaanu - Title Song (AR Rehman) 190Kbps.mp3":"ok jaanu",
           r"D:\Music_guesser\songs\02 Darkhaast - Shivaay (Arijit Singh) 190Kbps-1.mp3":"darkhaast",
           r"D:\Music_guesser\songs\02 Raabta - Title Song (Arijit Singh) 190Kbps.mp3":"raabta",
           r"D:\Music_guesser\songs\01. Oh Girl You're Mine.mp3":"o girl you are mine",
           r"songs/WhatsApp Audio 2024-12-07 at 19.37.21_7cea9fce.mp3":"faded",
         r"D:\Music_guesser\songs\WhatsApp Audio 2024-12-07 at 19.37.22_66de4d6e.mp3":"bad boy",
         r"songs/WhatsApp Audio 2024-12-07 at 19.37.25_328d6a2d.mp3":"worth it",
         r"songs/WhatsApp Audio 2024-12-07 at 19.37.25_328d6a2d.mp3":"believer",
         r"D:\Music_guesser\songs\WhatsApp Audio 2024-12-07 at 19.37.26_dd986468.mp3":"no lies",
         r"D:\Music_guesser\songs\WhatsApp Audio 2024-12-07 at 19.37.27_19f266ce.mp3":"perfect",
         r"D:\Music_guesser\songs\WhatsApp Audio 2024-12-07 at 19.37.28_2b4b43c6.mp3":"without me",
         r"D:\Music_guesser\songs\WhatsApp Audio 2024-12-07 at 19.37.28_9509977e.mp3":"hey mamma"
}

English = {
    r"songs/WhatsApp Audio 2024-12-07 at 19.37.21_7cea9fce.mp3":"faded",
         r"D:\Music_guesser\songs\WhatsApp Audio 2024-12-07 at 19.37.22_66de4d6e.mp3":"bad boy",
         r"songs/WhatsApp Audio 2024-12-07 at 19.37.25_328d6a2d.mp3":"worth it",
         r"songs/WhatsApp Audio 2024-12-07 at 19.37.25_328d6a2d.mp3":"believer",
         r"D:\Music_guesser\songs\WhatsApp Audio 2024-12-07 at 19.37.26_dd986468.mp3":"no lies",
         r"D:\Music_guesser\songs\WhatsApp Audio 2024-12-07 at 19.37.27_19f266ce.mp3":"perfect",
         r"D:\Music_guesser\songs\WhatsApp Audio 2024-12-07 at 19.37.28_2b4b43c6.mp3":"without me",
         r"D:\Music_guesser\songs\WhatsApp Audio 2024-12-07 at 19.37.28_9509977e.mp3":"hey mamma"
}

# Function to start the game
def start_game():
    print("Hello Gamefreak, Welcome to the ultimate game of guessing songs!")
    print("Let's start the game by asking your preferences!")

    while True:
        # User inputs
        try:
            rounds = int(input("How many rounds would you like to play?\n(1) 3\n(2) 5\n(3) 7\n"))
            language = input("Select the language you prefer:\n 'e' for English\n 'Hi' for Hindi\n 'h' for Hinglish:\n").strip().lower()
        except ValueError:
            print("Invalid input. Please try again.")
            continue

        # Select dictionary based on language choice
        if language == "hi":
            selected_songs = list(Hindi.items())
        elif language == "e":
            selected_songs = list(English.items())
        elif language == "h":
            selected_songs = list(Hinglish.items())
        else:
            print("Invalid language choice. Please try again.")
            continue

        # Shuffle the songs
        random.shuffle(selected_songs)

        # Game logic
        score = 0
        for i in range(rounds):
            if i >= len(selected_songs):
                print("No more songs available. Ending game!")
                break

            song_path, song_name = selected_songs[i]
            print(f"Round {i + 1}: Playing music...")

            # Play the middle part of the song
            play_middle_part(song_path, duration=10)

            start_time = time.time()
            guess = input("Guess the song name: ").strip().lower()
            elapsed_time = time.time() - start_time

            if elapsed_time > 10:
                print("Time's up! No points for this round.")
            elif guess == song_name.lower():
                if elapsed_time < 4:
                    score += 30
                    print(f"Wohoo! You got 30 points!\nTime taken: {round(elapsed_time, 2)} seconds")
                elif elapsed_time < 7:
                    score += 20
                    print(f"Wohoo! You got 20 points!\nTime taken: {round(elapsed_time, 2)} seconds")
                elif elapsed_time <= 10:
                    score += 15
                    print(f"Wohoo! You got 15 points!\nTime taken: {round(elapsed_time, 2)} seconds")
            else:
                print(f"Better luck next time. The correct answer was '{song_name}'.")
            
            print(f"Your current score is: {score}\n")

        print(f"Game Over! Your total score is: {score}")
        
        replay = input("Do you want to play again? (yes/no): ").strip().lower()
        if replay != "yes":
            print("Thanks for playing! Goodbye!")
            break

# Run the game
start_game()'''
