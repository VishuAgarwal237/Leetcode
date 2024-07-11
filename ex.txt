def test(nums):

    t1 = [0] * len(nums)
    t2 = [0] * len(nums)

    for i in range(len(nums)):
        count = 0
        if i % 2 == 0:
            if nums[i] % 2 == 0:
                t1[i] = 0
            else:
                while nums[i] % 2 == 1:
                    nums[i] = nums[i] // 2
                    count = count + 1
                t1[i] = count
        else:
            count = 0
            if nums[i] % 2 == 1:
                t1[i] = 0
            else:
                while nums[i] % 2 == 0:
                    nums[i] = nums[i] // 2
                    count = count + 1
                t1[i] = count

    for i in range(len(nums)):
        count = 0
        if i % 2 == 0:
            if nums[i] % 2 == 1:
                t2[i] = 0
            else:
                while nums[i] % 2 == 0:
                    nums[i] = nums[i] // 2
                    count = count + 1
                t2[i] = count
        else:
            count = 0
            if nums[i] % 2 == 0:
                t2[i] = 0
            else:
                while nums[i] % 2 == 1:
                    nums[i] = nums[i] // 2
                    count = count + 1
                t2[i] = count

    print(t1)
    print(t2)
    if sum(t1) > sum(t2): 
        return sum(t1)
    else:
        return sum(t2)
    
if __name__ == "__main__":
    test([5,3,2,4])
