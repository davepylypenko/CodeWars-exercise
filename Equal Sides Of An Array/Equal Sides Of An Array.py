def find_even_index(arr):
    sumpre = 0
    sumnext = 0
    ans = -1
    for i in range(len(arr)):
        for j in range(i):
            sumpre += arr[j]
        for k in range(i + 1, len(arr)):
            sumnext += arr[k]
        if sumpre == sumnext:
            ans = i
            break
        else:
            sumpre = 0
            sumnext = 0
    return ans