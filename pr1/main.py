# Написати функцію, яка приймає рядок і повертає словник, де ключі — це унікальні символи, а значення — кількість їх входжень

from collections import Counter

print(dict(Counter(input("Enter phrase\n"))))
