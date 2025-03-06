# Написати функцію, яка приймає рядок і повертає словник, де ключі — це унікальні символи, а значення — кількість їх входжень

from collections import Counter

def char_count(s: str) -> dict:
    return dict(Counter(s))


print(char_count(input("Enter phrase\n")))
