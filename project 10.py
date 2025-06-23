print("name:T P Aswathi\n","sec:o\n","usn:1AY24AI109")
class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.seconds = hours * 3600 + minutes * 60 + seconds

    def __str__(self):
        hours = self.seconds // 3600
        minutes = (self.seconds % 3600) // 60
        seconds = self.seconds % 60
        return f'{hours:02}:{minutes:02}:{seconds:02}'

    def time_to_int(self):
        return self.seconds

    def increment(self, seconds):
        return Time(0, 0, self.seconds + seconds)

    def is_after(self, other):
        return self.seconds > other.seconds


def int_to_time(seconds):
    return Time(0, 0, seconds)


def main():
    start = Time(9, 45, 0)
    print("Start time:", start)

    duration = Time(1, 35, 0)
    print("Duration:", duration)

    start_seconds = start.time_to_int()
    duration_seconds = duration.time_to_int()
    end = int_to_time(start_seconds + duration_seconds)

    print("End time:", end)
    print("Is end after start?", end.is_after(start))
    print("Start incremented by 500 seconds:", start.increment(500))


if __name__ == "__main__":
    main()
