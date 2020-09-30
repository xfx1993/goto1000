def calcEquation(equations, values, queries):
    """
    :type equations: List[List[str]]
    :type values: List[float]
    :type queries: List[List[str]]
    :rtype: List[float]
    """

    father =dict()
    valuedict =dict()

    def findfather(node):
        curnode = node
        while father[node]!=node:
            node = father[node]
            if (node,curnode) in valuedict and (father[node],node) in valuedict and (father[node],curnode) not in valuedict:
                valuedict[(father[node],curnode)] = valuedict[(father[node],node)]*valuedict[(node,curnode)]
                valuedict[(curnode,father[node])] = 1/valuedict[(father[node],curnode)]
        return node
    for i,[a,b] in enumerate(equations):
        if b not in father:
            father[b]=b
            valuedict[(b,b)]=1.0
        if a not in father:
            father[a]=a
            valuedict[(a,a)]=1.0
        valuedict[(a,b)]=values[i]
        valuedict[(b,a)]=1/values[i]
        root_a = findfather(a)
        root_b = findfather(b)
        valuedict[(root_a,b)] = valuedict[(root_a,a)]*valuedict[(a,b)]
        valuedict[(b,root_a)] = 1/valuedict[(root_a,b)]
        valuedict[(root_a,root_b)] =  valuedict[(root_a,b)]/valuedict[(root_b,b)]
        valuedict[(root_b,root_a)] = 1/valuedict[(root_a,root_b)]
        father[root_b]=root_a
    res =[]
    for x,y in queries:
        if (x,y) in valuedict:
           res.append(valuedict[(x,y)])
        else:
            if x not in father or y not in father:
                res.append(-1.0)
            else:
                x_root = findfather(x)
                y_root = findfather(y)
                if x_root!=y_root:
                    res.append(-1.0)
                else:
                    res.append(valuedict[(y_root,y)]/valuedict[(x_root,x)])
    return res

e =[["a","b"],["e","f"],["b","e"]]
v =[3.4,1.4,2.3]
q = [["b","a"],["a","f"],["f","f"],["e","e"],["c","c"],["a","c"],["f","e"]]



print(calcEquation(e,v,q))





