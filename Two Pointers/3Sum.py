'''
Use a moving two pointer method, so that one pointer is fixed 

1. Sort nums
2. Loop through nums indexes except for the last 2 values
3. Intiialize left to be i + 1 and right to be len(nums) - 1
4. While left < right, 
    if the sum is == 0, then append the values at those indices to returning array, increment left and decrement right but use 
    inner while loops to make sure that the next vals for left and right are not the same as the direct previousl val
    elif the sum is < 0, then increment left
    else increment right
6. Add a check in the beginning of the for loop to make sure that the val at the new i is not equal to the previous ith value 
    because the same assortment of numbers can be added again
5. return arr

'''
