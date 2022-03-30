from io import BytesIO
from pycarchive import __version__
from pycarchive.core import CArchive, CArchiveMode, Type


def test_version():
    assert __version__ == '0.1.0'


def test_read_uint16():
    dummy = BytesIO(b'\x01\x00')

    ar = CArchive(dummy, CArchiveMode.read)
    assert ar.read(Type.uint16) == 1
