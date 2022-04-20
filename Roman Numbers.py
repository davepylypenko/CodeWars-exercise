class RomanNumerals:

    """from arabic numbers to roman"""
    def to_roman(val):
        all_roman_nums = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        res = ''
        res += 'M' * (val // 1000)
        val %= 1000
        new_res = ''
        for i in range(1, (val // 100) + 1):
            if i < 4:
                new_res += 'C'
            elif i == 4:
                new_res = 'CD'
            elif i == 5:
                new_res = 'D'
            elif i < 9:
                new_res += 'C'
            elif i == 9:
                new_res = 'CM'
        res += new_res
        val %= 100
        new_res = ''
        for i in range(1, (val // 10) + 1):
            if i < 4:
                new_res += 'X'
            elif i == 4:
                new_res = 'XL'
            elif i == 5:
                new_res = 'L'
            elif i < 9:
                new_res += 'X'
            elif i == 9:
                new_res = 'XC'
        res += new_res
        val %= 10
        new_res = ''
        for i in range(1, val + 1):
            if i < 4:
                new_res += 'I'
            elif i == 4:
                new_res = 'IV'
            elif i == 5:
                new_res = 'V'
            elif i < 9:
                new_res += 'I'
            elif i == 9:
                new_res = 'IX'
        res += new_res
        return res


    """from correct roman numbers to arabic"""
    def from_roman(roman_num):
        all_roman_nums = {'M': 1000, 'D': 500, 'C':100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        res = 0
        for i in range(len(roman_num) - 1):
            if all_roman_nums[roman_num[i]] < all_roman_nums[roman_num[i + 1]]:
                res += - all_roman_nums[roman_num[i]]
            else:
                res += all_roman_nums[roman_num[i]]
        res += all_roman_nums[roman_num[- 1]]
        return res