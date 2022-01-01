current_age = int(input("Enter your current age: "))

remaining_age = 90 - current_age
remaining_days = remaining_age * 356
remaining_weeks = remaining_age * 52
remaining_months = remaining_age * 12

print(
    f"You have {remaining_days} days, {remaining_weeks} weeks and {remaining_months} months left"
)
