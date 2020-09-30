def isIdealPermutation( A):
    """
    :type A: List[int]
    :rtype: bool
    """

    stack = []

    local_cnt = 0
    global_cnt = 0

    size = len(A)
    for i in range(size):
        if not stack:
            stack.append(i)
        else:
            if A[i] < A[stack[-1]]:
                if stack[-1] == i - 1:
                    local_cnt += 1
                    global_cnt += len(stack)

                else:
                    global_cnt += len(stack)
                stack.append(i)
            else:
                left = 0
                right = len(stack)-1
                while left < right:
                    mid = (left + right) // 2
                    if A[stack[mid]]> A[i]:
                        left = mid + 1
                    else:
                        right = mid
                stack.insert(left, i)
                global_cnt += left
    if global_cnt == local_cnt:
        return True
    else:
        return False


A =  [0,2,1]
print(isIdealPermutation(A))