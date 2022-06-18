import numpy as np
from PIL import Image
import os
import serial
import time


alph={0:0, 1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:'a', 11:'b', 12:'c', 13:'d', 14:'e', 15:'f'}

path='J:/Пикчи и видосеки/Пикчи/Разбивка/'
name='pokeball'+'.jpg'
file=os.path.join(path, name)
log_img=os.path.join(path, 'IMAGES.txt')
img = Image.open(file)
arr = np.asarray(img, dtype='int')
out=[]
mid=[]
pixels=[]
white=[255,255,255]
com_use=0

for num in arr:
    for subject in num:
        for essence in subject:

            pixels.append(essence)

triple=[]
string_=[]
nines=[]
prev=0
nums=[]
middle=[]
x=0

for i in range(0,81,9):
    if x==1:

        for u in reversed(range(prev,i)):
            middle.append(u)
        x=0

    else:
        for u in range(prev,i):

            middle.append(u)
        x=1

    prev=i
    nums.append(middle)
    middle=[]

for i in reversed(range(72,81)):

    middle.append(i)

nums.append(middle)
nums.pop(0)
middle=[]

prev=0
for i in range(3, 243,3):
    for t in range(prev, i):
        triple.append(pixels[t])

    if triple==white:

        triple=[0,0,0]

    prev=i
    string_.append(triple)
    triple=[]

for i in range(239, 243):

    triple.append(pixels[i])

string_.append(triple)
triple=[]
midles=[]
prev=0
lmao=[]

for i in string_:
    for o in i:

        lmao.append(o)
lmao.pop(-4)
#arr_=np.array(lmao, ndmin=1).reshape(9, 27)

for counter_ in range(9, 81,9):
    for u in range(prev, counter_):

        midles.append(string_[u])

    prev=counter_
    nines.append(midles)
    midles=[]
middle=string_[80][1:]
string_.pop(80), string_.append(middle)

for i in range(72,81):

    midles.append(string_[i])

nines.append(midles)
midles=[]
out=[]

for counter_1, strings in enumerate(nines): # Strings
    for counter_2, pixelz in enumerate(strings):

        num=nums[counter_1][counter_2]
        pixelz.insert(0, num)
        out.append(pixelz)

for counter, t in enumerate(out):
    if t.count(0)==3:

        out.insert(counter, 999)
        out.pop(counter+1)

out=list(out)

while out.count(999)>0:

    out.remove(999)

print(len(out))

out_copy=out.copy()
out_str=str(out)
out_fin=''

for counter, i in enumerate(out_str):
    if i=='[':

        out_fin+='{'
    elif i==']':

        out_fin+='}'
    elif i==',':

        if out_str[counter-1]==']' and out_str[counter+2]=='[':

            out_fin+='A,'
        else:

            out_fin+=i
    elif i==' ':

        pass
    else:

        out_fin+=i

out_list=list(out_fin)

while out_list.count('A')>0:
    out_list.remove('A')
out_fin=''.join(out_list)

#print(out_fin)
#log=open(log_img, 'a')
#log.write(f'{name}\n{out_fin}\n---------------\n')
#log.close()

x=0
remainder=[]
outs=[]
hex_pixels=[]
out=''
print(out_fin)

print(out_copy)
for i in out_copy:
    counter=0
    miss_zero=1
    miss_max=1
    for num in i:
        if counter==0:

            pix_num=num

        else:
            if num == 0:
                if miss_zero==3:

                    print(pix_num, num, outs, 'popping\n')
                    outs.clear()
                    miss_zero=1

                else:
                    miss_zero+=1
                    outs.append('00')

            elif num==255:
                if miss_max==3:

                    print(pix_num, num, outs, 'popping\n')
                    outs.clear()
                    miss_max=1
                else:

                    miss_max+=1
                    outs.append('ff')
            else:

                quotient=num

                while quotient!=0:

                    remainder.append(alph[num%16])
                    num=num//16
                    quotient=num

                remainder.reverse()

                for i in remainder:

                    out+=str(i)
                if len(out)<2:

                    out_temp=out
                    out='0'+out_temp

                outs.append(out)
                out=''
                remainder.clear()

        counter+=1

    if len(outs)!=0:

        out=str(pix_num)+'S'
        for i in outs:
            out+=i
        hex_pixels.append(out)
        out=''
        outs.clear()
        #print('\n')

outs=''

for num in hex_pixels:
    outs+=num+'P'

print(outs)



if com_use == 1:
    ser = serial.Serial('COM27', 9600, bytesize=8, parity='N', stopbits=1)
    if x==0:

        time.sleep(4)
        print('connected')
        ser.write((outs.encode()))
        print(outs)
        x+=1
    else:

        serread=ser.readline()

        while serread!=b'g\r\n':

            serread=ser.readline()
    #print(num)
        #print(outs)
        ser.write((outs.encode()))
        ser.reset_output_buffer()
        ser.reset_input_buffer()
#ser.write(outs.encode())
#while ser.readline()!=b'g\r\n':
    #print(ser.readline())
    ser.close()
