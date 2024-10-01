# input monthly salary and loan
salary = float(input("Enter Your Monthly Salary: "))
loan = float(input("Enter Loan Amount: "))
eligibleCheck = salary * 10
# identify if salary is much higher or equal to the needed amount
if(salary>=float(30000.00) and loan<=eligibleCheck):
    print("You are eligible fo a loan.")
    months = int(input("How Many Month to Pay: "))
    interest = loan * 0.10
    newLoan = loan + interest
    print("Amount to Pay:", newLoan / months)
# if salary is lower print the salary is to low
elif(salary<30000):
    print("You are not eligible: Salary to low.")
# if loan requested is too high print the loan requested is too high
elif(loan>eligibleCheck):
    print("You are not eligible: Loan requested is too high.")
else:
    print("Error")