from sim_checker import is_valid_sim, check_sim_card

def test_is_valid_sim():
    assert is_valid_sim("09171234567") == True
    assert is_valid_sim("0917123") == False
    assert is_valid_sim("12345678901") == False
    assert is_valid_sim("0917123456A") == False

def test_check_sim_card():
    assert check_sim_card("09171234567") == "SIM card number 09171234567 is valid."
    assert check_sim_card("0917123") == "SIM card number 0917123 is invalid."
    assert check_sim_card("12345678901") == "SIM card number 12345678901 is invalid."
    assert check_sim_card("0917123456A") == "SIM card number 0917123456A is invalid."
    