def capital_letters():
<<<<<<< HEAD
    """Делает загланые все буквы каждого каждого слова в строке"""
    str_input = input()
    return str_input.upper()

def capitalized_first_letter():
    """Делает заглавные первые буквы каждого слова в строке"""
    letter_input = input()
    split_letter = letter_input.split()
    capilize_letter = split_letter.capitalize()
    return ''.join(capilize_letter)
=======
    """Принимает на вход строку и возвращает её со всеми заглавными буквами"""
    str_input = input()
    return str_input.upper()
>>>>>>> develop
