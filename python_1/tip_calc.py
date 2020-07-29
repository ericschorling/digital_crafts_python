bill_amount = int(input("Total bill amount? "))
lvl_service = input("Level of service? ")

good_serv = 0.20
fair_serv = 0.15
bad_serv = 0.10

def output_func (bill_total, tip_val):
    print("Tip amount: $%.2f" % (bill_total * tip_val))
    print("Total amount: $%.2f" % (bill_total *(1+tip_val)))

if lvl_service == 'good':
    output_func(bill_amount, good_serv)
elif lvl_service =='fair':
    output_func(bill_amount, fair_serv)
else:
    output_func(bill_amount, bad_serv)

