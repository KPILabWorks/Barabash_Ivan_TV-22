from collections import Counter

def char_count(s: str) -> dict:
    return dict(Counter(s))


print(char_count(input("Enter phrase\n")))
