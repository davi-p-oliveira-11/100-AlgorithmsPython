'''
   87) Create a program that improves the Generator() procedure from the previous question 
      so that it displays a custom message passed as a parameter.
      Example: When calling Generator("Learning Python"), it should display:

      +-------=======------+
       Learning Python
      +-------=======------+
'''

def generator(message: str) -> None:
    line = '+-------=======------+'
    print(line)
    print(f'  {message}')
    print(line)

generator('Learning Python')

input("Press Enter to exit ... ")
