print("name:T P Aswathi\n","sec:o\n","usn:1AY24AI109")
class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def time_to_seconds(self):
        """Convert time to total seconds."""
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def seconds_to_time(self, total_seconds):
        """Convert total seconds to Time object."""
        self.hours = total_seconds // 3600
        total_seconds %= 3600
        self.minutes = total_seconds // 60
        self.seconds = total_seconds % 60

    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

def mul_time(time, number):
    """Multiply a Time object by a number and return a new Time object."""
    total_seconds = time.time_to_seconds()
    result_seconds = int(total_seconds * number)

    new_time = Time()
    new_time.seconds_to_time(result_seconds)
    return new_time

def avg_pace(finishing_time, distance):
    """Return average pace (time per mile)."""
    return mul_time(finishing_time, 1 / distance)

finishing_time = Time(1, 30, 0)  
distance = 10 

average_pace = avg_pace(finishing_time, distance)

print("Finishing Time:", finishing_time)
print("Average Pace per Mile:", average_pace)
