'''
   89) Create a program that improves the Generator() procedure from the previous question 
      so that the programmer can choose one of three borders:

      +-------=======------+  Border 1  
      ~~~~~~~~:::::::~~~~~~~  Border 2  
      <<<<<<<<------->>>>>>>  Border 3  

      Example: A valid function call would be Generator("Python Studio", 3, 2), which should display:

      ~~~~~~~~:::::::~~~~~~~  
      Python Studio
      Python Studio
      Python Studio
      ~~~~~~~~:::::::~~~~~~~  
'''

def generator(message: str, repetitions: int, border_type: int) -> None:
    borders = [
        '+-------=======------+',
        '~~~~~~~~:::::::~~~~~~~',
        '<<<<<<<<------->>>>>>>'
    ]
    
    border = borders[border_type - 1] if 1 <= border_type <= len(borders) else borders[0]

    for _ in range(repetitions):
        print(border)
        print(f'  {message}')
    print(border)

generator('Python Studio', 3, 2)


input("Press Enter to exit ... ")