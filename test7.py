def numOfSubarrays(arr):
    """
    :type arr: List[int]
    :rtype: int
    """
    js = 0
    os = 0
    end_js = 0
    end_os = 0
    for i in range(len(arr)):
        cur_end_js= 0
        cur_end_os = 0
        if arr[i]%2==0:
            cur_end_js=end_js
            js+=cur_end_js

            cur_end_os = 1+end_os
            os+=cur_end_os

        else:
            cur_end_js = end_os+1
            js+=cur_end_js
            cur_end_os = end_js
            os+=cur_end_os

        end_os = cur_end_os
        end_js = cur_end_js

    return js

arr = [100,100,99,99]
print(numOfSubarrays(arr))