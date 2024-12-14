def formate_name(f_name, l_name):
    if f_name=="" and l_name=="":
        return "you did not provide valid input"
    elif f_name=="":
        return "you have to provide your first name"
    elif l_name=="":
        return "you did not provide your second name"
    
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"your full name is {formated_f_name}" "{formated_l_name}"



print(formate_name(input("what is your first name"),input("what is your last name")))