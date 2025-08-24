from dataclasses import dataclass

from .base import AppView


@dataclass
class CheckboxAppView(AppView):
    """
    Флажок (Checkbox / Toggle).

    Атрибуты:
        is_checked: Состояние чекбокса.
        title: Подпись рядом с флажком.
        action: Идентификатор действия при изменении состояния.
    """

    is_checked: bool = False
    title: str = ""
    action: str | None = None