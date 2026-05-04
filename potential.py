import time
import random
import pyautogui

# Function to mimic human-like typing with random pauses and occasional mistakes
def human_typing(text, pause_min, pause_max, typo_chance):
    """
    text: the string to type
    pause_min, pause_max: delay between keystrokes (in seconds)
    typo_chance: probability of making a typo per character (0.0 - 1.0)
    """
    for char in text:
        # Randomly decide whether to make a typo
        if random.random() < typo_chance and char.isprintable() and char != '\n':
            wrong_char = random.choice('abcdefghijklmnopqrstuvwxyz,.!?')
            pyautogui.typewrite(wrong_char)
            time.sleep(random.uniform(pause_min, pause_max))
            pyautogui.press('backspace')
            time.sleep(random.uniform(pause_min, pause_max))
        
        pyautogui.typewrite(char)
        time.sleep(random.uniform(pause_min, pause_max))

# Function to simulate very short random breaks
def random_break(min_seconds, max_seconds):
    break_time = random.randint(min_seconds, max_seconds)
    print(f"Taking a short break for {break_time} seconds...")
    time.sleep(break_time)

# Main function to type the content into Google Docs
def type_in_google_doc(file_path, chunk_size, pause_min, pause_max, typo_chance, break_min, break_max):
    with open(file_path, 'r') as file:
        input_text = file.read()

    print("Please focus the Google Doc window and click to place the cursor at the start of the document.")
    time.sleep(5)

    print("Starting to type...")

    for i in range(0, len(input_text), chunk_size):
        chunk = input_text[i:i+chunk_size]
        human_typing(chunk, pause_min, pause_max, typo_chance)

        # Take a short break after each chunk
        if i + chunk_size < len(input_text):
            random_break(break_min, break_max)

    print("Finished typing the document!")

# -------------------- CUSTOMIZATION VARIABLES --------------------
file_path = './sampleScript.txt'  # Path to your text file
chunk_size = 60        # chars per chunk
pause_min = 0.08       # min delay per keystroke (s)
pause_max = 0.12       # max delay per keystroke (s)
typo_chance = 0.02     # 2% chance of typo per character
break_min = 4          # min break between chunks (s)
break_max = 6          # max break between chunks (s)
# ------------------------------------------------------------------

# Start typing with the customized settings
type_in_google_doc(file_path, chunk_size, pause_min, pause_max, typo_chance, break_min, break_max)