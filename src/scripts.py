import random
import re
# import operator
def throw_dice(list, throws, dice_size):
    for i in range(throws):
        list.append(random.randint(1,dice_size))
    return list

def TFTL_throw(command):
    string_result = ''
    split_throws = re.split("[tT]", command)

    if split_throws[0] != '':
        res = throw_dice([], int(split_throws[0]), 6)
    else:
        res = throw_dice([], int(split_throws[1]), 6)

    for i in res:
        string_result += str(i) + "+"

    string_result = string_result[:-1]
    return "Wynik: " + string_result + " Sukcesów: " + str(res.count(6))

def standard_throw(command):
    # ops = {"+": operator.add,   #dictionary for operators
    #        "*": operator.mul}

    # signs = re.findall("[+*]",command)  #finding all operators
    sum = 0
    string_result = ''  # string fo throw results
    result = []  # result values list
    split_throws = re.split("[+*]", command)  # separated throws: 3k6 2k4

    for i in split_throws:
        if re.search("[kdKD]", i):
            throw = re.split("[kdKD]", i)  # splitting throw to number of throws and dice
            if throw[0] != '':
                res = throw_dice([], int(throw[0]), int(throw[1]))
                result.append(res)
            else:
                res = throw_dice([], 1, int(throw[1]))
                result.append(res)
        else:
            temp = []
            temp.append(int(i))
            result.append(temp)

    for i in result:
        for j in i:
            string_result += str(j) + '+'
            sum += j

    string_result = string_result[:-1]
    return string_result + " Razem: " + str(sum)

def check_command(command):

    if re.findall("[^kKdDtT1-9+]", command):
        return "Błąd w równaniu rzutu!"
    else:
        if re.findall("[tT]", command):
            if re.findall("[^tT1-9]", command):
                return "Mieszane komendy rzutu! Proszę wpisać ponownie!"
            else:
                return TFTL_throw(command)
        else:
            if re.findall("[^kKdD1-9+]", command):
                return "Mieszane komendy rzutu! Proszę wpisać ponownie!"
            else:
                return standard_throw(command)






# txt = "t7"
# print(check_command(txt))
