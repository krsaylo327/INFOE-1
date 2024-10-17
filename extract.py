import numpy as np
import PIL.Image

image = PIL.Image.open("hidden.png", "r") #opens img in reading mode
image_array = np.array(list(image.getdata())) #converts image to array

channels = 4 if image.mode == 'RGBA' else 3 #if image is RGBA, channels = 4, else channels = 3

pixels = image_array.size // channels #total number of pixels in image

secret_bits = [bin(image_array[i][j])[-1] for i in range(pixels) for j in range(0,3)] #extracting the last bit of each pixel
secret_bits = ''.join(secret_bits) #joining all the bits together
secret_bits = [secret_bits[i:i+8] for i in range(0, len(secret_bits), 8)] #grouping 8 bits together

#print(secret_bits) - prints the secret bits, if you want to see them

secret_message = [chr(int(secret_bits[i], 2)) for i in range(len(secret_bits))] #converting the bits to characters
secret_message = ''.join(secret_message) #joining the characters together

stop_indicator = "$Neural$" #stop indicator to know when to stop extracting the message

if stop_indicator in secret_message: #if the stop indicator is in the message
    print(secret_message[:secret_message.index(stop_indicator)]) #print the message up to the stop indicator
else:
    print("No hidden message found") #if the stop indicator is not in the message, print this