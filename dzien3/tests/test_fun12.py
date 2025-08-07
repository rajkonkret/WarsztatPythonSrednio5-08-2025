from fun12 import filter_transactions, transactions, map_transactions, reduce_transactions, process_transactions


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
def test_map_trnsactions_usd():
    result = [1000, 200, 500, 300, 700, 0, 0]
    assert map_transactions(transactions, "USD") == result


# (.venv) PS C:\Users\CSComarch\PycharmProjects\WarsztatPythonSrednio5-08-2025\dzien3\tests> pytest .\test_fun12.py
# ======================================================================= test session starts ========================================================================
# platform win32 -- Python 3.13.5, pytest-8.4.1, pluggy-1.6.0
# rootdir: C:\Users\CSComarch\PycharmProjects\WarsztatPythonSrednio5-08-2025\dzien3\tests
# collected 2 items
#
# test_fun12.py ..                                                                                                                                              [100%]
#
# ======================================================================== 2 passed in 0.01s =========================================================================
# (.venv) PS C:\Users\CSComarch\PycharmProjects\WarsztatPythonSrednio5-08-2025\dzien3\tests>

# reduce
def test_reduce_transactions():
    assert reduce_transactions([1000, 500, 700, 0]) == 2200

def test_process_transactions_expense_eur():
    assert process_transactions(transactions, "expense", "EUR") == 400
# pytest .\test_fun12.py -v
# rootdir: C:\Users\CSComarch\PycharmProjects\WarsztatPythonSrednio5-08-2025\dzien3\tests
# collected 4 items
#
# test_fun12.py::test_filter_tranactions_income PASSED                                                                                                          [ 25%]
# test_fun12.py::test_map_trnsactions_usd PASSED                                                                                                                [ 50%]
# test_fun12.py::test_reduce_transactions PASSED                                                                                                                [ 75%]
# test_fun12.py::test_process_transactions_expense_eur PASSED                                                                                                   [100%]
#
# ======================================================================== 4 passed in 0.01s =========================================================================
# (.venv) PS C:\Users\CSComarch\PycharmProjects\WarsztatPythonSrednio5-08-2025\dzien3\tests>