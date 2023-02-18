from datetime import datetime, timedelta

today = datetime.now()
fiveDaysAgo = today - timedelta(days=5)
print("Current date:", today.strftime("%Y-%m-%d"))
print("Five days ago:", fiveDaysAgo.strftime("%Y-%m-%d"))
