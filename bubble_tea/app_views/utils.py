from collections.abc import Iterable
from dataclasses import field, fields, is_dataclass, make_dataclass, MISSING
from typing import TYPE_CHECKING, Any

from . import AppView, ComplexAppView


def bindingAppView(
    app_view: "AppView",
    kwargs: dict[str, Any],
) -> "AppView":
    """
    На основании одного подкласса AppView создает новый подкласс AppView,
    в котором можно передавать значения используя синтаксис django templates.
    """

    if not is_dataclass(app_view):
        raise TypeError("Expected a dataclass class")

    new_fields = []

    for f in fields(app_view):
        name = f.name
        if (value := kwargs.get(name)) and type(value) == str and f.type != str:
            _type = str
        else:
            _type = f.type

        if f.default is not MISSING:
            new_fields.append((name, _type, field(default=f.default)))
        elif f.default_factory is not MISSING:
            new_fields.append((name, _type, field(default_factory=f.default_factory)))
        else:
            new_fields.append((name, _type))

    NewClass = make_dataclass(
        cls_name=f"Bound{app_view.__name__}",
        fields=new_fields,
        kw_only=True,
    )
    return NewClass(**kwargs)


def make_app_view(
    cls_name: str,
    fields: Iterable[str | tuple[str, Any] | tuple[str, Any, Any]],
    complex: bool = True
) -> AppView:
    bases = (ComplexAppView,) if complex else (AppView,)
    return make_dataclass(
        cls_name=cls_name,
        fields=fields,
        bases=bases
    )
