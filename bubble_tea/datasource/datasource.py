from dataclasses import asdict, dataclass


@dataclass
class DataSource:
    url: str
    items_key: str = "results"

    def to_dict(self):
        return asdict(self)
