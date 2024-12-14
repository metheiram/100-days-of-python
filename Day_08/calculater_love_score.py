def calculate_love_score(name_01, name_02):
    print(f"Your name: {name_01}")
    print(f"Your partner's name: {name_02}")
    
    # Combine both names to check each unique letter
    combined_names = name_01 + name_02
    
    # Iterate through each unique letter in the combined names
    for letter in set(combined_names.lower()):
        # Count occurrences of the letter in both names
        count_1 = name_01.lower().count(letter)
        count_2 = name_02.lower().count(letter)
        
        # Print the letter and the count of its occurrences in each name
        print(f"'{letter}' occurs {count_1} times in {name_01} and {count_2} times in {name_02}")

# Test the function
calculate_love_score(name_01="jack", name_02="angela")
