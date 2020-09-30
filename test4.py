def maxA( N):
    """
    :type N: int
    :rtype: int
    """
    print_A = 0
    catch_A = 0
    ready_copy_A = 0
    copy_A = 0

    lastcopy = []

    for i in range(N):
        cur_print_A=max(print_A,catch_A,ready_copy_A,copy_A)+1
        cur_catch_A = max(print_A,copy_A)
        cur_ready_copy_A = catch_A
        cur_copy_A = 0
        if ready_copy_A!=0:
            if not lastcopy:
                cur_copy_A =ready_copy_A*2
                lastcopy.append((i,cur_copy_A,ready_copy_A))
            else:
                max_cur_copy_A = ready_copy_A*2
                for j in range(len(lastcopy)-1,-1,-1):
                    cen,c,r = lastcopy[j]
                    max_cur_copy_A = max(max_cur_copy_A,c+(i-cen)*r)

                lastcopy.append((i,ready_copy_A*2,ready_copy_A))
                cur_copy_A = max_cur_copy_A



        #更新
        print_A = cur_print_A
        catch_A = cur_catch_A
        ready_copy_A = cur_ready_copy_A
        copy_A = cur_copy_A


    return max(print_A,catch_A,ready_copy_A,copy_A)

print(maxA(34))