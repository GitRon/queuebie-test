import logging
from dataclasses import dataclass

from queuebie.messages import Command


@dataclass(kw_only=True)
class CreateLogEntry(Command):
    message: str
    level: int = logging.INFO
