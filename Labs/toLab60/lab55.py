import datetime
import datetime as dt


class Trip:
    def __init__(self, symbol, title, start, end):
        self.symbol = symbol
        self.title = title
        self.start = start
        self.end = end

    def check_data(self):
        assert self.start <= self.end, TripExceptionDate('Date error\t\t')
        assert len(self.title) > 0, TripExceptionName('Name error\t\t')

    @staticmethod
    def publish_offer(trips_list: list):
        trip_errors_dict = {}

        for x in trips_list:
            try:
                Trip.check_data(x)
            except ValueError as e:
                trip_errors_dict.setdefault(x.symbol, str(type(e).__name__) + ':\t' + str(e))
            except Exception as e:
                trip_errors_dict.setdefault(x.symbol, str(type(e).__name__) + ':\t' + str(e))
        return trip_errors_dict


class TripException(Exception):

    def __init__(self, text, description):
        super().__init__(text)
        self.description = description

    def __str__(self):
        return super().__str__() + '\t' + self.description


class TripExceptionName(TripException):
    def __init__(self, text):
        self.description = 'Name can not be empty'
        super().__init__(text, self.description)


class TripExceptionDate(TripException):
    def __init__(self, text):
        self.description = 'End date can note be earlier than start date'
        super().__init__(text, self.description)


trips = [
            Trip('IT-VNC', 'Italy-Venice', dt.date(2023, 6, 1), dt.date(2023, 6, 12)),
            Trip('SP-BRC', 'Spain-Barcelona', dt.date(2023, 6, 12), dt.date(2023, 5, 22)),
            Trip('IT-ROM', 'Italy-Rome', dt.date(2023, 6, 21), dt.date(2023, 6, 12))
        ]

try:
    print('Started checking trips')
    result = Trip.publish_offer(trips)
    print('Done')
    assert len(result) == 0, str(result.values()).replace('\\t', '\t').replace(', ', ',\n').replace('[\'', '[\n\'')
except Exception as e:
    print(e)
else:
    print('The offer will be published')
