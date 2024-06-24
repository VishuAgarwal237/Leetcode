'''
1. Initialize left = 0 and right = len(s) - 1
2. While left < right, 
    while left < right and check that the char at left is alnum, increment left
    while left < right and check that the char at right is alnum, decrement right
    Check if lowercase versions of char at right and left are not equal, then return false
    Increment left and decrement right
3. default to return True 

'''

