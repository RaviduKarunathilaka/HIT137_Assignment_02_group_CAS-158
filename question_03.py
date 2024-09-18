###-------------------------------------------###
###--------------Question 03------------------###
###-------------------------------------------###

###---------Part 1 - getting the key----------###
print("tesssssssssssssssssssssssssssst")
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

def decrypt(encrypted_text, key =13):
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

encrypted_text ="""
tybony_inevnoyr = 100
zl_qvpg {'xr11': 'inyhr1', 'xr12': 'inyhr2', 'xr13': 'inyhr3']
qrs cebprff_ahzoref():
tybony tybony_inevnoyr ybpny inevnoyr
5
ahzoref [1, 2, 3, 4, 5]
juvyr ybpny inevnoyr > 0:
vs ybpny inevnoyr % 2 == 0:
ahzoref.erzbir(ybpny_inevnoyr)
ybpny inevnoyr - 1
erghea ahzoref
zl_frg (1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
erfhyg
cebprff_ahzoref (ahzoref=zl_frg)
qrs zbqvsl_qvpg():
ybpny inevnoyr
10
zl qvpg['xr14'] = ybpny_inevnoyr
zbqvs1_qvpg(5)
qrs hcqngr_tybony():
tybony tybony_inevnoyr
tybony inevnoyr + 10
sbe v va enatr(5):
cevag(v)
V+ 1
vs z1_frg vf abg Abar naq zl_qvpg['xr14'] == 10: cevag("Pbaqvgvba zrg!")
vs 5 abg va z1_qvpg:
cevag("s abg sbhaq va gur qvpgvbanel!")
cevag(tybony_inevnoyr)
cevag(z1_qvpg) cevag(z1_frg) """

print(decrypt(encrypted_text, key =13))


###---------Part 3 - correct the encrypting code----------###

global_variable = 100

#dictionary ending bracket was wrong before. and equal sign was missing before
my_dict = {'ke11': 'value1', 'ke12': 'value2', 'ke13': 'value3'}

# here after 'numbers' variable equal mark was missing before
# this should passed inside the function previously. now its passing from outside the function
numbers = [1, 2, 3, 4, 5]

# 'numbers' paramter in the function was missing before
def process_numbers(numbers):
    # equal sign was missng before
    global global_variable 
    # didnt started from a new line before
    local_variable =5

    while local_variable > 0:
        if local_variable % 2 == 0:
            numbers.remove(local_variable)
        # equal sign missing before. therefore this has been a infinite loop before
        local_variable -= 1
    return numbers


#starting bracket was wrong before
my_set = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
# here after 'result' variable equal mark was missing before
result = process_numbers (numbers=my_set)
print(result)


def modify_dict(n):
    #'local_variable' name was wrong before
    local_variable = 10
    # "_" was missing before
    my_dict[n] = local_variable

#function name was incorrect before    
print(modify_dict(5))


def update_global():
    global global_variable
    #"_" missing before amd "=" was missing before
    global_variable += 10
    for i in range(5):
        print(i)
        # previously uppercase letter was metioned below (I for i)
        i+ 1
        # 'my_set' name was incorrect before / ke14 was wrong before
        if my_set is not None and my_dict['ke13'] == 10: 
            print("Condition met!")
        # 'my_dict' name was incorrect before
        if 5 not in my_dict:
            print("f not found in the dictionary!")
    print(global_variable)
    #comma was missing before and 'my_dict,'my_set' names were incorrect before
    print(my_dict)
    print(my_set)

