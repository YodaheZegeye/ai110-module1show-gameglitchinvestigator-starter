# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
A simple number-guessing game where the player tries to guess a secret number within a limited number of attempts, using "higher" or "lower" hints to narrow it down.
- [ ] Detail which bugs you found.
 - The game always said "between 1 and 100" even on Easy or Hard, and the hints pointed the wrong way (telling me to go lower when I needed to go higher).
  - After winning and clicking New Game, the "You already won" message wouldn't go away.
  - The "Show hint" checkbox didn't actually show me a hint when I clicked it.
- [ ] Explain what fixes you applied.
 - Made the range message match the chosen difficulty and swapped the hint directions so
they point toward the secret.
  - Made New Game fully reset the game, score, status, and messages included, so a fresh
 round actually starts fresh.
  - Flipped the hint checkbox so clicking it turns hints on, and made the last hint stay visible so toggling the box works right away.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. The number to guess is let's say 27. User guesses 47
2. The game returns Too High
3. The user guesses 15
4. Game returns Too Low
5. The user guesses 27
6. Game ends because you guessed the correct number and have the option to restart a new game

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
