def create_cast_list1(filename):
    cast_list = []
    filenameList = open(filename,'r')
    for line in filenameList:
        b = line.split(',')
        cast_list.append(b[0])
    filenameList.close()

    return cast_list

def create_cast_list(filename):
    cast_list = []
    with open(filename) as f:
        for line in f:
            line_data = line.split(',')
            cast_list.append(line_data[0])
    return cast_list

# s = create_cast_list('E:\\git-code\\sunfei\\txt\\flying_circus_cast.txt')
s = create_cast_list1('E:\\git-code\\sunfei\\txt\\flying_circus_cast.txt')
print (s)


