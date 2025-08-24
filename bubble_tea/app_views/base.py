from dataclasses import asdict, dataclass, fields
from typing import Any

from bubble_tea.datasource.datasource import DataSource


@dataclass
class AppView:
    """Базовый класс для всех UI элементов приложения."""

    def type_name(self) -> str:
        if hasattr(self, "type"):
            return self.type
        return self.__class__.__name__.replace("AppView", "").lower()

    def to_dict(self) -> dict[str, Any]:
        result = {}
        for field in fields(self):
            value = getattr(self, field.name)
            if isinstance(value, (AppView, DataSource)):
                result[field.name] = value.to_dict()
            elif isinstance(value, list):
                result[field.name] = [
                    v.to_dict() if isinstance(v, AppView) else v for v in value
                ]
            else:
                result[field.name] = value
        result["type"] = self.type_name()
        return result
