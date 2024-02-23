import datetime
time = datetime.datetime.now()
microsecond = time.strftime("%f")
print(f"Microsecond = {microsecond}")