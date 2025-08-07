from fun12 import filter_transactions, transactions


# pip install pytest

# assert - asercje

def test_filter_tranactions_income():
    expected_list = [
        {"id": 1, "type": "income", "amount": 1000, "currency": "USD"},
        {"id": 3, "type": "income", "amount": 500, "currency": "USD"},
        {"id": 5, "type": "income", "amount": 700, "currency": "USD"},
        {"id": 7, "type": "income", "amount": 100, "currency": "EUR"},
    ]
    assert filter_transactions(transactions, "income") == expected_list
# ======================================================================= test session starts ========================================================================
# platform win32 -- Python 3.13.5, pytest-8.4.1, pluggy-1.6.0
# rootdir: C:\Users\CSComarch\PycharmProjects\WarsztatPythonSrednio5-08-2025\dzien3\tests
# collected 1 item
#
# test_fun12.py .                                                                                                                                               [100%]
#
# ======================================================================== 1 passed in 0.01s =========================================================================
# (.venv) PS C:\Users\CSComarch\PycharmProjects\WarsztatPythonSrednio5-08-2025\dzien3\tests>

# map trasactionss
