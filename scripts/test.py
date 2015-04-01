def twoSum(num, target):
    for index, e in enumerate(num):
        i = get_e(index, len(num), target - e, num)
        if i != -1:
            return (index + 1), (i + 1)
        else:
            continue
                
def get_e(low, high, target, array):
    
    mid = (low + high) / 2
    if low > high :
		return -1
	else:
	    if array[mid] == target:
	        return mid
	    elif array[mid] < target:
	        high = mid - 1
	        get_e(low, high, target, array)
	    else:
	        low = mid + 1
	        get_e(low, high, target, array)

num = [1, 2, 5, 7]
target = 7

a, b = twoSum(num, target)
print a, b