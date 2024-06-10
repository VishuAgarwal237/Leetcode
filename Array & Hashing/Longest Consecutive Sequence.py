'''
1. Create a set of the nums to have O(1) search
2. Make a count variable
3. Edge case: if nums is empty, return 0
4. Iterate x through the set
5. If x-1 not in s, 
    then create a temp var
    and z = x + 1 var
    while z in s, increment both temp and z
    check if temp > count, and if so, count = temp
6. Return temp outside the loop


'''
