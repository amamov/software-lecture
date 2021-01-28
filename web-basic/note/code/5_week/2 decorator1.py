def decorator(func):
    def inner():
        print("This is emoticon")
        func()

    return inner


if __name__ == "__main__":

    def smile():
        print("^_^")

    smile = decorator(smile)
    smile()

    @decorator
    def confused():
        print("@_@")

    confused()
