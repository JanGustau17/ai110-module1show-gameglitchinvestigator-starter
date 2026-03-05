# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

When I first ran the game, it appeared to work on the surface — it accepted input and showed messages — but the hints were completely wrong and the score behaved strangely. After digging in, I found multiple bugs that made the game unplayable and untrustworthy.

**Bug 1: The hints were backwards**
I expected that guessing too low (like entering `0`) would tell me to go higher. Instead, the game said "📉 Go LOWER!" — which is the opposite of what I needed. The `check_guess` function had the messages swapped: when `guess > secret` it said "Go HIGHER!" and when `guess < secret` it said "Go LOWER!", both pointing the player in the wrong direction every single time.

**Bug 2: The range hint in the info bar didn't match the selected difficulty**
I expected the instruction text to say something like "Guess a number between 1 and 20" when playing on Easy. Instead, it always displayed "Guess a number between 1 and 100" regardless of which difficulty was selected. The code had `"1 and 100"` hardcoded into the `st.info` message instead of using the `{low}` and `{high}` variables that were already calculated from the difficulty setting.

**Bug 3: After winning or losing, the New Game button did nothing**
I expected clicking "New Game 🔁" after a completed round to reset the game and let me play again. Instead, the game stayed frozen on the win or loss screen no matter how many times I clicked it. The issue was that the `status` field in session state was never reset — it stayed `"won"` or `"lost"` even after the new game started, so the app immediately hit `st.stop()` on every rerun and blocked all input.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
