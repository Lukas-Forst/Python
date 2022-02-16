# This entrypoint file to be used in development. Start by reading README.md
from time_calculator import add_time
from unittest import main

#print(add_time("11:06 PM", "2:02"))
#print(add_time("6:30 PM", "205:12"))

#print(add_time("11:40 AM", "0:25"))
#print(add_time("11:40 PM", "24:25"))
#print(add_time("11:59 PM", "24:05")) # 12:04 2 days
#print(add_time("11:59 PM", "24:05", "Wednesday"))
# Run unit tests automatically
main(module='test_module', exit=False)