morse_code = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.',
    ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-',
    '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'
        }

def text_to_morse(text):
    morse = []
    for char in text.upper():
        if char == " ":
            morse.append(" ")
        else:
            if char in morse_code:
                morse.append(morse_code[char])
    return morse

def morse_to_text(morse = []):
    text = []
    for code in morse:
        if code == " ":
            text.append(" ")
        else:
            for char, morse_char in morse_code.items():
                if code == morse_char:
                    text.append(char)
    return ' '.join(text)

def text_to_morseV2(text):
    morse = []
    for char in text:
        if char == " ":
            morse.append(" ")
        else:
            if char.upper() in morse_code:
                morse.append(morse_code[char.upper()])
    return ','.join(morse)

def morse_to_textV2(morse):
    text = []
    morse = morse.split(',')
    for code in morse:
        if code == " ":
            text.append(" ")
        else:
            for char, morse_char in morse_code.items():
                if code == morse_char:
                    text.append(char)
    return ''.join(text)


morse = text_to_morseV2( str( input("Informe o texto para gerar morse:\n") ))
print(morse)

morseDecodificado = morse_to_textV2(str( input("Informe o código morse para decodificar:\n") ))

print( morseDecodificado)