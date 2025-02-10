def currency_converter(rate, euros):
    dollars = float(euros) * float(rate)
    return float(dollars)


r = input("Enter rate")
e = input("Enter euros")

#print(currency_converter(float(r),float(e)))
print(currency_converter(r,e))
