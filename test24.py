def spellchecker( wordlist, queries):
    """
    :type wordlist: List[str]
    :type queries: List[str]
    :rtype: List[str]
    """
    yuanying = ['a','e','i','o','u','A','E','I','O','U']
    pattern_normal = dict()
    pattern_big_small = dict()

    for i,word in enumerate(wordlist):
        if word not in pattern_normal:
            pattern_normal[word]=i
        if word.lower() not in pattern_big_small:
            pattern_big_small[word.lower()] = word

    def find(need,r,stack,newq,flag):
        if need ==0:
            cur = newq.format(*stack)
            if cur.lower() in pattern_big_small:
                curword = pattern_big_small[cur.lower()]
                r.append([pattern_normal[curword],curword])
                #flag[0]=True
            return
        for n in yuanying:
            stack.append(n)
            find(need-1,r,stack,newq,flag)
            stack.pop()

    def pattern_error(q):
        qlist = list(q)
        #格式化qlist
        need = 0
        for i,w in enumerate(qlist):
            if w in yuanying:
                qlist[i]='{}'
                need+=1
        newq = ''.join(qlist)
        pwordlist =[]
        stack = []
        flag =[False]
        find(need,pwordlist,stack,newq,flag)
        return pwordlist








    res = []
    for q in queries:
        if q in pattern_normal:
            res.append(q)
        elif q.lower() in pattern_big_small:
            res.append(pattern_big_small[q.lower()])
        else:
            pattern_word = pattern_error(q)
            if not pattern_word:
                res.append("")
            else:
                pattern_word.sort(key=lambda x:x[0])
                res.append(pattern_word[0][1])
    return res

wordlist =["dtk","oag","pad","nfs","xej","bys","dgp","hev","hsk","gws","kqd","ztv","fvi","irw","rhv","dys","ofl","lnt","vmq","vsp","kbv","fof","ako","gbu","mbd","szy","zlr","cpt","xck","hdg","uoo","fvm","vla","fpe","mpk","abv","mcf","ibp","num","ouv","icx","uab","wka","ozz","gte","vpv","rvd","hed","fcl","iaf","sba","wxa","gjp","qzh","kjv","fxr","msf","bwj","wqp","whj","vxu","xoe","wwh","ray","jor","vsi","yft","ngn","inf","ggw","kwj","irk","vqs","zvi","lwx","ooc","fdi","ana","jcg","rga","vow","gia","nxa","pgr","ymw","kfk","rur","bud","cfe","ffn","wnr","uzh","yff","ucx","xss","mbi","tph","efn","syu","sqz"]
queries =["aiF"]


print(spellchecker(wordlist,queries))

