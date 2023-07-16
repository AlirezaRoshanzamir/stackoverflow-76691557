"""Main entrypoint into package."""

from importlib import metadata
from typing import Optional

from .indexes import PineconeClient, CreateIndex, DeleteIndex, IndexAllDocumentsFromBlobStorage

try:
    __version__ = metadata.version(__package__)
except metadata.PackageNotFoundError:
    # Case where package metadata is not available.
    __version__ = ""
del metadata  # optional, avoids polluting the results of dir(__package__)

verbose: bool = False
debug: bool = False

__all__ = [
    "PineconeClient",
    "CreateIndex",
    "DeleteIndex",
    "IndexAllDocumentsFromBlobStorage"
]
