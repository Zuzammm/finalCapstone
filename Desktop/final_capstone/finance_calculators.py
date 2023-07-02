import math
print ("investment - to calculate the amount of interest you'll earn on your investment")
print ("bond - to calculate the amount you'll have to pay on a home loan")

#Based on user's input the programm will proceed with the calculations or show an error message and ask the user to input the choice again

while True:
    calculation_choice = input ("Enter either 'investment' or 'bond' from the menu above to proceed:").lower ()
 #the following part of code calculates the return on ivestment
    if calculation_choice == "investment":
        deposit_amount = float(input("Please enter the amount of money you are depositing:"))
        interest_rate_investment = float(input("Please enter your interest rate. Please enter only the number:"))
        years_investment = int(input("Please enter the number of years you plan on investing:"))
        while True:
            interest = input ("Please select whether you want 'simple' or 'compound' interest: ").lower ()
            if interest == "simple":
                final_investment_amount = deposit_amount *(1 + (interest_rate_investment / 100) * years_investment)
                break
            elif interest == "compound":
                final_investment_amount = deposit_amount * math.pow((1+(interest_rate_investment / 100)),years_investment)
                break
            else: print ("Please enter a valid interest option. Enter simple or compound.")
            continue
        print(f"Yor return on investment after {years_investment} years will be {final_investment_amount}.")
        break
#the following part of code calculates the value of a bond
    elif calculation_choice == "bond":
        house_value = float(input("Please enter the value of the poperty:"))
        interest_rate_bond = float(input("Please enter your interest rate. Please enter only the number:"))
        months_bond = int(input("Please enter the number of of months you plan to take to repay the house:"))
        repayment = ((interest_rate_bond / 100/ 12) * house_value)/(1 - (1 + (interest_rate_bond / 100/ 12))**(-months_bond))
        print(f"The amount that you will have to repay on a home loan each month is {repayment}.")
        break
#the following part of the code shows an error message if an invalid choice was made
    else: print ("Invalid choice. Please choose either investment or bond.")
    continue

