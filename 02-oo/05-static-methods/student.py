class Duration:
    def __init__(self, seconds):
        self.__seconds = seconds

    @property
    def seconds(self):
        return self.__seconds

    @property
    def minutes(self):
        return self.__seconds // 60

    @property
    def hours(self):
        return self.__seconds // 3600

    @staticmethod
    def from_seconds(seconds):
        return Duration(seconds)

    @staticmethod
    def from_minutes(minutes):
        return Duration(minutes * 60)

    @staticmethod
    def from_hours(hours):
        return Duration(hours * 3600)
    
duration = Duration.from_minutes(60)
print(duration.seconds)  # Output: 60
print(duration.minutes)  # Output: 1

duration = Duration.from_hours(1)
print(duration.minutes)  # Output: 60
print(duration.seconds)  # Output: 3600