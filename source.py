import math

result = 0

def gratuity_calculation(P, n, m, e):
    if m>=5 :
        n = n+1
    if n<5:
        printf("\nTo be eligible for gratuity under the Gratuity Act")
        printf("\n an employee needs to have at least five full years of service")
        printf("\n with the current employer, except in the event that an employee")
        printf("\n passes away or is rendered disabled due to accident or illness.")
        printf("\n In these cases, gratuity must be paid.\n")

    if e==1 :
        result = P*((float)15/26)*n
        return result
    elif e==0 :
        result = (P)*((float)15/30)*(n)
        return result
    else :
        print("\nPlease try again")
        return 0

def fixed_deposit(P, n, r) :
    result = P*(pow((1+(float)r/100), n))-P
    return result


def roi(P, n, r) :
    result = P*(pow((1+(float)r/100),n))-P
    return result

def emi(P, n, r) :
    R = 0.0
    R = r/1200
    N = 0.0
    N = n*12
    res = (long double)pow((1+R), N)/(pow((1+R), (N-1)))
    result = (P * R * res)
    return result



printf("\n****Welcome to the Financial Calculator****\n")
while(1) :
    financial_calculator_menu()
    

def financial_calculator_menu():
    printf("\nSupported Financial Operations\n")
    printf("\n1. Gratuity Calculation for private sector employees")
    printf("\n2. Fix Deposit maturity amount Calculation")
    printf("\n3. Return on Investment on Mutual Funds")
    printf("\n4. EMI Calculation")
    printf("\n5. Exit")
    printf("\n\tEnter your choice\n")
    scanf("%u", &financial_calculator_operation)

    if EXIT == financial_calculator_operation :
        printf("\nThank you. Exiting the Application\n")
        exit(0)


print(gratuity_calculation(3000,5,5,1))
print(fixed_deposit(100000,3,6.65))
print(roi(0,5,10))
print(emi(0,5,10))