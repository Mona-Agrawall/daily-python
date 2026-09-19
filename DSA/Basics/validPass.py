def check_password(password):

    if len(password) >= 4:
        cond1 = True
    else:
        cond1 = False

    cond2 = False

    for i in password:
        if i.isdigit():
            cond2 = True
    
    cond3 = False
    
    for i in password:
        if i.isupper():
            cond3 = True
    cond5 = True
    if(password[0].isdigit()):
        cond5 = False
                
    if cond1 and cond2 and cond3:
        return 1

    return 0


password = input("Enter password: ")
print(check_password(password))