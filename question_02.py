###-------------------------------------------###
###---Question 02 -Chapter 1:The Gatekeeper---###
###-------------------------------------------###

import time
current_time = int(time.time())
generated_number = (current_time % 100) + 50

if generated_number % 2 == 0:
    generated_number += 10

print(generated_number)


#import libraries
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg

# first importing image 
image = mpimg.imread('Chapter1.jpg')

# Next convert the image to a NumPy array
# If the image is in range [0, 1] (float), convert to [0, 255] (int). Also pixel values for each color red, green and blue range between 0 and 255.
if image.dtype == np.float32 or image.dtype == np.float64:
    image = (image * 255).astype(np.uint8)

# Add n to each pixel value (r, g, b)
n = generated_number
# Here we use np.clip to make sure the pixel values stay in the range [0, 255]
new_image = np.clip(image + n, 0, 255).astype(np.uint8)

# Sum all red pixel values in the modified image
red_sum = np.sum(new_image[:, :, 0])

# Save the new image using Matplotlib's imsave function
plt.imsave('chapter1out.png', new_image)

# Output the sum of all red values
print(f"Sum red values: {red_sum}")

 
###---------------------------------------------------###
###---Question 02 -Chapter 1:The Chamber of Strings---###
###---------------------------------------------------###

###----part-01----###

def string_convert(s):
    #first convert string into numbers and letters
    number_str = ''.join(char for char in s if char.isdigit())
    letter_str = ''.join(char for char in s if char.isalpha())

    #get the even number & even number ASCII value to lists
    even_num = []
    even_num_ascii = []
    for num in number_str:
        #check whether remainder is 0 to identify even or odd number
        if int(num) % 2 == 0:
            even_num.append(num)
            even_num_ascii.append(ord(num))

    #get the upper-case letters in the letter substring and get their ASCII value to the list
    upper_case_letter = []
    upper_case_letters_ascii = []
    for letter in letter_string:
        # checking selected letter is uppercase letter
        if letter.isupper():
            upper_case_letter.append(letter)
            upper_case_letters_ascii.append(ord(letter))

    return number_str, letter_str,even_num, even_num_ascii,upper_case_letter, upper_case_letters_ascii
