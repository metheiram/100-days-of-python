#cheaking heighest score 

students_score = [100,23,45,67,89,99,199,182,788,34,55,67]

# totalmarks=sum(students_score)
# print(totalmarks)

# max_num  = max(students_score)
# print(max_num)


#now the task is  find maximum number by using loop 
score=0
for max_score in students_score:
    if max_score> score:
       score= max_score

print(score)