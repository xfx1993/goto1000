def wordsTyping( sentence, rows, cols):
    """
    :type sentence: List[str]
    :type rows: int
    :type cols: int
    :rtype: int
    """
    size = len(sentence)
    wordsize = [len(w) for w in sentence]
    if max(wordsize)>cols:
        return 0

    index =0
    cursize=0
    count = 0
    currow=0
    while True:
        cursize +=wordsize[index]
        if cursize<=cols:
            cursize+=1
            index+=1
            if index==size:
                count+=1
                index=0
        else:
            currow+=1
            if currow==rows:
                break
            cursize=wordsize[index]
            if cursize <= cols:
                cursize += 1
                index += 1
                if index == size:
                    count += 1
                    index = 0
                    if cursize+wordsize[index]>cols:
                        break
    return count



rows = 3
cols = 6
sentence = ["a", "bcd", "e"]
print(wordsTyping(sentence,rows,cols))



