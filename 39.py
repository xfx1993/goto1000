def hIndex (citations):
    """
    :type citations: List[int]
    :rtype: int
    """

    size = len(citations)
    if size ==1:
        if citations[0]==0:
            return 0
        else:
            return 1

    def get(target):
        curleft = 0
        curright = size-1

        while curleft<curright:
            mid = (curleft+curright)//2
            if citations[mid]<target:
                curleft = mid+1
            else:
                curright = mid
        cur  = size-curleft
        return size-curleft

    left =0
    right =size

    while left<=right:
        mid = (left+right)//2
        if get(mid)>=mid:
            left=mid+1
        else:
            right = mid-1
    return left-1 if max(citations)!=0 else 0

citations = [1,1,1,1]

print(hIndex(citations))
