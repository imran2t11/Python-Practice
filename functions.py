def fun_name():
    return 56
    print("function called")
x=fun_name()
print(x)  

def fun_2(param1):
    return param1*param1
x=fun_2(8)
print(x)  

def fun_even_num(x):
    if(x%2==0):
        return True
    else:
        return False
print(fun_even_num(8))            

def fun_count(x):
    if(x==1):
        print(x)
        return 1
    print(x)
    return fun_count(x-1)
fun_count(9)    

def length_calculation(s):
    i=0
    while(i< len(s)):
        i=i+1
    return i    
print(length_calculation("This is a demo text to calculate length"))    