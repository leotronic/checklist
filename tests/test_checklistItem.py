from model.checklistItem import ChecklistItem


def test_set_to_done():
    my_item = ChecklistItem('Testname')
    assert my_item.done is False
    my_item.set_to_done()
    assert my_item.done is True


def test_set_to_not_done():
    my_item = ChecklistItem('Testname')
    my_item.done = True
    my_item.set_to_not_done()
    assert my_item.done is False
