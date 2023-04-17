ans = input("Enter the character for the Diamond:")
if ans.isalpha() and len(ans)==1:
    num = int(ord(ans.upper())- 64)
    print('The position is {}'.format(num))
else:
    print('Please enter one valid letter')

# username = input("Enterq the character for the Diamond:")
# print("Username is: " + username)