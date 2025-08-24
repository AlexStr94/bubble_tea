from dataclasses import dataclass

from ..datasource import DataSource
from . import AppView


@dataclass
class ListAppView(AppView):
    """
    Вертикальный список элементов (UITableView / RecyclerView / List).

    Атрибуты:
        item: Класс дочернего AppView-элемента.
        is_scrollable: Можно ли прокручивать список.
        separator: Отображать ли разделители между элементами.
    """

    data_source: DataSource
    item: "AppView"
    is_scrollable: bool = True
    separator: bool = True
