bill_amount = int(input("Total bill amount? "))
lvl_service = input("Level of service? ")
ppl_eating = int(input("Number of people at the table: "))

good_serv = 0.20
fair_serv = 0.15
bad_serv = 0.10

def output_func (bill_total, tip_val, people_there):
    tip_amt = bill_total * tip_val
    total_bill = bill_total * (1 + tip_val)
    per_ppl_bill = total_bill / people_there

    print("Tip amount: $%.2f" % (tip_amt))
    print("Total amount: $%.2f" % (total_bill))
    print("Amount per person: $%.2f" % (per_ppl_bill))

if lvl_service == 'good':
    output_func(bill_amount, good_serv,ppl_eating)
elif lvl_service =='fair':
    output_func(bill_amount, fair_serv, ppl_eating)
else:
    output_func(bill_amount, bad_serv, ppl_eating)

