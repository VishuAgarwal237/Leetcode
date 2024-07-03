'''
1. Initialize last variable index for nums1 and also decrement m and n to use as indices
2. While n >= 0,  (loops through vars that need to be inserted in nums1)
    if m >= 0 and nth index in nums2 is greater than mth index in nums1, move mth index in nums1 to last
        decrement m and last
    else if nth index in nums2 is less than or equal to mth index in nums1, make the last index in nums1 equal to nth index in nums2
    (If m is already exhausted (i.e., m < 0), it will still copy elements from nums2 to nums1.)
        decrement n and last 

'''
