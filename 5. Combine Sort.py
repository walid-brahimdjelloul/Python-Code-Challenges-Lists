## Finally, let’s create a function that combines two different lists together and then sorts them. To do this we can combine the lists with an operation and then sort using a function call.
#Write your function here
def combine_sort(my_list1, my_list2):
  combine_list = my_list1 + my_list2
  combine_list.sort()
  return combine_list

#Uncomment the line below when your function is done
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))
