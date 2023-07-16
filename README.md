# A solution to Stackoverflow question #76691557.

Create a virtual environment (whatever tool you preferred) and activate it.

Run:

    poetry build

Then:

    pip3 install --force-reinstall dist/e61indexingclient-0.0.5-py3-none-any.whl

Then:

    python3 tests/test_installed_package.py
