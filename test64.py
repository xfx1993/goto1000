def highFive(items):
    """
    :type items: List[List[int]]
    :rtype: List[List[int]]
    """
    import heapq

    student=dict()
    cls_size =dict()

    for id,cost in items:
        if id not in student:
            student[id]=[]
            heapq.heappush(student[id],cost)
            cls_size[id]=1
        else:
            if cls_size[id]<5:
                heapq.heappush(student[id], cost)
                cls_size[id]+=1
            else:
                if cost>student[id][0]:
                    heapq.heappop(student[id])
                    heapq.heappush(student[id],cost)
    res = [[id,sum(values)/5] for id,values in student.items()]
    res.sort(key = lambda x:x[0])


