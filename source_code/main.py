'''
Author - Tejashri Wagh.
Aim - Implement Fianancial Calculator in python to calculate Gratuity, Fixed Deposit, EMI, ROI.
User have to select choice and enter the value of particular variable to calculate user's choice.
'''

from calculations import gratuity_calc
from calculations import FD
from calculations import roi
from calculations import emi



print("******     Welcome to the Financial Calculator     *******\n")

def financial_calculator():
    EXIT = 5

    print("\nSupported Financial Operations --")
    print("\n1. Gratuity Calculation for private sector employees") 
    print("\n2. Fix Deposit maturity amount Calculation")
    print("\n3. Return on Investment on Mutual Funds")
    print("\n4. EMI Calculation")
    print("\n5. Exit")
    print("\nEnter your choice : ")
    selection = int(input())

    if EXIT == selection :
        print("\nThank you. Exiting the Application\n")
        exit(0)

    if selection == 1 :    
        print("\nYou selected to calculate gratuity. \nEnter your last drawn salary : ")
        s_amount = int(input())

        print("\nEnter your service duration in years and months : ")
        no_of_Years = int(input())
        No_of_Months = int(input())

        print("\nEnter 1 if your organization consists of more than 10 employees else enter 0")
        eligibility = int(input())

        result = gratuity_calc(s_amount, no_of_Years, No_of_Months, eligibility) 

        print("\nGratuity amount is : ", result)

    if selection == 2:
        print("\nYou selected to calculate maturity amount of Fixed deposit.\nEnter your principal amount : ")
        p_amount = int(input())   

        print("\nEnter tenur of Fixed Deposit : ")
        no_of_Years = int(input())

        print("\nEnter rate of interest for FD : ")
        rate_of_interest = float(input())

        result = FD(p_amount, no_of_Years, rate_of_interest)
        
        print("\nMaturity amount is : ", result)

    if selection == 3:
        print("\nYou selected to calculate Return on investment for Mutual Funds.\nEnter your principal amount : ")
        p_amount = int(input())
                
        print("\nEnter tenur in years : ")
        no_of_Years = int(input())        
            
        print("\nEnter rate of interest : ")
        rate_of_interest = float(input())       
               
        result = roi(p_amount, no_of_Years, rate_of_interest)
        print("\nROI is : ", result)        

    if selection == 4 :
        print("\nYou selected to calculate EMI for a particular loan amount.\nEnter your loan amount : ")
        l_amount = int(input())
        
        print("\nEnter your loan tenur in years : ")
        no_of_Years = int(input())
               
        print("\nEnter rate of interest : ")
        rate_of_interest = float(input())
        
        result = emi(l_amount, no_of_Years, rate_of_interest)
        print("\nEMI is : ", result)

    else : 
        print("\n\t*Choice is not implemented yet* ")
        return   

while(1) : 
    financial_calculator()

# print(gratuity_calc(3000,5,5,1))
# print(FD(100000,3,6.65))
# print(roi(0,5,10))
# print(emi(0,5,10))