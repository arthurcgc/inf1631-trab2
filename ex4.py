
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

def maxProduct(arr):
    # salva o maior valor encontrado ate agr
    res = arr[0]

    # imax/imin = maximo e minimo pordutos do subarray que acaba em arr[i]

    for i in range(1, len(arr)):
        imax = res
        imin = res

        if arr[i] < 0:
            # swap(imax, imin)
            temp = imax
            imax = imin
            imin = temp

        # produto de max e min para o numero corrente ou é o numero corrente ou o max ou o min

        imax = max(arr[i], imax * arr[i])
        imin = min(arr[i], imin*arr[i])


        res = max(res, imax)

    return res



if __name__ == "__main__":
    print(maxProduct([1,2,3,4,-5,-7]))
