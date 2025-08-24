from dataclasses import dataclass

from .base import AppView


@dataclass
class SwitchAppView(AppView):
    """
    Переключатель (UISwitch / Switch).

    Атрибуты:
        is_on: Текущее состояние.
        on_color: Цвет включённого состояния.
        thumb_color: Цвет бегунка.
        action: Идентификатор действия при переключении.
    """

    is_on: bool = False
    on_color: str = "#34C759"
    thumb_color: str = "#FFFFFF"
    action: str | None = None