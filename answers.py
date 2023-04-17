ans = input("Enter the character for the Diamond:")
if ans.isalpha() and len(ans)==1:
    n = int(ord(ans.upper())- 64)
    # print('The position is {}'.format(n))

    for i in range(1, n+1):
        for j in range(1, n-i+1):
            print(" ", end="")
        for k in range(1, 2*i):
            if k==1 or k==2*i-1:
                print(str(chr(64+i)), end="")
            else:
                print(" ", end="")
        print()
    
    for i in range(n-1,0,-1):
        for j in range(1, n-i+1):
            print(" ", end="")
        for k in range(1, 2*i):
            if k==1 or k==2*i-1:
                print(str(chr(64+i)), end="")
            else:
                print(" ", end="")
        print()
else:
    print('Please enter one valid letter')

