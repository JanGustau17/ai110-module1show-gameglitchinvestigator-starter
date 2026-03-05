from logic_utils import check_guess, update_score


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    # If secret is 50 and guess is 60, outcome should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    # If secret is 50 and guess is 40, outcome should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# --- Bug 1 fix: hint messages were inverted ---

def test_too_low_hint_says_go_higher():
    # BUG: a guess of 0 against secret 50 used to say "Go LOWER!" instead of "Go HIGHER!"
    _, message = check_guess(0, 50)
    assert "HIGHER" in message.upper()


def test_too_high_hint_says_go_lower():
    # BUG: a guess of 99 against secret 50 used to say "Go HIGHER!" instead of "Go LOWER!"
    _, message = check_guess(99, 50)
    assert "LOWER" in message.upper()


# --- Bug 6 fix: wrong guesses on even attempts gave +5 points ---

def test_wrong_guess_always_subtracts_score():
    # BUG: update_score gave +5 for "Too High" on even attempt numbers
    score_after = update_score(100, "Too High", attempt_number=2)
    assert score_after < 100
