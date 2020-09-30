def generateSentences( synonyms, text):
    """
    :type synonyms: List[List[str]]
    :type text: str
    :rtype: List[str]
    """
    textlist = text.split(' ')
    graph = dict()
    for word1,word2 in synonyms:
        if word1 not in graph:
            graph[word1]=[]
            graph[word1].append(word2)
            if word2 not in graph:
                graph[word2] = [word1]
            else:
                if word1 not in graph[word2]:
                    graph[word2]=[word1]
        else:
            if word2 not in graph[word1]:
                graph[word1]=[word2]
            if word2 not in graph:
                graph[word2] = [word1]
            else:
                if word1 not in graph[word2]:
                    graph[word2]=[word1]

    changewords = []
    for i,w in enumerate(textlist):
        if w in graph:
            changewords.append(w)
            textlist[i]='{}'

    text1 =' '.join(textlist)

    sameword =[]
    visited=dict()
    for word in changewords:
        if word not in visited:
            cursame =[]
            used = dict()
            used[word]=1
            cursame.append(word)
            nodes=[word]
            while nodes:
                curnodes =[]
                for node in nodes:
                    for nextnode in graph[node]:
                        if nextnode not in used:
                            cursame.append(nextnode)
                            curnodes.append(nextnode)
                            used[nextnode]=1
                nodes = curnodes
            sameword.append(cursame)
            visited[word]=cursame
        else:
            sameword.append(visited[word])

    stack =[]
    res =[]
    size = len(sameword)
    def dfs(sameword,cen):
        if cen==size:
            res.append(text1.format(*stack[:]))
            return
        for w in sameword[cen]:
            stack.append(w)
            dfs(sameword,cen+1)
            stack.pop()

    dfs(sameword,0)
    res = sorted(res)
    return res



synonyms = [["happy","joy"],["sad","sorrow"],["joy","cheerful"]]
text = "I am happy today but was sad yesterday"
print(generateSentences(synonyms,text))
