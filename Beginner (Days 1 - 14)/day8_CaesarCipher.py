alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encrypt(original, shift):
    encrypted = ""
    for char in original:
        if char not in alphabet:
            encrypted += char
        else:
            newIndex = alphabet.index(char) + shift
            newIndex %= len(alphabet)
            encrypted += alphabet[newIndex]
    print(f"Here is the encoded text: {encrypted}")

def decrypt(encrypted, shift):
    decrypted = ""
    for char in encrypted:
        if char not in alphabet:
            decrypted += char
        else:
            newIndex = alphabet.index(char) - shift
            newIndex %= len(alphabet)
            decrypted += alphabet[newIndex]
    print(f"Here is the decoded text: {decrypted}")

def caesar(direction,text,shift):
    if direction == "encode":
        encrypt(text, shift)
    else:
        decrypt(text, shift)


decision = "yes"
while decision == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction,text,shift)
    decision = input("Type 'yes' if you would like to continue, otherwise type 'no'.\n")