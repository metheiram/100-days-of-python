#nesting is like  folder inside the folder 
#in the dictionary nesting mean we can take a list as a value of dictionary key 
#also we can take a value of another dictionary in the dictionary like 

#for example:

# dictionary={"key":"value"}
# dictionary={"key":"[list]"}
# dictionary={"key":"dictionary"}

# travel_log={"place":["france","paris","pakistan","chaina","korea","uk"],
#             "p":["apple" ,"banana",["a","b","c"]]}

# print(travel_log["p"][2][1])



#chllange fetch the data from given below dictionary

travel = {

    "france":{
        "visited_cities":["france","paris","pakistan"],
        "total_visited":12
    },

    "germany":{
        "visited_cities":["berlin","hamburg","something"],
        "total_visited":5

    },


}


print(travel["france"]["visited_cities"][1])
print(travel["germany"]["visited_cities"][0])
