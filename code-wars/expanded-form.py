##Write Number in Expanded Form
##
##You will be given a number and you will need to return
##it as a string in Expanded Form. For example:
##
##expanded_form(12) # Should return '10 + 2'
##expanded_form(42) # Should return '40 + 2'
##expanded_form(70304) # Should return '70000 + 300 + 4'
##
##NOTE: All numbers will be whole numbers greater than 0.


def expanded_form(num):
    res=[]
    power=0
    while num/10>0:
        res.insert(0,str(num%10*10**power))
        num//=10
        power+=1
    ls=list(filter(lambda x: x!="0", res))
    return " + ".join(ls)