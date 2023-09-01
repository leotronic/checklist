import pytest

from model.checklist import Checklist


def test_init():
    checklist = Checklist()
    assert checklist.items == []


def test_add_item():
    checklist = Checklist()
    checklist.add_item("Milk")
    assert checklist.items == ["Milk"]


def test_remove_item():
    checklist = Checklist()
    checklist.add_item("Milk")
    checklist.remove_item("Milk")
    assert checklist.items == []


def test_update_item():
    checklist = Checklist()
    checklist.add_item("Milk")
    checklist.update_item(0, "Water")
    assert checklist.items == ["Water"]


def test_set_items():
    checklist = Checklist()
    checklist.items = ["Milk", "Water"]
    assert checklist.items == ["Milk", "Water"]


def test_invalid_set_items():
    checklist = Checklist()
    with pytest.raises(ValueError):
        checklist.items = "Not a list"


def test_index_out_of_range():
    checklist = Checklist()
    with pytest.raises(IndexError):
        checklist.update_item(999, "Doesn't matter")
