
lookup = []
lookupv2 = []

def max_subarray(arr):
    if len(arr) == 1:
        return arr[0]
    for i in range(0, len(arr)):
        lookup.append(arr[i])
        lookupv2.append([arr[i]])
    for i in range(1, len(arr)):
        if lookup[i-1] + arr[i] > arr[i]:
            lookup[i] += lookup[i-1]
            lookupv2[i] = lookupv2[i-1].copy()
            lookupv2[i].append(arr[i])
    print(lookupv2)
    return max(lookup)

def maxProduct(self, nums: List[int]):
        global_max = nums[0]
        imax, imin = nums[0],nums[0]
        
        for i in range(1,len(nums)):
            print(local_min, local_max, global_max)
            candidates = (nums[i], imax * nums[i], imin * nums[i])
            imax = max(candidates)
            imin = min(candidates)            
            global_max = max(global_max, imax)
        return global_max

if __name__ == "__main__":
    print(max_subarray([1,2]))

