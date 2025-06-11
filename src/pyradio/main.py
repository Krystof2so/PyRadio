import sys

from PySide6.QtWidgets import QApplication
from model import RadioModel
from view import RadioView
from controller import RadioController


def main():
    app = QApplication(sys.argv)

    model = RadioModel()
    view = RadioView()
    controller = RadioController(model, view) 
    _ = controller  # Utilisation triviale pour éviter l'avertissement du linter

    view.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

