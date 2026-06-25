# AutomatedEdit-GoogleDocs

A Python script that types text into Google Docs in a way that looks human — including randomized keystroke delays, occasional typos with self-corrections, and short breaks between chunks.

## What It Does

Given any text file, the script opens a keyboard stream and types the content character-by-character into whatever window is focused (intended to be Google Docs). It uses:

- **Randomized inter-keystroke delays** to avoid a mechanical rhythm
- **Simulated typos** — a configurable percentage of characters are typed wrong, then immediately backspaced and corrected
- **Chunk-based pauses** — the text is broken into chunks, with a randomized rest between each, mimicking natural writing sessions

## Usage

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Put your content in a `.txt` file (a sample is included as `sampleScript.txt`).

3. Edit the configuration block at the bottom of `potential.py`:
   ```python
   file_path = './sampleScript.txt'  # path to your text
   chunk_size = 60        # characters per typing burst
   pause_min = 0.08       # minimum delay between keystrokes (seconds)
   pause_max = 0.12       # maximum delay between keystrokes (seconds)
   typo_chance = 0.02     # probability of a typo per character
   break_min = 4          # minimum rest between chunks (seconds)
   break_max = 6          # maximum rest between chunks (seconds)
   ```

4. Run the script, then quickly click into your Google Doc to focus it:
   ```
   python potential.py
   ```

The script waits 5 seconds after launch before starting, giving you time to focus the document.

## Dependencies

- [PyAutoGUI](https://pyautogui.readthedocs.io/) — keyboard and mouse automation
- Python 3.x

## Notes

This was a small personal automation experiment. The core interest was in how randomness and probabilistic error simulation can make programmatic output feel organic — something that comes up in a lot of UI testing and simulation contexts.
