class Checklist:
    def __init__(self, items=None):
        if items is None:
            items = []
        self._items = items

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        if isinstance(value, list):
            self._items = value
        else:
            raise ValueError("items must be a list")

    def add_item(self, item):
        self._items.append(item)

    def remove_item(self, item):
        self._items.remove(item)

    def update_item(self, index, new_item):
        if 0 <= index < len(self._items):
            self._items[index] = new_item
        else:
            raise IndexError("Index out of range")
