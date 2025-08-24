from dataclasses import dataclass

from .constants import ContentMode
from .base import AppView


@dataclass
class ImageAppView(AppView):
    """
    UI-элемент для отображения изображения (UIImageView / ImageView).

    Атрибуты:
        source: Путь, URL или имя ресурса изображения.
        content_mode: Способ отображения ("fit", "fill", "center", ...).
        tint_color: Цвет для маскирования (если применимо).
        background_color: Цвет фона.
        is_interactive: Можно ли взаимодействовать с картинкой.
    """

    source: str = ""
    content_mode: ContentMode = ContentMode.FIT
    tint_color: str | None = None
    background_color: str | None = None
    is_interactive: bool = False