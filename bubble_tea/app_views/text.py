from dataclasses import dataclass, field
from .base import AppView

from .constants import FontWeight, LineBreakMode, TextAlignment

@dataclass
class TextAppView(AppView):
    """
    UI-элемент для отображения текста (UILabel / TextView).

    Атрибуты:
        content: Текстовое содержимое.
        font_size: Размер шрифта (по умолчанию 17).
        font_weight: Начертание шрифта ("regular", "bold", "medium", ...).
        text_color: Цвет текста (hex или системное имя).
        alignment: Выравнивание текста ("left", "center", "right", "justified").
        number_of_lines: Количество строк (0 = без ограничений, по умолчанию 1).
        line_break_mode: Режим переноса ("word_wrap", "char_wrap", "clip",
            "head_truncation", "middle_truncation", "tail_truncation").
        adjusts_font_size: Автоматически уменьшать шрифт под ширину.
        minimum_scale_factor: Минимальный коэффициент уменьшения шрифта (0.0–1.0).
        is_enabled: Активен ли элемент (по умолчанию True).
        is_highlighted: Подсвечен ли текст.
        highlighted_text_color: Цвет текста при подсветке.
        background_color: Цвет фона.
        shadow_color: Цвет тени текста.
        shadow_offset: Смещение тени в формате (x, y).
    """

    content: str = ""
    font_size: int = 17
    font_weight: FontWeight = FontWeight.REGULAR
    text_color: str = "#000000"
    alignment: TextAlignment = TextAlignment.LEFT
    number_of_lines: int = 1
    line_break_mode: LineBreakMode = LineBreakMode.TAIL_TRUNCATION
    adjusts_font_size: bool = False
    minimum_scale_factor: float = 1.0
    is_enabled: bool = True
    is_highlighted: bool = False
    highlighted_text_color: str | None = None
    background_color: str | None = None
    shadow_color: str | None = None
    shadow_offset: tuple[int, int] = field(default_factory=lambda: (0, 0))
