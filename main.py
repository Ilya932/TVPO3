


def calc(credit, years, procent):

    if not all(isinstance(x, (float, int)) for x in [credit, years, procent]):
        raise ValueError("Некорректный тип данных")
    if min(credit, years, procent) <= 0:
        raise ValueError("Некорректный размер данных")

    monthly_rate = procent/12/100
    total_rate = (1 + monthly_rate)**(years * 12)
    monthly_payment = credit * monthly_rate * total_rate / (total_rate - 1)
    overpayment = monthly_payment * years * 12 - credit
    result = ["ежемесячный платёж", round(monthly_payment),"переплата",round(overpayment)]
    return result





