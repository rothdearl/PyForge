"""Type aliases used by the progress package."""

from typing import Literal

#: Message rendered alongside an indicator, or ``None`` for no message.
type ProgressMessage = str | None

#: Position of the message relative to the indicator.
type ProgressMessagePosition = Literal["left", "right"]

__all__ = (
    "ProgressMessage",
    "ProgressMessagePosition",
)
