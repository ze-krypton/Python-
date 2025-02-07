alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from logo import logo
print(logo)
should_continue=True
    
def ceaser(original_text,shift_number,encode_or_decode):
    cipher_text=""
    if encode_or_decode=="decode":
        shift_number*=-1
    for letters in original_text:
        if letters not in alphabet:
            cipher_text+=letters
        else:
            shifted=alphabet.index(letters)+shift_number
            shifted%=len(alphabet)
            cipher_text+=alphabet[shifted]
    print(f"your {encode_or_decode}d text: {cipher_text}")
        
    
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    ceaser(original_text=text,shift_number=shift,encode_or_decode=direction)
    restart=input("Type \'yes\' to continue or \'no\' to exit :")
    
    if restart=='yes':
        should_continue=True
    elif restart=='no':
        should_continue=False
    
            
    