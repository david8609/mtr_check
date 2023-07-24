# import the time module
import time

# get the current time in seconds since the epoch
seconds = time.time()

print("Seconds since epoch =", seconds)	

# Output: Seconds since epoch = 1672214933.6804628

print("Printed immediately.")
time.sleep(2.4)
print("Printed after 2.4 seconds.")
