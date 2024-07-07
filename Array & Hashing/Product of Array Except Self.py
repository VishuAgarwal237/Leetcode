'''
1. Calculate prefix(front to end of running prod) and postfix(end to front of running prod) arrays
2. Output array has only second element of postfix array (bc that is the first element of the output)
3. Iterate from index 1 to end-1 
    Add prefix[i-1] * post[i+1] to output array
4. Append prefix 2nd to last element (bc this is the last element of the output)
5. Return output



'''