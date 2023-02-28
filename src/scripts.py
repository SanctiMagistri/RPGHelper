import random
import re
import operator
def throw_dice(list, throws, dice_size):
    for i in range(throws):
        list.append(random.randint(1,dice_size))
    return list

def check_command(command):
    ops = {"+": operator.add,}
    sum = 0
    string_result = ''
    result = []
    signs = re.findall("[+*]",command)
    split_throws = re.split("[+*]", command)

    for i in split_throws:
        if re.search("[kd]",i):
            throw = re.split("[kd]", i)
            if throw[0] != '':
                result.append(throw_dice([],int(throw[0]),int(throw[1])))
            else:
                result.append(throw_dice([],1, int(throw[1])))
        else:
            temp = []
            temp.append(int(i))
            result.append(temp)

    for i in result:
        for j in i:
            string_result += str(j) + '+'
            sum += j
    string_result = string_result[:-1]

"""
DODAĆ OBSŁUGĘ MNOZENIA RZUTÓW
DODAĆ RETURN WIADOMOŚCI
DODAĆ KOMENTARZE
"""



txt = "1d8+2k6+k12+k100"
check_command(txt)
