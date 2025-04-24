'''
  86) Create a program that has a procedure called Generator() that, when called, 
     displays the message "Hello, World!" with some visual components (lines).
     Example: When calling Generator(), it should display:

     +-------=======------+
       Hello, World !
     +-------=======------+
'''

def generator():
    line = '+-------=======------+'
    print(line)
    print('  Hello, World !')
    print(line)

generator()


input("Press Enter to exit ... ")