import numpy as np
from PIL import Image
import os
import serial
import time

alph={0:0, 1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:'a', 11:'b', 12:'c', 13:'d', 14:'e', 15:'f'}

width=9
height=9
square=width*height

com_use=0

com_port=53


com_port='COM'+str(com_port)

path='J:/Пикчи и видосеки/Пикчи/Разбивка/bmp'
name='skull'+'.bmp'
file=os.path.join(path, name)
log_img=os.path.join(path, 'IMAGES.txt')
img = Image.open(file)
arr = np.asarray(img, dtype='int')

prev=0
x=1
y=0
value=0
white_miss=0
zero_miss=0
prev=0

hex_value=''
hex_value_end=''
pixels=[]
middle=[]
num_order=[[]]
normalized_pixels=[]
prepairing_list=[]
hex_pixels=[]
remainder=[]

for num in arr:
    for subject in num:
        for essence in subject:

            pixels.append(essence)

for i in range(0, square+1, width):
    if y==0:
        for num in range(prev, i+1):

            middle.append(num)
        prev=i
        x=0
        y=1
    else:
        if x==1:
            for num in range(prev, i):

                middle.append(num)
            prev=i
            x=0
        else:
            for num in reversed(range(prev, i)):
                middle.append(num)
            prev=i
            x=1
        num_order+=middle
        middle.clear()
num_order.pop(0), num_order.pop(0)

for num_order_iterator, value in enumerate(range(3, len(pixels), 3)):
    for num in range(prev, value):
        pixel_value=pixels[num]
        prepairing_list.append(pixel_value)
        if pixel_value==255:
            white_miss+=1
        elif pixel_value==0:
            zero_miss+=1
    prev=value
    if white_miss==3 or zero_miss==3:
        prepairing_list.clear()
    else:
        prepairing_list.insert(0, num_order[num_order_iterator])
        prepairing_list_copy=prepairing_list.copy()
        normalized_pixels.append(prepairing_list_copy)
        prepairing_list.clear()
    zero_miss=0
    white_miss=0


for value_list in normalized_pixels:
    for counter,value in enumerate(value_list):
        if counter%4==0:
            hex_value_end=str(value)+'S'
        else:
            if value!=0:
                quotient=value
                while quotient!=0:
                    remainder.append(alph[value%16])
                    value=value//16
                    quotient=value
                remainder.reverse()
                for adding in remainder:
                    hex_value+=str(adding)
                remainder.clear()

            else:
                hex_value+='00'
            if len(hex_value)<2:
                hex_temp=hex_value
                hex_value='0'+hex_temp
        hex_value_end+=hex_value
        hex_value=''
    hex_pixels.append(hex_value_end+'P')
    hex_value=''
    hex_value_end=''

hex_out=''
for hex_append in hex_pixels:
    hex_out+=hex_append
print(hex_out)

if com_use==1:
    ser = serial.Serial(com_port, 9600, bytesize=8, parity='N', stopbits=1)
    serread=ser.readline()
    while serread!=b'R\r\n':
        serread=ser.readline()

    print('Arduino ready, transfering data')
    ser.write((hex_out.encode()))
    while serread!=b'g\r\n':
        serread=ser.readline()
    print('transfering completed')
    #ser.reset_output_buffer()
    #ser.reset_input_buffer()
    ser.close()
