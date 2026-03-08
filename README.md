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
The game is a number-guessing game where you guess a secret number within limited attempts, getting "Too High"/"Too Low" hints and earning/losing points based on correctness.

- [ ] Detail which bugs you found.
1. Inverted hints ("Too High" said "Go HIGHER!")
2. Hard range was 1–50 (easier than Normal's 1–100)
3. Attempts initialized to 1 but reset to 0 on New Game
4. Info banner hardcoded "1 and 100" regardless of difficulty
5. Game status never reset on New Game (stuck after win/loss)
6. New Game used randint(1, 100) instead of difficulty range
7. Secret cast to str on even attempts → lexicographic comparison
8. Wrong guesses on even attempts gave +5 points instead of −5

- [ ] Explain what fixes you applied.
1. Swapped hint messages in check_guess
2. get_range_for_difficulty("Hard") → (1, 200)
3. Changed initial attempts to 0
4. Updated banner to use {low} and {high} from difficulty
5. Added status = "playing" reset in New Game handler
6. New Game now uses randint(low, high)
7. Removed str(secret) cast — comparisons always use integers
8. Removed +5 branch in update_score — wrong guesses always subtract 5

## 📸 Demo

- [ ] [Insert a screenshot of your fixed, winning game here]
![alt text](image.png)


## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
