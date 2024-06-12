'''
DO NOT USE SORTED, USE BUCKET SORT

1. Create an array orempty arrays like so: bucket = [[] for i in range(len(nums)+1)]
2. Use Counter method to generate dict of freqs
3. Loop through keys of the dict
    For each key, the value associated to it is the index of the key in the bucket array
4. Create a array to return
5. Loop from the bucket back to front(0) since higher freqs start at the last index (higher count)
    Loop through the array in each index of bucket
    Append each val in the subarray to your return array
        If the len(returning array) == k: return returning array


'''