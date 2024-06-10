'''
1. Create empty stack
2. Create dict of bracket pairs like d = {"(":")", "{":"}", "[":"]"}
3. Iterate through string, 
    if x is an open bracket, then append it to stack
    Else
        if stack empty, return false
        if x is the dict value of the last val in the stack, pop last element of stack
        Else return false
4. If stack is empty, return true, else false

'''