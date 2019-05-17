##Your function will receive an integer between 1 and 10000
##which is the number of steps in the chromatic scale at the piano
##from bottom la to top do and repeating from bottom
##Given the number you stopped on, was it on a black key or a white key?

def black_or_white_key(keycount):
    black=2,5,7,10,12
    x=keycount%88
    if x==0:
        return "white"
    else: 
        if x%12 in black or x%12==0:
            return "black"
        else:
            return "white"