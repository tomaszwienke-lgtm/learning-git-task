def is_palindrome(text):
    znaki = []
    for znak in text:
        if znak.isalnum():
            znaki.append(znak.lower())
    return znaki == znaki[::-1]

# Testy z zadania
if __name__ == "__main__":
    print(is_palindrome("kajak"))   # True
    print(is_palindrome("potop"))   # True
    print(is_palindrome("python"))  # False
