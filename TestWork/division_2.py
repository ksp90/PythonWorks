def large_division(divident,divisor,step):
    length_divisor = len(divisor)
    length_divident = len(divident)
    temp_num=''
    temp_res=0
    res=''
    if length_divident>length_divisor:
        temp_num=divident[:length_divisor]

        
def getDifference(divdnt,divsr,num):
    # '12345' '12456' 5
    dif=0
    length_divisor=len(divsr)
    #if divisor is less
    if (length_divisor<num):
        for i in range(num-length_divisor):
            divsr += '0'
    for i in range(0,num):
        divsr_num = int(divsr[i])
        divdnt_num = int(divdnt[i])
        tmp_diff = divdnt_num-divsr_num
        tmp_diff = tmp_diff*(10**(num-i-1))
        dif+=tmp_diff
