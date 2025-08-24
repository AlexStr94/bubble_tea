from dataclasses import dataclass, field

from .complex import ComplexAppView


@dataclass(kw_only=True)
class CardAppView(ComplexAppView):
    title: str | None
    price: int
    type: str = field(init=False, default="card")
