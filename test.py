def subarrayBitwiseORs( A):
        """
        :type A: List[int]
        :rtype: int
        """
        count = 0
        used = dict()
        size = len(A)
        cur=[]
        for i in range(size):
            curdp = []
            for num in cur[::-1]:
                n =  num|A[i]
                if n not in used:
                    used[n]=1
                    count+=1
                curdp.append(n)
                if bin(n).count('0')==1:
                    break
            if A[i] not in used:
                used[A[i]]=1
                count+=1
            curdp.append(A[i])

            cur = curdp

        return count

A = [1,2,4]
print(subarrayBitwiseORs(A))