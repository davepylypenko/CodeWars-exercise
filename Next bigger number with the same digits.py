def next_bigger(n):
    n = str(n)
    no_sort = ''
    to_sort = []
    new_n = n[::-1]
    for i in range(len(n) - 1):
        if new_n[i] > new_n[i + 1]:
            to_sort.append(new_n[i + 1])
            to_sort.append(new_n[i])
            no_sort += new_n[i + 2:]
            new_n = new_n[i + 1]
            for j in sorted(to_sort):
                if j > new_n:
                    new_n = j
                    to_sort.remove(j)
                    break
            break
        else:
            to_sort.append(new_n[i])
    if len(new_n) > 1:
        return -1
    res = str(str(no_sort[::-1]) + str(new_n) + ''.join(sorted(to_sort)))
    if int(res) > int(n):
        return int(res)
    else:
        return -1