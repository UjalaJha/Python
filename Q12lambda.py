#Print Even numbers in a list using Lambda function
my_list = [3,5,2,11,6,8]
list_Even_Numbers = list(filter(lambda varX: varX % 2 == 0,my_list))
print("Following are Even numbers in the list =")
print(list_Even_Numbers)


#Print Odd numbers in a list using Lambda function
my_list = [3,5,2,11,6,8]
list_Odd_Numbers = list(filter(lambda varX: varX % 2 == 1,my_list))
print("Following are Odd numbers in the list =")
print(list_Odd_Numbers)



my_list = [3,5,2,11,6,8]
list_square_Numbers =  list(map(lambda x: x**2, my_list))
print("Following are square in the list =")
print(list_square_Numbers)
