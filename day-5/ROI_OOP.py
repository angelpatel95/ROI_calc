class ROI:
    
    def ROI_calc(self, income, total_investment, total_expenses):
        cash_flow = income - total_expenses
        annual_cash_flow = cash_flow * 12
        Return_of_Investment = (annual_cash_flow / total_investment) * 100
        print("The return of investment is", Return_of_Investment, "%") 

income = int(input("Enter your income"))
total_expenses = int(input("What are your total expenses?"))
total_investment = int(input("What is your total investment?"))

obj_calc = ROI()

while True:
    obj_calc.ROI_calc(income, total_investment, total_expenses)
    break