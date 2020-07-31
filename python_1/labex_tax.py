import sys

for x in sys.argv:
    print (x)
job_id = 0
job_dict={}
salary = ""
ins_fund = 0.165
x = 1
y = 0
soc_sec = 3500

while x < len(sys.argv):
    try:
        job_id = int(sys.argv[x][0] + sys.argv[x][1] + sys.argv[x][2])
        y = 4
        while y < len(sys.argv[x]):
            salary += sys.argv[x][y]
            y += 1
        salary = int(salary)
        job_dict[job_id] = salary
        x += 1
        salary = ""
    except: 
        print("Parameter Error")
        #print(job_id)
        #print(salary)
        break
    #while y < len(sys.argv[x]):

def calc_post_tax (tax_dict):
    for x in tax_dict:
        tax_dict[x] = post_tax_salary(tax_dict[x])

def post_tax_salary(sal):
    taxable = 0
    post_ins = sal * ins_fund
    taxable =  sal - post_ins - soc_sec
    check_val = sal - soc_sec
    if check_val <= 0 :
        return sal - post_ins
    elif check_val >0 and check_val <= 1500:
        taxes = (taxable * 0.03) - 0
        return sal - post_ins - taxes
    elif check_val > 1500 and check_val <= 4500:
        taxes = (taxable * 0.10) - 105
        return sal - post_ins - taxes
    elif check_val > 4500 and check_val <= 9000:
        taxes = (taxable * 0.20) - 555
        return sal - post_ins - taxes
    elif check_val > 9000 and check_val <= 35000:
        taxes = (taxable * 0.25) - 1005
        return sal - post_ins - taxes
    elif check_val > 35000 and check_val <= 55000:
        taxes = (taxable * 0.30) - 2755
        return sal - post_ins - taxes
    elif check_val > 55000 and check_val <= 80000:
        taxes = (taxable * 0.35) - 5505
        return sal - post_ins - taxes
    else :
        taxes = (taxable * 0.45) - 13505
        return sal - post_ins - taxes


print (job_dict)
calc_post_tax(job_dict)
print (job_dict)

for x in job_dict:
    print("%d:%.2f" % (x, job_dict[x]))