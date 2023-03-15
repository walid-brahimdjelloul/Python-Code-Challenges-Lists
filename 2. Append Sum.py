## Let’s create a function that calculates the sum of the last two elements of a list and appends it to the end. After doing so, it will repeat this process two more times and return the resulting list.
#Write your function here
def append_sum(my_list):
    my_list.append((my_list[-1]+my_list[-2]))
    my_list.append((my_list[-1]+my_list[-2]))
    my_list.append((my_list[-1]+my_list[-2]))
    return my_list
    


#Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))
