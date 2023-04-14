def pyramid(text):
    my = 1

    while len(text) > my:
        print(text[0:my:])

        text = text[my::]
        my += 1

text = "abcdefghijklmnopqrstwxyz" * 10

pyramid(text)