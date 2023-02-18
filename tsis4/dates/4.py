from datetime import datetime, timedelta

date1 = datetime.now()
date2 = date1 - timedelta(days=2)

difference = (date1 - date2).total_seconds()

print("Difference between two dates in seconds:", difference)
