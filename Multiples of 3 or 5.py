def solution(number):
    ans = 0
    if number > 0:
        for i in range(number):
            if i % 3 == 0 or i % 5 == 0:
                ans += i
    else:
        ans = 0
    return ans