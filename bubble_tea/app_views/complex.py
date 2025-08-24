from dataclasses import dataclass

from . import AppView


@dataclass
class ComplexAppView(AppView):
    """Класс UI элементов, реализующий логику вложенности элементов."""

    elements: tuple["AppView"]
