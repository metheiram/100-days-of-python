#task 01 create a function name great(), write 3 print statment in it and simply call the function 

def great():
    print("statment 01")
    print("statment_02")
    print("statment_03")
great()

# fuctions that allows us to take inputs

def function(something):
    print(f"hello {something}")
function("angla")

#functions with more than 1 input

def great_with_2(input_1,input_02):
    print( f"what is your name and your city name {input_1}{input_02}" )

great_with_2("iram","from lahore")

#keyword argument concept
great_with_2(input_1= "iram"  ,input_02 = " from lahore")