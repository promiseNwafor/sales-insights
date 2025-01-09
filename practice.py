def removeDuplicates(nums):
    if not nums:
        return 0

    k = 1  
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[k] = nums[i]
            k += 1

    return k

ans = removeDuplicates([1,1,2])

def romanToInt(s):
    dict = {'(': ')', '{': '}', '[' : ']'}
    
    for i in dict:
        print(dict[i])
        
# romanToInt(['III', 'IV', 'IX', 'LVIII', 'MCMXCIV'])

# Factorial
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

def fibonacci2(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a

def sorter(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

print(sorter([3, 2, 1]))
        
    