###-------------------------------------------###
###---Question 02 -Chapter 1:The Gatekeeper---###
###-------------------------------------------###

###---------Part 1 - getting the key----------###

total = 0
# Fixing the outer for loop
for i in range(5):
    for j in range(3):
        # Adjusting the condition and calculation
        if i + j == 5:
            total += i + j
        else:
            total -= i - j

print(total)

counter = 0
# Fixing the while loop condition by removing 'else'. Cause from that given code has a infinite loop
while counter <= 5:
    if total <= 13:
        total += 1
    elif total > 13:
        total -= 1
        counter +=1
        

#find the key
print("Key:", total)
#as per above code key is 13

###---------Part 2 - decrypyion function----------###

def decrypt(encrypted_text, key):
    decrypt_code = ""
    
    for char in encrypted_text:
        if char.isalpha():  # Checking whether if the character is a letter
            shifted = ord(char) - key  # Shift the character backwards by the key
            
            if char.islower():  # to handle lowercase letters
                if shifted < ord('a'):  # if 'shifted' less than 'a' then 'shifted + 26'
                    shifted += 26
            elif char.isupper():  # to handle uppercase letters
                if shifted < ord('A'):  # if 'shifted' less than 'a' then 'shifted + 26'
                    shifted += 26
            
            decrypt_code += chr(shifted)
        else:
            # If it's not an alphabetical character, no change
            decrypt_code += char

    return decrypt_code


