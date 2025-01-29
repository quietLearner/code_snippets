import datetime


goal_subs = 1000
current_subs = 10
subs_needed = goal_subs - current_subs

avg_subs_per_day = 5
days_needed = subs_needed / avg_subs_per_day

today = datetime.date.today()
delta = datetime.timedelta(days=days_needed)
goal_date = today + delta

print(f"Current subs: {current_subs}")
print(f"Subs needed: {subs_needed}")
print(f"You will reach {goal_subs} subscribers on: {goal_date}")
