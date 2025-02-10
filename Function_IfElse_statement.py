def age_show(age):
    new_age = age + 50
    return new_age


age = float(input("Enter your age: "))

if age < 120:
    print(age_show(age))
else:
    print("How is that possible")

# Using the conditional block with functions.
