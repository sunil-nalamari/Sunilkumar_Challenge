# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
count =int(input())
for _ in range(count):
    num=input()
    checkNum=re.search(r'^[456][0-9]{3}-?[0-9]{4}-?[0-9]{4}-?[0-9]{4}',num)
    if checkNum:
        valid=re.sub(r'-','',num)
        if len(valid)==16:
            valid=re.search(r'(\d)\1{3}',valid)
            if valid :
                print('Invalid')
            else :
                print('Valid')
        else :
            print('Invalid')

    else :
            print('Invalid')


