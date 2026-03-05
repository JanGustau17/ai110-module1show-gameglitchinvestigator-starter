from logic_utils import check_guess, update_score


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# --- Bug 1 fix: hint messages were inverted ---

def test_too_low_message_says_go_higher():
    # BUG: entering 0 (below secret) used to say "Go LOWER!" instead of "Go HIGHER!"
    # Expected: when guess < secret, message should direct player upward
    _, message = check_guess(0, 50)
    assert "HIGHER" in message.upper(), f"Expected 'HIGHER' in message but got: {message}"


def test_too_high_message_says_go_lower():
    # BUG: when guess was above secret, message said "Go HIGHER!" instead of "Go LOWER!"
    # Expected: when guess > secret, message should direct player downward
    _, message = check_guess(99, 50)
    assert "LOWER" in message.upper(), f"Expected 'LOWER' in message but got: {message}"


def test_hint_message_not_inverted_symmetry():
    # Both directions should never give the same message word
    _, msg_low = check_guess(1, 50)
    _, msg_high = check_guess(99, 50)
    assert msg_low != msg_high, "Too Low and Too High should not produce identical messages"


# --- Bug 6 fix: score rewarded wrong guesses on even attempts ---

def test_too_high_always_subtracts_score():
    # BUG: on even attempt numbers, a Too High guess gave +5 points instead of -5
    # Expected: wrong guesses should always reduce the score
    score_after_odd = update_score(100, "Too High", attempt_number=1)
    score_after_even = update_score(100, "Too High", attempt_number=2)
    assert score_after_odd < 100, "Too High on odd attempt should subtract from score"
    assert score_after_even < 100, "Too High on even attempt should also subtract, not add"


def test_too_low_always_subtracts_score():
    # Too Low should always subtract regardless of attempt number
    score_after = update_score(100, "Too Low", attempt_number=2)
    assert score_after < 100, "Too Low should always subtract from score"
