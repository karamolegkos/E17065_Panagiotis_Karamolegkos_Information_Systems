def removeDuplicates(list):
    final_list = []             # This list will be the returned list
    d_list = []                 # Duplicate List
    for i in range(len(list)):  # Every number is consider as
        d_list.append(False)    # not a duplicate
    for i in range(len(list)):  # Run all the numbers
        if d_list[i] == True:   # If the number is a duplicate continue
            continue
        for j in range(i+1, len(list)): # If not a duplicate then test
            if list[i] == list[j]:      # all the other numbers that left
                d_list[j] = True        # if duplicate is found then mark it
    for i in range(len(list)):          # Find every number that is not a
        if d_list[i] == False:          # duplicate. Append those numbers
            final_list.append(list[i])  # in the final_list
    return final_list            # Return the final list
#############################################################################
def sortList(list):   # bubble sort
    for i in range(1, len(list)):
        for j in range(len(list)-1, i-1, -1):
            if list[j-1] > list[j]:
                temp = list[j]
                list[j] = list[j-1]
                list[j-1] = temp
    return list
#############################################################################
def removeDictDuplicates(dict):
    value_list = []             # Make two parallel lists for the dictionary
    key_list = []               # that is given
    for k,v in dict.items():    # Fill the two lists with the keys and
        value_list.append(v)    # values of the dictionary
        key_list.append(k)
    final_dict = {}             
    d_list = []                 # Take value_list and fill it up with the
    for i in range(len(dict)):  # value True at the duplicated values
        d_list.append(False)    # with the same algorithm used in the 
    for i in range(len(dict)):  # function removeDuplicates(list)
        if d_list[i] == True:   
            continue
        for j in range(i+1, len(dict)): 
            if value_list[i] == value_list[j]:      
                d_list[j] = True        
    for i in range(len(dict)):  # Update the dictionary with the non duplicate
        if d_list[i] == False:  # values
            final_dict.update({key_list[i]:value_list[i]})
    return final_dict            
#############################################################################
def sortDict(dict):   # bubble sort with parallel lists
    final_dict = {}
    value_list = []
    key_list = []
    for k,v in dict.items():
        value_list.append(v)
        key_list.append(k)
    for i in range(1, len(dict)):
        for j in range(len(dict)-1, i-1, -1):
            if value_list[j-1] > value_list[j]:
                temp_v = value_list[j]
                value_list[j] = value_list[j-1]
                value_list[j-1] = temp_v
                temp_k = key_list[j]
                key_list[j] = key_list[j-1]
                key_list[j-1] = temp_k
    for i in range(len(dict)):
            final_dict.update({key_list[i]:value_list[i]})
    return final_dict
#############################################################################
"""
The list below is made by randomizing the a_list
of the given exercise because the given list was
already sorted
"""
a_list = [16, 14, 30, 10, 28, 14, 12, 28]
print("The starting list is: \n", a_list)
a_list = removeDuplicates(a_list)
print("The list without duplicates is:\n",a_list)
a_list = sortList(a_list)
print("The sorted list is: \n",a_list) # a_list is now sorted
print()
"""
The dictionary below is made considering the a_list
for the same reason as before
"""
a_dict = {"a":16, "b":14, "c":30, "d":10, "e":28, "f":14, "g":12, "h":28}
print("The starting dictionary is: \n", a_dict)
a_dict = removeDictDuplicates(a_dict)
print("The dictionary without duplicates is: \n", a_dict)
a_dict = sortDict(a_dict)
print("The sorted dictionary is: \n", a_dict)