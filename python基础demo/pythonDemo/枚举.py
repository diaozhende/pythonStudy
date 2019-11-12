from enum import Enum,unique

@unique
class Weekday(Enum):
    Sun = 0  # Sun 的 value 被设定为 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

print(Weekday.Mon.value)
print(Weekday.Mon == Weekday.Thu)