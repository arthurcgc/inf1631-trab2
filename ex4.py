
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
    # import pdb; pdb.set_trace()
    # variaveis que guardam o maximo e minimo até o índice corrente
    min_prod = max_prod = arr[0]
    # salvar o maximo global
    global_max = arr[0]

    for i in range(1, len(arr)):
        tmp = max_prod

        max_prod = max(arr[i], max(arr[i] * max_prod, arr[i] * min_prod))
        min_prod = min(arr[i], min(arr[i] * tmp, arr[i] * min_prod))

        global_max = max(global_max, max_prod)

    return global_max


if __name__ == "__main__":
    print(maxProduct([-1, 2, -4, 0, 5]))
