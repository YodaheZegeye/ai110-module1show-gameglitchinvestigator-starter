from logic_utils import check_guess


def test_winning_guess():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


def test_too_high_hint_tells_player_to_go_lower():
    # Regression: hint strings used to be swapped — "Too High" wrongly said
    # "Go HIGHER!", sending the player further from the secret every turn.
    _, message = check_guess(80, 50)
    assert "LOWER" in message.upper()
    assert "HIGHER" not in message.upper()


def test_too_low_hint_tells_player_to_go_higher():
    # Regression: "Too Low" used to say "Go LOWER!", trapping the player
    # below the secret forever.
    _, message = check_guess(20, 50)
    assert "HIGHER" in message.upper()
    # Guard against substring collision: "HIGHER" contains neither "LOWER"
    # nor any lone occurrence of it, so this check is safe.
    assert "LOWER" not in message.upper().replace("HIGHER", "")
