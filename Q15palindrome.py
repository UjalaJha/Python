str=input("Enter string : ")
str = str.casefold()
str2=reversed(str)


if list(str) == list(str2):
   print("It is palindrome")
else:
   print("It is not palindrome")
