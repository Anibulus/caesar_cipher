import regex

DISPLACE : int = 3
ABCEDARY : list = []

"""_summary_
Build dinamicly the abcdary
"""
def build_abecedary():
    start : int = ord("A")
    end : int = ord("Z") + 1
    for i in range(start, end):
        ABCEDARY.append(chr(i))

"""_summary_
Based on the action 'code' or 'decode', this method will set the direction of the movement
"""
def set_movement(action: str) -> int:
    if (action == 'code'):
        movement = 1
    else :
        movement = -1
    return movement
 

"""_summary_
Main process to code or decode a message
""" 
def encode(text: str, action: str) -> str:
    text = text.upper()
    result : str = ""
    movement : int = set_movement(action)

    for character in text:
        if(regex.match("\s",character)): # If catch an space of any kind, skip
            result = result + character
            continue
        
        index = ABCEDARY.index(character)
        index = (DISPLACE * movement) + index
        if (index > len(ABCEDARY)-1): #Restart position if exceds th bound if the list
            index = index - (len(ABCEDARY))

        result = result + ABCEDARY[index]
    return result

