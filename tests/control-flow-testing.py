
import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from calculate_ticket_price import calculate_ticket_price


class TestCalculateTicketPrice(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(calculate_ticket_price(-5, True), "Invalid")

    def test_case_2(self):
        self.assertEqual(calculate_ticket_price(10, False), 50000)

    def test_case_3(self):
        self.assertEqual(calculate_ticket_price(65, False), 70000)

    def test_case_4(self):
        self.assertEqual(calculate_ticket_price(30, True), 90000)

    def test_case_5(self):
        self.assertEqual(calculate_ticket_price(25, False), 100000)

    def test_case_6(self):
        self.assertEqual(calculate_ticket_price(130, False), "Invalid")


if __name__ == "__main__":
    unittest.main()
