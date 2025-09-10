#!/usr/bin/python3
def best_score(a_dictionary):
    highScore = 0
    if a_dictionary is not None:
        for key, value in a_dictionary.items():
            if value > highScore:
                highScore = value
        dSwap = {value: key for key, value in a_dictionary.items()}
        for key, value in dSwap.items():
            if key == highScore:
                return value
    else:
        return None
