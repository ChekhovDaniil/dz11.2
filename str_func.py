def capital_letters():
    """Делает загланые все буквы каждого каждого слова в строке"""
    str_input = input()
    return str_input.upper()

def capitalized_first_letter():
    """Делает заглавные первые буквы каждого слова в строке"""
    letter_input = input()
    split_letter = letter_input.split()
    capilize_letter = split_letter.capitalize()
    return ''.join(capilize_letter)