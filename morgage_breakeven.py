
def MorgaBreakeven(inflation_rate, initial_pay_rate, loan_term):
    house_return_rate = (1 + inflation_rate) ** loan_term - 1
    required_return = (house_return_rate/initial_pay_rate + 1) ** (1/loan_term) -1
    return required_return

rr = MorgaBreakeven(0.03,0.2,25)


def MorgaBreakeven_example(house_price,inflation_rate, initial_pay, loan_term):
   house_value = (house_price) * (1 + inflation_rate) ** loan_term
   house_return = house_value - house_price

   investment = initial_pay
   required_return = (house_return/investment + 1) ** (1/loan_term) -1
   return required_return

rr_e = MorgaBreakeven_example(500000,0.03,100000,25)