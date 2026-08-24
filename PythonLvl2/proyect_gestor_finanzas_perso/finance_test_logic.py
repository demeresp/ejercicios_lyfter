from logic_src_main import FinanceGestor as fg, Movement as mv
from persistance_files_managment import DataManager as dm
import pytest

def test_if_movement_to_dict_returns_dict():
    movement = mv(title="Salary", amount=1000.0, category="income", movement_type="income", date="01/01/2024")
    movement_dict = movement.movements_to_dict()

    assert isinstance(movement_dict, dict)


def test_if_from_dict_to_object_returns_movement():
    movement_dict = {
        "title": "Salary",
        "amount": 1000.0,
        "category": "income",
        "date": "01/01/2024",
        "movement_type": "income"
    }
    movement = mv.from_dict_to_object(movement_dict)

    assert isinstance(movement, mv)


def test_if_obtain_all_movements_returns_list():
    gestor = fg()
    movements = gestor.obtain_all_movements()

    assert isinstance(movements, list)


def test_spent_amount_validation():
    gestor = fg()
    valid_amount = gestor.validate_spent_amount(100.0)
    assert valid_amount == 100.0


def test_date_validation():
    gestor = fg()
    valid_date = gestor.date_validation("13/08/2024" )
    assert valid_date == "13/08/2024" 


def test_if_amount_is_negative():
    gestor = fg()
    try:
        gestor.validate_spent_amount(-50.0)
    except ValueError as e:
        assert str(e) == "Amount cannot be negative"


def test_if_expense_raises_value_error_for_invalid_amount():
    gestor = fg()
    with pytest.raises(ValueError):
        gestor.add_expense(title="Groceries", amount=-50.0, category="Food", date="01/01/2024")


def test_if_expense_raises_value_error_for_invalid_category():
    gestor = fg()
    with pytest.raises(ValueError):
        gestor.add_expense(title="Groceries", amount=50.0, category="InvalidCategory", date="01/01/2024")