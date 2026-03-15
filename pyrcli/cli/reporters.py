"""Factory functions for creating ``ErrorReporter`` callbacks."""

from .types import ErrorReporter


def raises(exception_type: type[Exception]) -> ErrorReporter:
    """Return an ``ErrorReporter`` that raises ``exception_type`` with the error message."""

    def reporter(message: str) -> None:
        """Raise ``exception_type`` with ``message``."""
        raise exception_type(message)

    return reporter


def suppress(_: str) -> None:
    """Ignore the reported error message."""
    pass


__all__ = (
    "raises",
    "suppress",
)
