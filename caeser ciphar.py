import art
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caeser(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
            shift_amount *= -1
    for letter in original_text:
       if letter not in alphabet:
            output_text += letter
       else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")

continue_result = True
while continue_result:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()    
    shift = int(input("Type the shift number:\n"))
    caeser(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input("Type 'yes' to do it again or type 'no' to finish it:\n")
    if restart == "no":
         continue_result = False
         print("Goodbye!!")
  
                  
