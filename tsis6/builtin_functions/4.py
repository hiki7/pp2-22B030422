import time, math

value = float(input("Value = "))
delay = int(input("Time delay = "))
root = math.sqrt(value)
time.sleep(delay*0.001)
print("Square root of",value, "after",delay, "miliseconds is",root)