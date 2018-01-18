def print_list(l, numbered = False, bullet_character='_'):
    """Prints a list on multiple lines, with numbers or bullets

    Arguments:
    l: The list to print
    numbered: set to True to print a numbered list
    bullet_character: The symbol placed before each list element. This is
                      ignored if numbered is True.
    """
    for index, element in enumerate(l):
        if numbered:
            print("{}: {}".format(index + 1, element))
        else:
            print("{} {}".format(bullet_character, element))


print_list(["cats", "in", "space"],True)
print ("--------------------------------------------------------------")
def todo_list(new_task, base_list=['wake up']):
    base_list.append(new_task)
    return base_list

print todo_list("check the mail")
print todo_list("begin orbital transfer")
print ("--------------------------------------------------------------")

str = "Chris_iven+Chris_jack+Chris_lusy"
print str.split("+")
a = str.split("+")
print a[1]
print ("--------------------------------------------------------------")

def buy_eggs():
    egg_count = 0
    egg_count += 12 # purchase a dozen eggs
    print (egg_count)
buy_eggs()
print ("--------------------------------------------------------------")

