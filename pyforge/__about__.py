"""Runtime distribution metadata for PyForge."""

from importlib.metadata import PackageNotFoundError, version
from typing import Final


def _get_version() -> str:
    """Return the installed distribution version for pyforge."""
    try:
        return version("pyforge")
    except PackageNotFoundError:
        return "0+unknown"


__version__: Final[str] = _get_version()
