import unittest
import datetime


def day(date):
    thedate = datetime.date(*date)
    return thedate.strftime("%A")


def total_sundays():
    start = datetime.date(*(1901, 1, 1))
    end = datetime.date(*(2000, 12, 31))
    count = 0
    delta = datetime.timedelta(days=1)

    while start <= end:
        if start.strftime("%A") == "Sunday" and start.day == 1:
            count += 1
        start += delta

    return count


class Test(unittest.TestCase):
    def test_sunday(self):
        self.assertEqual(day((2018, 7, 1)), "Sunday")
        self.assertEqual(day((2018, 7, 2)), "Monday")
        self.assertEqual(day((2018, 7, 3)), "Tuesday")

    def test_number_of_sundays(self):
        self.assertEqual(total_sundays(), 171)


if __name__ == "__main__":
    unittest.main()
