#translate every vowel to X
def translate (phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou": #en lugar de poner leter in "AEIOUaeiou"
            if letter.isupper():
                translation = translation + "X"
            else:
                translation = translation + "x"
        else:
            translation = translation + letter

    return translation

print(translate(input("Enter a phase:")))