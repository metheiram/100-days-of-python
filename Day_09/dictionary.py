# dictionary 

programming_dictionary= {"bug":"error", "function":"the piece of code we want to reuse store in the function"}

#in the  dictionary there is a key and value stored in {}

print(programming_dictionary["bug"])
 
#if you want to edit the value of the key then use the given below syntax

programming_dictionary["bug"]="there is a error in the computer called bug "
print(programming_dictionary)


#loop through the dictionary 

for thing in programming_dictionary:
    print(thing)
    print(programming_dictionary[thing])