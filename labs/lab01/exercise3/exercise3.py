# Lab 01 Exercise 3: Secure Vault System
def validate_entry(name, pin):
    if name=="Director" and pin == 1122 :
        allow = True
    elif name=="Security" and pin == 9900 :
        allow = True
    else :
        allow = False
    return allow
