def gross_salary(basic, hra, da):
    return basic + hra + da


def deductions(basic):
    return basic * 0.1


def net_salary(basic, hra, da):
    return gross_salary(basic, hra, da) - deductions(basic)
