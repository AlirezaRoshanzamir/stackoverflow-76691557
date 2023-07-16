import inspect

from e61indexingclient import CreateIndex
from e61indexingclient import PineconeClient


def test_installed_package():
    assert CreateIndex == "CreateIndex dummy value."
    assert inspect.ismodule(PineconeClient)


if __name__ == "__main__":
    test_installed_package()
