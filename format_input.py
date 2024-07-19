from tkinter import Tk
import const

def char_checker(pInput):
    """Returns a list if illegal characters are used, returns True if the string is OK."""
    illegalList = []
    for char in pInput:
        if (char not in const.CHARS) and (char not in illegalList) and (char != " "):
            illegalList.append(char)
    return illegalList
    
def len_checker(pInput):
    total = 0
    for i in pInput:        
        if i == " ":
            total+=1
        else:
            with open(f'{const.CHARDIR}\\{i}.char', 'r') as reader:
                pLength = len(reader.readline().strip())
                total += pLength + 1
    total -= 1 # accounts for the extra space in the end
    if total <= const.MAX_LINE_LENGTH: 
        return total, True
    return total, False

def input_format(pInput, pLength):
    # center allign measurements
    x_pad = (const.MAX_LINE_LENGTH - pLength) //2
    r = (const.MAX_LINE_LENGTH - pLength) %2
    if r == 0: left_pad, right_pad = x_pad, x_pad
    elif r == 1: left_pad, right_pad = x_pad, x_pad+1

    final_ascii = ""

    for x in range(const.MAX_LINES):
        line = ""
        if x == 0 or x == const.MAX_LINE_LENGTH-1:
            final_ascii+='#'*const.MAX_LINE_LENGTH
        else:
            final_ascii+='#'*left_pad
            j=0
            for i in pInput:
                j+=1
                if i != " ":
                    with open(f'{const.CHARDIR}\\{i}.char', 'r') as reader:
                        lines = reader.readlines()
                    line = lines[x].replace(' ','#').strip('\n')
                    while len(lines[0]) > len(line)+1:
                        line+='#'

                    final_ascii+=line
                if j != len(pInput):
                    final_ascii+='#'
            final_ascii+='#'*right_pad

    return final_ascii.replace('#',const.TXT_SPACE).replace('a',const.TXT_FILL)

def ascii_formatter(user_input):

    if user_input == "":
        return 'Enter text above to translate into ASCII text!'

    user_input = (str(user_input)).upper() # temporary until lowercase letters are added

    # check if character has format file
    invalid_chars = char_checker(user_input)
    if invalid_chars:
        text = f"There is currently no support for these characters: "
        for char in invalid_chars:
            text += f"{char} "
        return text

    # check if the thing will fit in the chatbox even
    length, valid = len_checker(user_input)

    if not valid:
        return f"Length would be too long!"
    
    # format the message and return to main
    final_result = input_format(user_input, length)
    
    # copy to clipboard
    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(final_result)
    r.update() # now it stays on the clipboard after the window is closed
    r.destroy()

    return final_result.replace(const.TXT_SPACE,'.')#.replace(const.TXT_FILL,'#')
