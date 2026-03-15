"""Helpers for building multipart/form-data file mappings for HTTP uploads."""

from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path

from .types import MultipartFiles


@contextmanager
def multipart_file(file_path: str, *, field_name: str = "file") -> Iterator[MultipartFiles]:
    """Yield a multipart/form-data file mapping for an HTTP upload and close the file on exit."""
    path = Path(file_path)

    with path.open("rb") as file:
        yield {field_name: (path.name, file)}


__all__ = ("multipart_file",)
