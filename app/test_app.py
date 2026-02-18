import pytest
from streamlit.testing.v1 import AppTest

def test_game_flow_and_restart():
    # 1. Initialize the app from your filename (e.g., 'main.py')
    at = AppTest.from_file("main.py").run()
    
    # 2. Mock a known secret number for predictable testing
    at.session_state.secret_number = 42
    at.run()

    # 3. Simulate a WRONG guess (to test feedback logic)
    at.number_input(key="user_guess_input").set_value(10).run()
    at.button(label="Submit Guess").click().run()
    assert "Too low" in at.session_state.game_message
    assert at.session_state.guesses_left == 6

    # 4. Simulate a WINNING guess
    at.number_input(key="user_guess_input").set_value(42).run()
    at.button(label="Submit Guess").click().run()
    assert at.session_state.game_over is True
    assert "Congratulations" in at.session_state.game_message

    # 5. RESOLVE COVERAGE: Click the 'Restart Game' button
    # This specifically covers the 'Uncovered code' block in your snippet
    at.button(label="Restart Game").click().run()
    
    # Verify reset state
    assert at.session_state.game_over is False
    assert at.session_state.guesses_left == 7
    assert "New game started" in at.session_state.game_message

def test_game_over_loss():
    at = AppTest.from_file("main.py").run()
    at.session_state.secret_number = 50
    at.session_state.guesses_left = 1
    at.run()

    # Make the final failing guess
    at.number_input(key="user_guess_input").set_value(1).run()
    at.button(label="Submit Guess").click().run()
    
    assert at.session_state.game_over is True
    assert "Game over" in at.session_state.game_message
