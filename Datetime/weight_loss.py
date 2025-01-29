import datetime

current_weight = 280
goal_weight = 160

average_weekly_weight_loss = 2

start_date = datetime.date.today()
end_date = start_date

while current_weight > goal_weight:
    end_date += datetime.timedelta(days=7)
    current_weight -= average_weekly_weight_loss

    print(end_date, current_weight)
# Output:

print(
    f"You will reach your goal weight {goal_weight} in {(end_date - start_date).days // 7} weeks."
)
