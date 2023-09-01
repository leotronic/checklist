from unittest.mock import Mock

from controller.checklist_controller import ChecklistController


def test_add_item():
    # Erstelle Mock-Objekte für die Abhängigkeiten
    mock_view = Mock()
    mock_model = Mock()

    # Erstelle den Controller und injiziere die Mock-Objekte
    controller = ChecklistController()
    controller.view = mock_view
    controller.checklist = mock_model

    # Rufe die Methode, die du testen möchtest, auf
    controller.add_item("Test Item")

    # Überprüfe, ob die Mock-Objekte wie erwartet aufgerufen wurden
    mock_model.add_item.assert_called_once()
    mock_view.update_view.assert_called_once()


def test_remove_item():
    mock_view = Mock()
    mock_model = Mock()

    mock_item = Mock()
    mock_item.description = "Test Item"

    controller = ChecklistController()
    controller.view = mock_view
    controller.checklist = mock_model

    controller.remove_item(mock_item)

    mock_model.remove_item.assert_called_once_with(mock_item)
    mock_view.update_view.assert_called_once()
