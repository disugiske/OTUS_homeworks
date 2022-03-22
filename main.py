def is_prime(*num):
    f=[]
    for i in num:
        for a in range(2,i):
            if i%a == 0:
                f.append(i)
                break
            break
    return(list(filter(lambda x: x not in f, num)))
print(is_prime([2,3,4,56,53,7,9,5,97,6]))

