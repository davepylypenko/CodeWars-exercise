"""from list of names to list who likes"""

def likes(names):
    text = 'no one likes this'
    if len(names) == 1:
        return names[0] + ' likes this'
    elif len(names) == 2:
        return names[0] + ' and ' + names[1] + ' like this'
    elif len(names) == 3:
        return names[0] + ', ' + names[1] + ' and ' + names[2] + ' like this'
    elif len(names) > 3:
        text = names[0] + ', ' + names[1] + ' and '
        num = 2
        for i in range(len(names) - 4):
            num += 1
        return text + str(num) + ' others like this'
    return text