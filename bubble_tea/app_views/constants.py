from enum import Enum


class FontWeight(str, Enum):
    """Начертания шрифта."""
    REGULAR = "regular"
    MEDIUM = "medium"
    BOLD = "bold"
    SEMIBOLD = "semibold"
    LIGHT = "light"
    THIN = "thin"


class TextAlignment(str, Enum):
    """Выравнивание текста."""
    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"
    JUSTIFIED = "justified"


class LineBreakMode(str, Enum):
    """Режим переноса и обрезки текста."""
    WORD_WRAP = "word_wrap"
    CHAR_WRAP = "char_wrap"
    CLIP = "clip"
    HEAD_TRUNCATION = "head_truncation"
    MIDDLE_TRUNCATION = "middle_truncation"
    TAIL_TRUNCATION = "tail_truncation"


class Axis(str, Enum):
    """Ось расположения или прокрутки."""
    VERTICAL = "vertical"
    HORIZONTAL = "horizontal"


class ContentMode(str, Enum):
    """Режим отображения изображения."""
    FIT = "fit"
    FILL = "fill"
    CENTER = "center"
    SCALE_ASPECT_FIT = "scale_aspect_fit"
    SCALE_ASPECT_FILL = "scale_aspect_fill"
