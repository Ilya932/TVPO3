


def calc(credit, years, procent):



    monthly_rate = procent/12/100
    total_rate = (1 + monthly_rate)**(years * 12)
    monthly_payment = credit * monthly_rate * total_rate / (total_rate - 1)
    overpayment = monthly_payment * years * 12 - credit
    result = ["ежемесячный платёж", round(monthly_payment),"переплата",round(overpayment)]

    return result #результат точно





