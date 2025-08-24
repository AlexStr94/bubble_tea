from dataclasses import make_dataclass

from .base import AppView


class AppViewFactory:
    """Класс фабрика для создания объектов анонимных классов."""

    def __new__(cls, cls_name: str, elements: tuple[AppView, ...] = (), **kwargs):
        fields = [(name, type(value)) for name, value in kwargs.items()]
        
        if elements:
            fields.append(("elements", tuple[AppView, ...]))
            kwargs["elements"] = elements
        
        NewClass = make_dataclass(
            cls_name=cls_name,
            bases=(AppView,),
            fields=fields,
            kw_only=True,
        )

        return NewClass(**kwargs)
       
        