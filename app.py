# import re
# phoneNumRegex = re.compile(r'\d\d-\d\d\d\d-\d\d\d\d')
# result = phoneNumRegex.findall('Please call David at 02-8888-1688 by today. 02-9888-9898 is his office number.')

# print(result)

# # number = ', '.join(result)
# print('Phone Number: ' + str(result))
# print('Please call him/her as soon as possible.')


# def dot_stright(x0,y0,x1,y1):
#     distence_x = abs(x0 - x1)
#     distence_y = abs(y0 - y1)
#     distence00 = (distence_x ** 2 + distence_y ** 2) ** 0.5
#     print(distence00)

# X0 , X1 = int(input('x0 = ')) , int(input('x1 = '))
# Y0 , Y1 = int(input('y0 = ')) , int(input('y1 = '))
# dot_stright(X0,X1,Y0,Y1)

# arrays = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# for quantity_arr in arrays:
#     for quantity in quantity_arr:
#         print(quantity)

# print(arrays[0][0])

try:
    num = int(input("the num: ") )
    print(num)
except:
    print('not integer')
else:
    print("it's integer")