def count_smileys(arr):
    eyes, noses, mouses = [':', ';'], ['-', '~'], [')', 'D']
    ans = 0
    for i in arr:
        if i[0] in eyes and i[-1] in mouses and (i[1] in noses or i[1] in mouses):
            ans += 1
    return ans