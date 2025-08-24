from dataclasses import dataclass

from .base import AppView


@dataclass
class TextFieldAppView(AppView):
    """
    Поле для ввода текста (UITextField / EditText).

    Атрибуты:
        placeholder: Текст-заполнитель.
        text: Текущее значение поля.
        font_size: Размер шрифта.
        text_color: Цвет текста.
        is_secure: Использовать ли ввод скрытого текста (пароль).
        keyboard_type: Тип клавиатуры ("default", "numeric", "email", ...).
        is_enabled: Активно ли поле.
    """

    placeholder: str = ""
    text: str = ""
    font_size: int = 17
    text_color: str = "#000000"
    is_secure: bool = False
    keyboard_type: str = "default"
    is_enabled: bool = True