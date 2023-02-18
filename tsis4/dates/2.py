from datetime import datetime, timedelta
today = datetime.now()
tomorrow = today + timedelta(days=1)
yesterday = today - timedelta(days=1)

print("Yesterday's date:", yesterday.strftime("%Y-%m-%d"))
print("Today's date:", today.strftime("%Y-%m-%d"))
print("Tomorrow's date:", tomorrow.strftime("%Y-%m-%d"))