from datetime import datetime, timedelta
current_day = datetime.now()
five_days_ago = current_day - timedelta(days=5)
print(five_days_ago)