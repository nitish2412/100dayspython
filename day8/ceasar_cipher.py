import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def isNumber(s):
 
    for i in range(len(s)):
        if s[i].isdigit() != True:
            return False
 
    return True

def ceasar2(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
  print(f"Here's the {cipher_direction}d result: {end_text}")

def ceasar(text,shift,direction):
  new_text =""
  new_position=0
  for char in text:
    if char not in alphabet:
        new_text+=char
        continue
    position= alphabet.index(char)
    if direction =='encode':
      new_position=position+shift
      if new_position>= 25:
        new_position-=26
    else:
        new_position=position-shift
    new_text+=alphabet[new_position]
  print(f"The {direction}d text is {new_text}")



logo = art.logo
print(logo)

end_ceasar=True
while(end_ceasar):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction!='encode' and direction!='decode':
        print("Please provide a valid choice:")
        continue
    text = input("Type your message:\n").lower()
    shift = input("Type the shift number:\n")
    if isNumber(shift):
             shift=int(shift)
    else:
        print("Please provide a valid shift number:")
        continue
    
    shift=shift%26

    ceasar(text,shift,direction)
    choice=input("Type 'yes' if you want to go again. Otherwise type 'no'")
    if choice == 'no':
        end_ceasar=False
        print("GoodBye!!!!!!!!!!!!!")

