from dataclasses import dataclass

from .constants import FontWeight
from .base import AppView


@dataclass
class ButtonAppView(AppView):
    """
    UI-элемент кнопки (UIButton / Button).

    Атрибуты:
        title: Текст на кнопке.
        font_size: Размер шрифта.
        font_weight: Начертание текста.
        text_color: Цвет текста.
        background_color: Цвет фона.
        action: Идентификатор действия по нажатию.
        is_enabled: Активна ли кнопка.
        corner_radius: Радиус скругления углов.
    """

    title: str = ""
    font_size: int = 17
    font_weight: FontWeight = FontWeight.REGULAR
    text_color: str = "#FFFFFF"
    background_color: str = "#007AFF"
    action: str | None = None
    is_enabled: bool = True
    corner_radius: int = 8