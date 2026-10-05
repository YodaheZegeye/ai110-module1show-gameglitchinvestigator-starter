# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
At first, it looked fine. It's a guessing game for numbers between 1-100
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
tells me to guess between 1 and a 100 and tells me to go lower everytime. if I guess the correct number and then start a new game, the "your answer is correct", doesn't disappear. the show hint button always shows the hint even if you uncheck it

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| | | | |
| | | | |
| | | | |

--- I've listed all the bugs above

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used claude code in terminal here in VSCode
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- app.py:36-39: swapped the hint strings — "Too High" now says "Go LOWER!" and "Too Low" now says "Go HIGHER!". Also dropped the dead TypeError branch that was papering over the int/str mismatch. I tested this out using streamlit pytest and checked that it worked
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.
I used Opus while making this and didn't have anything I rejected. The code made sense for me since the task at hand was simple
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
The only way possible which is through testing using pytest and streamlit
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
 Running pytest showed all 5 tests passing against the fix, and when I monkey-patched check_guess back to the buggy version my two new regression tests failed while the original three still passed — proving the pre-existing tests only checked outcome labels, not the user-facing direction messages where the real bug lived.
- Did AI help you design or understand any tests? How?
 Yes. It suggested asserting "LOWER" in message.upper() instead of the exact emoji string so the tests stay robust to wording changes, and proposed temporarily reverting check_guess to confirm the new tests actually fail on the bug they claim to catch.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

--- Every time you click a button, Streamlit forgets everything and redraws the whole page from scratch — "session state" is the little notebook where you jot things down (like the secret number or your score) so the game can remember them across clicks instead of starting over every time.

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
 -- I want to learn how to plan and not let AI just replace my code without me reviewing it
- What is one thing you would do differently next time you work with AI on a coding task?
 -- Do better prompting and plan before implementing my code
- In one or two sentences, describe how this project changed the way you think about AI generated code.
 --  This project taught me that running the code and playing with it myself is the real test. AI's output is a starting draft to interrogate, not a finished product to trust
