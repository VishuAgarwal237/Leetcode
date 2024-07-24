
def SecondMax(nums):
    max = nums[0]
    secondmax = float('-inf')
    
    for x in nums[1:]:
        if x > max:
            secondmax = max
            max = x
        elif x > secondmax:
            secondmax = x
    print(max)
    print(secondmax)

if __name__ == "__main__":
    SecondMax([5,3,2,4,6,2,9,9])

