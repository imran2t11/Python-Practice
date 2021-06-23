def is_password_valid(password):
    # your code goes here
    # check the solution in the discord server.
    if(len(password)<8):
        return False
    numbers_count = sum(c.isdigit() for c in password)
    if(numbers_count<2): 
        return False
    if not any(char.isupper() for char in password):  
        return False
    if not any(char.islower() for char in password): 
        return False
    else:
        return True

print(is_password_valid("S34sdderf"))  
    
        
    