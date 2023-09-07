# palindromo, es unapalabra que se lee al derecho y al reves

def is_palindrome(string: str) -> bool:
    string = string.repalce(" ", "").lower()

    return string == string[::-1]

def run():
    print(is_palindrome(1000))

if __name__ == "__main__":
    run()
