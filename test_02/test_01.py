def hours2days(a):
    b = 1
    c = 0
    if a is None:
        return "sorry , a is null!"
    else:
        if a > 24:
            for o in range(a):
                if a - 24 > 24:
                    a = a - 24
                    b += 1
                else:
                    c = a - 24
                    break
        elif a <= 24:
            b = 0
            c = a
    return b, c

result = hours2days(25)
print ("{}days,{}hours").format(result[0],result[1])