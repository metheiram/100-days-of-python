#random password generator 

letter=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
number=['1', '2',' 3', '4', '5', '6', '7', '8',' 9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*']


print("Welcome to the  py  password generator")
r_letter=int(input("how many letters you want to include"))
r_number=int(input("how many numbers you want to include"))
r_symbols=int(input("how many symbols you want to include"))


#easy level you can generate it by sequence 

generate = r_letter,r_number,r_symbols
print(generate)

