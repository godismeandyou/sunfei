def box(width, height, symbol='*'):

    print(symbol * width) # print top edge of box

    # print sides of box
    for a in range(height-2):
        print(symbol + " " * (width-2) + symbol)

    print(symbol * width) # print bottom edge of box

box(7,5,'$')