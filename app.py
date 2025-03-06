import re
password = re.findall(r"\d","i have 20 PKR in my bag and 321$ in my bank account.")
print(password) # 2 \d matches one digit at a time.
num = re.findall(r"\(\d{4}\)-\d{4}-\d{4}|\d{10}","heloo my number is 9807642323 and (9990)-8888-9999.")
print(num)
patt = re.findall( r"FY\d{4} Q[1-4]","It is FY2021 Q1 and the other id FY2020 Q4 and $3 billion FY2023 Q5")
print(patt)
text = '''it is FY2021 Q1 and the other id Fy2020 Q4 and $3 billion
FY2023 Q5'''
pattern = "FY(\d{4} Q[1-4])"
matches = re.findall(pattern, text, flags=re.IGNORECASE)
print(matches)