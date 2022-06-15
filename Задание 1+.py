from sys import argv

def calculate_salary(work_hours, rate, bonus):
    return float(work_hours) * float(rate) + float(bonus)


print(calculate_salary(argv[1], argv[2], argv[3]))