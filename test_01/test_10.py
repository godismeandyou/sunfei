def remove_duplicates(source):
    target = []

    for element in source:
        if element not in target:
            target.append(element)

    return target

a = [1,2,2,2,2,3,4,5,6,7,8,8,8,9,0]
b = remove_duplicates(a)
print b[0:]

