'''
All financial calculations function written here!
'''

result = 0

def gratuity_calc(P, n, m, e):
    if m>=5 :
        n = n+1
    if n<5:
        printf("\nTo be eligible for gratuity under the Gratuity Act")
        printf("\n an employee needs to have at least five full years of service")
        printf("\n with the current employer, except in the event that an employee")
        printf("\n passes away or is rendered disabled due to accident or illness.")
        printf("\n In these cases, gratuity must be paid.\n")

    if e==1 :
        result = P*(float(15/26))*n
        return result
    elif e==0 :
        result = (P)*(float(15/30))*(n)
        return result
    else :
        print("\nPlease try again")
        return 0

def FD(P, n, r) :
    result = P*(pow((1+float(r/100)), n))-P
    return result


def roi(P, n, r) :
    result = P*(pow((1+float(r/100)), n))-P
    return result

def emi(P, n, r) :
    R = 0.0
    R = r/1200
    N = 0.0
    N = n*12
    res = int(pow((1+R), N)/(pow((1+R), (N-1))))
    result = (P * R * res)
    return result
