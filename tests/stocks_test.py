import unittest

from stocks import MonthlyPriceTransform

# To run - python -m unittest tests/stocks_test.py

class TestMonthlyPriceTransform(unittest.TestCase):

    def _assert_key_is_required(self, key, expected_result):
        actual_result = MonthlyPriceTransform.store_this_key(key)
        self.assertEqual(expected_result, actual_result)

    def test_store_this_key(self):
        # Only interested in USD info therefore ignore all others.
        self._assert_key_is_required("1a. open (CNY)", False)
        self._assert_key_is_required("1b. open (USD)", True)
        self._assert_key_is_required("1a. open (CNY)", False)
        self._assert_key_is_required("1b. open (USD)", True)
        self._assert_key_is_required("2a. high (CNY)", False)
        self._assert_key_is_required("2b. high (USD)", True)
        self._assert_key_is_required("3a. low (CNY)", False)
        self._assert_key_is_required("3b. low (USD)", True)
        self._assert_key_is_required("4a. close (CNY)", False)
        self._assert_key_is_required("4b. close (USD)", True)
        self._assert_key_is_required("5. volume", True)
        self._assert_key_is_required("6. market cap (USD)", True)
