

'''Calculate the monthly payments of a fixed term mortgage over given Nth terms at a given interest rate. Also figure out how long it will take the user to pay back the loan. For added complexity, add an option for users to select the compounding interval'''

morgage_term = int(input("Enter your mortgage payment term: "))
rate = float(input("Enter your interest rate: "))
loan = int(input("enter the loan amount: "))

payment = (loan*(1+(rate/100)))/(morgage_term*12)
time = (round(float(loan/payment)))

print("your monthly payment is {}$ and you will pay back your loan within {} months".format(payment,time))
