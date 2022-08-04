import os.path

import pytest

from app.main import CleanUpFile

filename = "file.txt"


@pytest.fixture()
def clean_up():
    clean_up = CleanUpFile(filename)
    return clean_up


def test_if_file_is_deleted():
    with open(filename, "w") as f:
        with CleanUpFile(filename):
            f.write("111")

    assert os.path.exists(filename) is False, "File should be deleted"


def test_check_if_file_is_deleted_with_exception():
    with open(filename, "w") as f:
        with CleanUpFile(filename):
            with pytest.raises(ZeroDivisionError):
                x = 1 / 0

    assert os.path.exists(filename) is False, "File should be deleted despite exceptions"


def test_clean_up_file_constructor(clean_up):
    assert clean_up.filename == "file.txt", f"self.filename should equal filename given to constructor"


def test_clean_up_file_enter_method(clean_up):
    assert clean_up.__enter__() == clean_up, "__enter__ should return class instance"
