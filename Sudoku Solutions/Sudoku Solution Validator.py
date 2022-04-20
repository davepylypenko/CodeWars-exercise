def valid_solution(board):
    # gorizont
    for i in range(9):
        a = set(board[i])
        if len(a) != 9:
            return False
    # vertical
    for i in range(9):
        a = set()
        for j in range(9):
            a.add(board[j][i])
        if len(a) != 9:
            return False
    # cube
    for i in range(0, 9, 3):
        a = set()
        for j in range(3):
            b = board[j][i: i + 3]
            for k in b:
                a.add(k)
        if len(a) != 9:
            return False
        a = set()
        for j in range(3, 6):
            b = board[j][i: i + 3]
            for k in b:
                a.add(k)
        if len(a) != 9:
            return False
        a = set()
        for j in range(6, 9):
            b = board[j][i: i + 3]
            for k in b:
                a.add(k)
        if len(a) != 9:
            return False
    return True