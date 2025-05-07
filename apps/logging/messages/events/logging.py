from dataclasses import dataclass

from queuebie.messages import Event


@dataclass(kw_only=True)
class LogEntryCreated(Event):
    message: str
    level: int
