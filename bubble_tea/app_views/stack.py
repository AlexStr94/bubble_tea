from dataclasses import dataclass

from .constants import Axis, TextAlignment
from .complex import ComplexAppView


@dataclass
class StackAppView(ComplexAppView):
    """
    Контейнер для упорядочивания элементов (UIStackView / Column / Row).

    Атрибуты:
        axis: Ось компоновки ("vertical", "horizontal").
        spacing: Расстояние между элементами.
        alignment: Выравнивание элементов.
        elements: Вложенные элементы.
    """

    axis: Axis = Axis.VERTICAL
    spacing: int = 8
    alignment: TextAlignment = TextAlignment.LEFT
