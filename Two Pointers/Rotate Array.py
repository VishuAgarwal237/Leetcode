'''
Use array slicing

1. Make sure to do k = k % len(nums) to check k isnt too big 
2. nums[:] makes sure that the arr is changed in place
3. Then slice nums from index -k to 0 (end of nums) then append on the beginning to the -kth index.

nums[:] = nums[-k:] + nums[:-k]

'''        
