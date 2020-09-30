def escapeGhosts( ghosts, target):
    """
    :type ghosts: List[List[int]]
    :type target: List[int]
    :rtype: bool
    """
    bias = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    used = dict()
    i = 1
    nodes = []
    for s, v in ghosts:
        used[(s, v)] = i
        nodes.append([s, v])
        i += 1

    used[(0, 0)] = 0
    nodes.append([0, 0])

    while nodes:
        nextnodes = []
        count = 0
        flag = False
        for x, y in nodes:
            for bx, by in bias:
                if -10000 <= x + bx <= 10000 and -10000 <= y + by <= 10000:
                    if used[(x, y)] == 0 and (x + bx, y + by) not in used and [x + bx, y + by] != target:
                        nextnodes.append([x + bx, y + by])
                        used[(x + bx, y + by)] = used[(x, y)]
                        count += 1
                    elif used[(x, y)] == 0 and (x + bx, y + by) not in used and [x + bx, y + by] == target:
                        flag = True
                        used[(x + bx, y + by)] = used[(x, y)]
                    elif used[(x, y)] == 0 and (x + bx, y + by) in used and [x + bx, y + by] == target:
                        if used[(x + bx, y + by)] != 0:
                            return False
                    elif used[(x, y)] != 0 and (x + bx, y + by) not in used:
                        if  [x + bx, y + by]==target:
                            return False
                        nextnodes.append([x + bx, y + by])
                        used[(x + bx, y + by)] = used[(x, y)]

                    elif used[(x, y)] != 0 and (x + bx, y + by) in used and used[(x + bx, y + by)] == 0 and [x + bx,
                                                                                                             y + by] == target:
                        return False
        if flag == True:
            return flag
        if count == 0:
            return False
        nodes = nextnodes

ghosts = [[1,0]]
target = [2,0]
print(escapeGhosts(ghosts,target))