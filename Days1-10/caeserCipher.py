class Cypher():
    def __init__(self):
        self.alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    def encrypt(self, text, shift):
        encryptedText = []
        for char in text:
            index = self.alphabet.index(char)
            newIndex = index + shift
            if newIndex > 25:
                newIndex = newIndex - 26
            encryptedText.append(self.alphabet[newIndex])
        print(''.join(encryptedText))
    def decrypt(self, text, shift):
        decryptedText = []
        for char in text:
            index = self.alphabet.index(char)
            newIndex = index - shift
            if newIndex < 0:
                newIndex = newIndex + 26
            decryptedText.append(self.alphabet[newIndex])
        print(''.join(decryptedText))
    
def main():
    cipher = Cypher()
    direction = input('Type "encode" to encrypt, type "decode" to decrypt: ').lower()
    text = input('Type your message: ').lower()
    shift = int(input('Type the shift number: '))
    if direction == 'encode':
        cipher.encrypt(text, shift)
    elif direction == 'decode':
        cipher.decrypt(text, shift)
    else:
        print('Invalid input. Please try again')
        main()
    again = input('Would you like to go again? Type "yes" or "no": ').lower()
    if again == 'yes' or again == 'y':
        main()
    else:
        quit()
if __name__ == "__main__":  
    main()

    