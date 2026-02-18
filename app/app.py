import streamlit as st
import random


MIN_NUM = 1
MAX_NUM = 100
MAX_GUESSES = 7


# Initialize the secret number and number of guesses in session state
if 'secret_number' not in st.session_state:
    st.session_state.secret_number = random.randint(MIN_NUM, MAX_NUM)
if 'guesses_left' not in st.session_state:
    st.session_state.guesses_left = MAX_GUESSES
if 'game_message' not in st.session_state:
    st.session_state.game_message = f"I have selected a number between {MIN_NUM} and {MAX_NUM}. Can you guess it in {MAX_GUESSES} tries?"
if 'game_over' not in st.session_state:
    st.session_state.game_over = False

# --- Functions ---
def restart_game():
    """Resets the game state."""
    st.session_state.secret_number = random.randint(MIN_NUM, MAX_NUM)
    st.session_state.guesses_left = MAX_GUESSES
    st.session_state.game_message = f"New game started! Guess a number between {MIN_NUM} and {MAX_NUM}."
    st.session_state.game_over = False

def check_guess(guess):
    """Checks the user's guess and updates the game state."""
    if st.session_state.game_over:
        return

    st.session_state.guesses_left -= 1

    if guess == st.session_state.secret_number:
        st.session_state.game_message = "🎉 Congratulations! You guessed the correct number!"
        st.session_state.game_over = True
    elif st.session_state.guesses_left <= 0:
        st.session_state.game_message = f"Game over! The number was {st.session_state.secret_number}."
        st.session_state.game_over = True
    elif guess < st.session_state.secret_number:
        st.session_state.game_message = "Too low! Try a higher number."
    else:
        st.session_state.game_message = "Too high! Try a lower number."

# --- App UI ---
st.title("🎯 Guess the Number Game")

st.write(st.session_state.game_message)

if not st.session_state.game_over:
    st.write(f"Guesses left: {st.session_state.guesses_left}")
    
    # Use number_input widget for user input
    user_guess = st.number_input(
        f"Enter a number between {MIN_NUM} and {MAX_NUM}:",
        min_value=MIN_NUM,
        max_value=MAX_NUM,
        step=1,
        key="user_guess_input" # Unique key for the widget
    )

    # Use a button to submit the guess
    if st.button("Submit Guess"):
        # The value from number_input is used here
        check_guess(int(user_guess))
else:
    # Option to restart the game
    st.button("Restart Game", on_click=restart_game)
