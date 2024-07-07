'''
1. Check count



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