from dataclasses import dataclass, field

@dataclass
class Cmmand:
    action: str

    object_type: str

    parameters: dict = field(default_factory=dict)