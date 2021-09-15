'''
Question 10
Calculate number of business days between two dates using datetime module.
'''
from datetime import date, timedelta
start_date = date(2021, 9, 5)
end_date = date(2021, 9, 26)
daygenerator = ((start_date + timedelta(x) for x in
                 range((end_date - start_date).days + 1)))
res = sum(1 for day in daygenerator if day.weekday() < 5)
print("Number of business days between two dates:", res)
