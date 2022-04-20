def increment_string(strng):
    if len(strng) == 0:
        return '1'
    elif strng[-1] in '123456780':
        strng = str(strng[:-1]) + str(int(strng[-1]) + 1)
        return strng
    elif strng[-1] not in '1234567890':
        return strng + '1'
    else:
        strng = strng[::-1]
        newstr = ''
        for i in range(len(strng)):
            if strng[i] == '9':
                newstr += '0'
            elif strng[i] == '0':
                newstr = str(newstr) + str(int(strng[i]) + 1)
                newstr = str(newstr) + str(strng[i + 1::])
                break
            elif strng[i] in '12345678':
                newstr = str(newstr) + str(int(strng[i]) + 1)
                newstr = newstr + strng[i + 1::]
                break
            else:
                newstr += '1' + strng[i]
                newstr += strng[i + 1::]
                break
        return newstr[::-1]