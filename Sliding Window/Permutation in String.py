'''
Idea is to check the Counter dict of each window of s2 to the Counter of s1

1. Create a correct counter of the s1 string and then of the initial window of s2, do initial check to see if they are equal
2. Loop through range of s2 untul len(s2)-len(s2)+1
    add the new letter (s2[i+len(s1)-1]) to the dict, decrement the old letter(s2[i-1])
    if the two counters match, return True
3. Return false as default

'''


        corr = Counter(s1)
        corr2 = Counter(s2[0:len(s1)])
        if corr == corr2: return True
        for i in range(1,len(s2)-len(s1)+1):
            corr2[s2[i-1]] = corr2[s2[i-1]] - 1
            corr2[s2[i+len(s1)-1]] = corr2[s2[i+len(s1)-1]] + 1
            if corr2 == corr:
                return True
        return False