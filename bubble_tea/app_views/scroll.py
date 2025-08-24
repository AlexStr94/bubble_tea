from dataclasses import dataclass

from .constants import Axis
from .base import AppView


@dataclass
class ScrollAppView(AppView):
    """
    Контейнер с прокруткой (UIScrollView / ScrollView).

    Атрибуты:
        content: Вложенный элемент.
        axis: Ось прокрутки ("vertical", "horizontal").
        shows_scroll_indicator: Отображать ли индикатор прокрутки.
    """

    content: AppView | None = None
    axis: Axis = Axis.VERTICAL
    shows_scroll_indicator: bool = True