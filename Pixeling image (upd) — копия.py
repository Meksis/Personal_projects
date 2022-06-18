import numpy as np
from PIL import Image
alph={0:0, 1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:'a', 11:'b', 12:'c', 13:'d', 14:'e', 15:'f'}

name = 'test_3'
format_ = "bmp"

com_use = False

com_port = 3


path=f'J:/Пикчи и видосеки/Пикчи/Разбивка/{format_}/{name}.{format_}'
arr = np.asarray(Image.open(path), dtype='int').tolist()

com_port='COM'+str(com_port)

width=12
height=12
square=width*height
numbers_list = []
counter = 1
step_counter = 0
pixels = []
mid_list = []
line_counter = 0

for number_counter in range(0, square+1, width):
    if number_counter-width == square - width:
        break
    if counter:
        for back_num in range(number_counter+8, number_counter-1, -1):
            numbers_list.append(back_num)
        counter = 0
    else:
        for face_num in range(number_counter, number_counter+9, 1):
            numbers_list.append(face_num)
        counter = 1

for pixel_line in arr:
    for pixel_point in pixel_line:
        if pixel_point.count(0) < 3 and pixel_point.count(255) < 3:
            pixel_point.insert(0, numbers_list[line_counter])
            pixels.append(pixel_point)
        line_counter+=1

for pixel_color in pixels:
    mid_val = [str(pixel_color[0])]
    for pixel_value in pixel_color[1:]:
        if alph[pixel_value//16] == alph[pixel_value%16]:
            mid_val.append(str(alph[pixel_value//16]))
        else:
            mid_val.append(str(alph[pixel_value//16]) + str(alph[pixel_value%16]))
    one_counter = 0
    for pixel_index, pixel_correct in enumerate(mid_val[1:]):
        if len(pixel_correct) == 1:
            one_counter+=1

    if one_counter == 3 or one_counter == 0:
        pass
    else:
        mid_val = [str(pixel_color[0])]
        for pixel_value in pixel_color[1:]:
            mid_val.append(str(alph[pixel_value//16]) + str(alph[pixel_value%16]))
    mid_val = mid_val[0]+'S'+mid_val[1]+mid_val[2]+mid_val[3]+'P'
    mid_list.append(mid_val)

mid_list = 'Z'+''.join(mid_list)
mid_len = len(mid_list)//2

if len(mid_list) > 350:
    rev = list(mid_list[ : mid_len])
    rev.reverse()
    p_index = rev.index('P')
    rev = mid_list[ : mid_len - p_index]
    rev_2 = 'Z'+mid_list[ mid_len - p_index : ]
    print_lst = [rev, rev_2]
else:
    print_lst = ['1'+mid_list]

print(print_lst)

if com_use==1:
    import serial
    ser = serial.Serial(com_port, 115200, bytesize=8, parity='N', stopbits=1)
    serread=ser.readline()

    while serread!=b'R\r\n':
        serread=ser.readline()
        print(serread)

    print('Arduino ready')
    ser.write(('b50'.encode()))
    while serread!=b'g\r\n':
        serread=ser.readline()
    print('brightness changed')
    for counter, piece in enumerate(print_lst, start = 1):

        ser.write((piece.encode()))
        while serread!=b'g\r\n':
            serread=ser.readline()
        print(f'Transfered {counter} part')
    print('Transfering completed')
    ser.close()