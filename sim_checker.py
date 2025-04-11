def is_valid_sim(sim_number):
    if len(sim_number) == 11 and sim_number.startswith("09") and sim_number.isdigit():
        return True
    return False


def check_sim_card(sim_number):
    if is_valid_sim(sim_number):
        return f"SIM card number {sim_number} is valid."
    else:
        return f"SIM card number {sim_number} is invalid."


print(check_sim_card("09171234567"))
print(check_sim_card("12345"))
