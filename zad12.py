for y in range(1,11,1):
    for x in range(1,11,1):

        if(y*x)>= 10:
            print (y*x , " ",end='')
        elif(y*x)== 100:
            print (y*x , " ",end='')
        else:
            print (y*x , "  ",end='')
    print("")