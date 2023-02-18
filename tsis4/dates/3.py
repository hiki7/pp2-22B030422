from datetime import datetime

today = datetime.now()
drop = today.replace(microsecond=0)
print(drop)
