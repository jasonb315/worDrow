# imports
# from textwrap import dedent
# import sys
import uuid


# take_input -> generate_lampe_cube -> take_input


class Lampecube:
    def __init__(self):
        self.cube = ''
        self.input_str = ''
        self.id = str(uuid.uuid4())


def generate_lampe_cube(input_str, input_offset, input_interval):
    # check for quit or about
    # should genetate the cube, print it, ask save, then call take input.

    temp_cube = Lampecube()
    temp_cube.input_str = input_str
    symbols = ''

    for word in (input_str.split()):
        for symbol in word:
            symbols += symbol
            symbols += ' '

    output = ''
    return_string = ''
    lines = 0
    # break the sentence into word strings

    # mutate and set initial str with UTF offset
    for word in symbols:
        for letter in word:
            output += (chr(ord(letter)+int(input_offset)))
            lines += 1
        output += ' '
    return_string += output + '\n'

    symbols = output.split()
    output = ''

    # lines after the first with sequential
    for k in range(lines - 1):
        for word in symbols:
            for letter in word:
                output += (chr(ord(letter)+int(input_interval)))
            output += ' '

        return_string += output + "\n"
        symbols = output.split()
        output = ''


    print(return_string)



def save_cube():
    #to fs
    pass


def take_input():

    #check for quit or about

    input_str = input(f'''input a string to lampe-cube.
    May include any UTF-8 characters.
    TIP: adjacently encoded characters in series will produce visual text-rivers.
    ex : abc, 123. >>   ''')

    input_offset = input(f'''input UTF-8 offset.
    This will incriment the UTF-8 code of ALL characters of the string by the given ammount.
    Negitive numbers accepted. >>   ''')

    input_interval = input(f'''input UTF-8 interval.
    This will incriment the UTF-8 code of EACH character of the string by the given ammount.
    Negitive numbers accepted. >>   ''')

    return generate_lampe_cube(input_str, input_offset, input_interval)


if __name__ == '__main__':
    '''
    run : core
    keu exit : polite
    '''
    try:
        print('LAMPE CUBE :D')
        take_input()
    except KeyboardInterrupt:
        exit()

# def letterBlock(phrase, offset, interval):
#     sentence = phrase
#     symbols = sentence.split()
#     output = ''
#     lettercount = 0
#     returnString = ''

#   for word in words:
#     for letter in word:
#       lettercount += 1
#       output += (chr(ord(letter)+offset))
#     output += ' '

#   returnString += output + "\n"
#   sentence = output
#   words = sentence.split()
#   output = ''

#   for k in range(51):
#     for word in words:
#       for letter in word:
#         output += (chr(ord(letter)+interval))
#       output += ' '

#     returnString += output + "\n"
#     sentence = output
#     words = sentence.split()
#     output = ''

#   return returnString

# # print(letterBlock("J A S O N", 0, 1))
# # letterBlock("B U R N S", 0, 1)
# # letterBlock("0 1 2 3 4 5 6 7 8 9", 1, -1)
# print(letterBlock("A B C D E F G H I J K L M N O P Q R S T U V W X Y Z Y X W V U T S R Q P O N M L K J I H G F E D C B A", -10, 1))
# # letterBlock("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG", 0, -1)
# # undo = output.split()
# # undoprint = ''
# print(len("A B C D E F G H I J K L M N O P Q R S T U V W X Y Z Y X W V U T S R Q P O N M L K J I H G F E D C B A"))
# # for letter in undo:
# #   undoprint += ' '
# #   for x in letter:
# #     undoprint += (chr(ord(x)-1111))

# # print(undoprint)

# # def break_line():
# #   return "line\nbreak"
# # print(break_line())

