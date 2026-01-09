# input = nums , target (type int)
# output = return True if any two numbers in the list add upt to the target

def two_sum(nums, target):
    seen = set()
    for i in nums: 
        key = target - i
        if key in seen: 
            return True
        seen.add(i)
    return False

        
if __name__== "__main__":
    print(two_sum([10, 15, 3, 7], 17))  # True
    print(two_sum([1, 2, 3], 7))        # False
    print(two_sum([2, 7, 11, 15], 9))   # True
    print(two_sum([], 5))               # False
    print(two_sum([5], 5))              # False