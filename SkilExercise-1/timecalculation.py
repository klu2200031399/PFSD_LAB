import time
from datetime import datetime
import pytz

time1 = pytz.timezone('Canada/Newfoundland')
print("Current time is :", datetime.now(time1))