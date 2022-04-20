def longest_consec(strarr, k):
    a = []
    ans = ''
    for i in range(len(strarr) - (k - 1)):
        word = ''
        for j in range(k):
            word += strarr[i + j]
        a.append(word)
    for i in a:
        if len(ans) < len(i):
            ans = i
    return ans