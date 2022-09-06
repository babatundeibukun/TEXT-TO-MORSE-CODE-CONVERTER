# def morse_to_english(morse_codes):
#     for i in
#
#
# morse_eng_dict = {".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E",
#                   "..-.": "F", "--.": "G", "....": "H",
#                   "..": "I", ".---": "J", "-.-": "K", ".-..": "L",
#                   "--": "M", "-.": "N", "---": "O", ".--.": "P",
#                   "--.-": "Q", ".-.": "R", "...": "S", "-": "T", "..-": "U", "...-": "V",
#                   ".--": "W", "-..-": "X", "-.--": "Y", "--..": "Z"}


def to_morse_code(text):
    codes = {
        "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....",
        "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-",
        "R": ".-.",
        "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..", " ": " "
    }

    morse_code = ""

    for i in text:
        morse_code += codes[i.upper()]

    return morse_code


text = input('Enter your english words to convert to morse:')
print(to_morse_code(text))
