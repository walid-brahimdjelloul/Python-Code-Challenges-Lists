## For the first code challenge, we are going to calculate the length of a list and then append the value to the end of the list.
#Write your function here
def append_size(my_list):
  my_list.append(len(my_list))
  return my_list

#Uncomment the line below when your function is done
print(append_size([23, 42, 108]))
