import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from logic_utils import check_guess, update_score, get_range_for_difficulty, parse_guess


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


# --- Bug fix: Hard difficulty range was 1–50 (easier than Normal's 1–100) ---

def test_hard_difficulty_range_is_larger_than_normal():
    # BUG: get_range_for_difficulty("Hard") returned (1, 50), making Hard easier than Normal (1–100)
    _, hard_high = get_range_for_difficulty("Hard")
    _, normal_high = get_range_for_difficulty("Normal")
    assert hard_high > normal_high, f"Hard upper bound ({hard_high}) should exceed Normal's ({normal_high})"

def test_hard_difficulty_range_is_1_to_200():
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 200


# --- Bug fix: secret converted to str on even attempts, causing lexicographic comparison ---

def test_numeric_comparison_not_lexicographic():
    # BUG: on even attempts secret was str(secret), so check_guess(9, "50") compared "9" > "50" = True
    # and returned "Too High" even though 9 < 50. After the fix, 9 < 50 → "Too Low".
    outcome, _ = check_guess(9, 50)
    assert outcome == "Too Low", "9 < 50 should be 'Too Low', not 'Too High' (lexicographic bug)"

def test_numeric_comparison_large_vs_small():
    # Mirror case: 90 > 5 should be "Too High", not confused by string ordering
    outcome, _ = check_guess(90, 5)
    assert outcome == "Too High"
