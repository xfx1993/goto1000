def hIndex(self, citations):
    """
    :type citations: List[int]
    :rtype: int
    """
    size = len(citations)
    citations.sort()
    maxyyong = citations[-1]
    maxcount = 0
    for curtarget in range(maxyyong + 1):
        left = 0
        right = size - 1

        while left < right:
            mid = (left + right) // 2
            if citations[mid] < curtarget:
                left = mid + 1
            else:
                right = mid
        curcount = size - left
        if curtarget <= curcount:
            maxcount = curcount
        else:
            break
    return maxcount