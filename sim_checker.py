def is_valid_sim(sim_number):
    """Checks if the given SIM card number is valid."""
    if len(sim_number) == 11 and sim_number.startswith("09") and sim_number.isdigit():
        return True
    return False

def check_sim_card(sim_number):
    """Provides feedback on SIM card validity."""
    if is_valid_sim(sim_number):
        return f"SIM card number {sim_number} is valid."
    else:
        return f"SIM card number {sim_number} is invalid."

print(check_sim_card("09171234567"))
print(check_sim_card("12345"))
