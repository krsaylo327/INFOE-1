import numpy as np
import PIL.Image

message_to_hide = "Heisenberg" #message to hide in the image

image = PIL.Image.open("garbage.png", "r") #opens img in reading mode
width, height = image.size #gets the width and height of the image
img_array = np.array(list(image.getdata())) #converts image to array

if image.mode == "P": #if the image is in palette mode (8-bit) then convert it to RGB mode
    print("not supported")
    exit()

channels = 4 if image.mode == 'RGBA' else 3 #if image is RGBA, channels = 4, else channels = 3

pixels = img_array.size // channels #total number of pixels in image

stop_indicator = "$Neural$" #stop indicator to know when to stop extracting the message
stop_indicator_length = len(stop_indicator) #length of the stop indicator in order to know how many characters to skip

message_to_hide += stop_indicator #add the stop indicator to the message to hide in the image

byte_message = ''.join(f"{ord(c):08b}" for c in message_to_hide) #convert the message to hide to binary
bits = len(byte_message)    #total number of bits in the message

if bits >  pixels:  #if the number of bits in the message is greater than the number of pixels in the image then print this
    print("Message too large to hide in image")
else: #if the number of bits in the message is less than or equal to the number of pixels in the image then hide the message in the image
    index = 0
    for i in range(pixels):
        for j in range(0, 3):
            if index < bits:
                img_array[i][j] = int(bin(img_array[i][j])[2:-1] + byte_message[index], 2)
                index += 1

img_array = img_array.reshape(height, width, channels) #reshape the image array to the original image shape

result_image = PIL.Image.fromarray(img_array.astype(np.uint8)) #convert the image array to an image
result_image.save("hidden.png") #save the image with the hidden message