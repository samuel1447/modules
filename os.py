import os

#os.mkdir('C:/Users/sarah/Desktop/python/c99 modules/module')

x=os.getcwd()

print('this is the current folder' +x)

y=os.path.exists('C:/Users/sarah/Desktop/python/c99 modules/module')

print(y)

z=os.path.splitext('C:/Users/sarah/Desktop/python/c99 modules/os.py')

print(z)

print(z[0])

red=os.listdir('C:/Users/sarah/Desktop/python')

print(red)