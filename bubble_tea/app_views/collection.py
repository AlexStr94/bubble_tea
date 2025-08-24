from dataclasses import dataclass, field

from .base import AppView


@dataclass
class CollectionAppView(AppView):
    """
    Коллекция элементов (UICollectionView / RecyclerView Grid).

    Атрибуты:
        items: Элементы коллекции.
        columns: Количество колонок в сетке.
        spacing: Отступы между элементами.
        is_scrollable: Можно ли прокручивать.
    """

    items: list[AppView] = field(default_factory=list)
    columns: int = 2
    spacing: int = 8
    is_scrollable: bool = True