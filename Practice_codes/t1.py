alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
text=input("Enter a text: ")
shift=int(input("Enter the shift: "))
def encrypt(o_text,o_shift):
    o_text=o_text.lower()
    cipher=""
    for letter in o_text:
        shifted=alphabet.index(letter)+o_shift
        shifted=shifted%25
        cipher+=alphabet[shifted]
    print(cipher.upper())

encrypt(o_text=text,o_shift=shift)