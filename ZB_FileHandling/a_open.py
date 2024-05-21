#rawx= read, append, write, create
#tx = text file, image file
try:
    f = open('test.txt')
    #file open vayera aafai close ni hunxa
    #with open('test.txt') as:
    f.write("ma append garna sikirako xu hai\n")
    print(f.readline())
    print(f.readline())
    f.close()

except FileNotFoundError:
    print("could not found file !!! could not exit file")