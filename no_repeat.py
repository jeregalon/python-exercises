# delete the repetitions in a list

list = [4, 56, 3, 4, 23, 3, 2, 56, 2, 67, 8]

# # without creating another list
# ind = -1

# for i in list:
#     ind += 1
#     reps = list.count(i)
#     while (reps > 1):
#         rest_of_the_list = list[ind + 1:]
#         del list[rest_of_the_list.index(i) + ind + 1]
#         reps = list.count(i)

# creating another list

list_no_rep = []
for i in list:
    if list_no_rep.count(i) == 0:
        list_no_rep.append(i)

list = list_no_rep[:]

print(list)        
    
