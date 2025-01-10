import unittest
from unittest.mock import patch, mock_open
import requests
from external_api import (
    load_transactions,
    get_transaction_by_id,
    convert_to_rubles_by_transaction_id,
OPERATIONS_FILE
)

class TestTransactionUtils(unittest.TestCase):
    @patch("os.path.exists", return_value=True)
    @patch("builtins.open", new_callable=mock_open, read_data='[{"id": 1, "operationAmount": {"amount": "100.0", "currency": {"code": "USD"}}}]')
    def test_load_transactions_valid_file(self, mock_file, mock_exists):
        """
        Проверяем, что транзакции загружаются корректно.
        """
        transactions = load_transactions()
        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0]["id"], 1)
        mock_exists.assert_called_once_with(OPERATIONS_FILE)
        mock_file.assert_called_once_with(OPERATIONS_FILE, "r", encoding="utf-8")

    @patch("external_api.load_transactions", return_value=[])
    def test_get_transaction_by_id_not_found(self, mock_load_transactions):
        """
        Проверяем, что возвращается None, если транзакция не найдена.
        """
        transaction = get_transaction_by_id(1)
        self.assertIsNone(transaction)
        mock_load_transactions.assert_called_once()

    @patch("external_api.requests.get")
    @patch("external_api.get_transaction_by_id", return_value={"id": 1, "operationAmount": {"amount": "100.0", "currency": {"code": "RUB"}}})
    def test_convert_to_rubles_by_transaction_id_rub(self, mock_get_transaction, mock_requests):
        """
        Проверяем, что сумма возвращается без конвертации, если валюта RUB.
        """
        result = convert_to_rubles_by_transaction_id(1)
        self.assertEqual(result, 100.0)

        mock_get_transaction.assert_called_once_with(1)
        mock_requests.assert_not_called()

if __name__ == "__main__":
    unittest.main()