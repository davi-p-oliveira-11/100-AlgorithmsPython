'''
   88) Create a program that improves the Generator() procedure from the previous question 
      so that it displays a message multiple times.
      Example: When calling Generator("Learning Python", 4), it should display:
'''

def generator(message: str, repetitions: int) -> None:
    line = '+-------=======------+'
    for _ in range(repetitions):
        print(line)
        print(f'  {message}')
        print(line)

generator('Learning TypeScript', 4)


input("Press Enter to exit ... ")