binary_rep = bin(N)
    gaps_list=binary_rep.split('1')
    if (binary_rep[0]=='1' and binary_rep[len(binary_rep)-1]=='1'):
        return len(max(gaps_list))
    elif (binary_rep[0]!='1' and binary_rep[len(binary_rep)-1]!='1'):
        gaps_list.pop()
        if len(gaps_list)==0:
            return len(gaps_list)
        gaps_list.pop(0)
        if len(gaps_list)==0:
            return len(gaps_list)
        return len(max(gaps_list))
    elif (binary_rep[0]=='1' and binary_rep[len(binary_rep)-1] !='1'):
        gaps_list.pop()
        if len(gaps_list)==0:
            return len(gaps_list)
        return len(max(gaps_list))
    else:
        gaps_list.pop(0)
        if len(gaps_list)==0:
            return len(gaps_list)
        return len(max(gaps_list))
