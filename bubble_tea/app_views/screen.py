from dataclasses import dataclass, field
from typing import ClassVar

from ..descriptors import ClassOnlyMethod
from . import ComplexAppView


@dataclass(kw_only=True)
class ScreenAppView(ComplexAppView):
    """Класс экрана приложения."""

    class StartScreenAlreadyExists(Exception):
        """Не возможно создать больше одного стартового экрана для приложения."""

    name: str
    title: str
    start: bool = False
    type: str = field(init=False, default="screen")

    _registry: ClassVar[list["ScreenAppView"]] = []

    def __post_init__(self) -> None:
        if self.start and next(filter(lambda x: x.start, ScreenAppView.get_screens()), False):
            raise self.StartScreenAlreadyExists()
        # Нужно также добавить проверку уникальности имени.
        ScreenAppView._registry.append(self)

    @ClassOnlyMethod
    @classmethod
    def get_screens(cls) -> list["ScreenAppView"]:
        return cls._registry
