bill_amount = int(input("Total bill amount? "))
lvl_service = input("Level of service? ")
ppl_eating = int(input("Number of people at the table: "))

good_serv = 0.20
fair_serv = 0.15
bad_serv = 0.10

def output_func (bill_total, tip_val, people_there):
    print("Tip amount: $%.2f" % (bill_total * tip_val))
    print("Total amount: $%.2f" % (bill_total *(1+tip_val)))
    print("Amount per person: $%.2f" % ((bill_total *(1+tip_val)))//people_there)
if lvl_service == 'good':
    output_func(bill_amount, good_serv,ppl_eating)
elif lvl_service =='fair':
    output_func(bill_amount, fair_serv, ppl_eating)
else:
    output_func(bill_amount, bad_serv, ppl_eating)

