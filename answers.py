# Ask for input
ans = input("Enter the character for the Diamond:")

# Test the validity of input
if ans.isalpha() and len(ans)==1:

    # Convert the character into uppercase
    # Calculate the length of diamond 
    # The unicode for A is 65
    n = int(ord(ans.upper())- 64)

    # Draw upper side of diamond
    # The forloop are based on the mathmatical observations
    for i in range(1, n+1):
        # Draw empty space
        for j in range(1, n-i+1):
            # The end character should be identified by whitespace and not a newline
            print(" ", end="")
        # Draw character
        for k in range(1, 2*i):
            if k==1 or k==2*i-1:
                print(str(chr(64+i)), end="")
            else:
                # Draw empty space
                print(" ", end="")
        # Draw empty space
        print()

    # Draw lower side of diamond
    # Reverse order
    for i in range(n-1,0,-1):
        for j in range(1, n-i+1):
            print(" ", end="")
        for k in range(1, 2*i):
            if k==1 or k==2*i-1:
                print(str(chr(64+i)), end="")
            else:
                print(" ", end="")
        print()
# For invalid input
else:
    print('Please enter one valid character')

