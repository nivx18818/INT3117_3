import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from calculate_ticket_price import calculate_ticket_price


class TestCalculateTicketPrice(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(calculate_ticket_price(-1, False), "Invalid")

    def test_case_2(self):
        self.assertEqual(calculate_ticket_price(10, False), 50000)

    def test_case_3(self):
        self.assertEqual(calculate_ticket_price(65, False), 70000)

    def test_case_4(self):
        self.assertEqual(calculate_ticket_price(30, False), 90000)


if __name__ == "__main__":
    unittest.main()
