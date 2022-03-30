from io import BytesIO

from pycarchive import __version__
from pycarchive.core import CArchive, CArchiveMode, Type


def test_version():
    assert __version__ == "0.1.0"


def test_read_uint16():
    dummy = BytesIO(b"\x01\x00")

    ar = CArchive(dummy, CArchiveMode.read)
    assert ar.read(Type.uint16) == 1


def test_write_uint16():
    dummy = BytesIO()

    ar = CArchive(dummy, CArchiveMode.write)
    ar.write(Type.uint16, 1)
    assert dummy.getvalue() == b"\x01\x00"


def test_read_2_uint16():
    dummy = BytesIO(b"\x01\x00\x02\x00")

    ar = CArchive(dummy, CArchiveMode.read)
    assert ar.read(Type.uint16) == 1
    assert ar.read(Type.uint16) == 2


def test_write_2_uint16():
    dummy = BytesIO()

    ar = CArchive(dummy, CArchiveMode.write)
    ar.write(Type.uint16, 1)
    ar.write(Type.uint16, 2)
    assert dummy.getvalue() == b"\x01\x00\x02\x00"


def test_read_uint32():
    dummy = BytesIO(b"\x01\x00\x00\x00")

    ar = CArchive(dummy, CArchiveMode.read)
    assert ar.read(Type.uint32) == 1


def test_write_uint32():
    dummy = BytesIO()

    ar = CArchive(dummy, CArchiveMode.write)
    ar.write(Type.uint32, 1)
    assert dummy.getvalue() == b"\x01\x00\x00\x00"


def test_read_2_uint32():
    dummy = BytesIO(b"\x01\x00\x00\x00\x02\x00\x00\x00")

    ar = CArchive(dummy, CArchiveMode.read)
    assert ar.read(Type.uint32) == 1
    assert ar.read(Type.uint32) == 2


def test_write_2_uint32():
    dummy = BytesIO()

    ar = CArchive(dummy, CArchiveMode.write)
    ar.write(Type.uint32, 1)
    ar.write(Type.uint32, 2)
    assert dummy.getvalue() == b"\x01\x00\x00\x00\x02\x00\x00\x00"


def test_read_uint64():
    dummy = BytesIO(b"\x01\x00\x00\x00\x00\x00\x00\x00")

    ar = CArchive(dummy, CArchiveMode.read)
    assert ar.read(Type.uint64) == 1


def test_write_uint64():
    dummy = BytesIO()

    ar = CArchive(dummy, CArchiveMode.write)
    ar.write(Type.uint64, 1)
    assert dummy.getvalue() == b"\x01\x00\x00\x00\x00\x00\x00\x00"


def test_read_2_uint64():
    dummy = BytesIO(b"\x01\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00")

    ar = CArchive(dummy, CArchiveMode.read)
    assert ar.read(Type.uint64) == 1
    assert ar.read(Type.uint64) == 2


def test_write_2_uint64():
    dummy = BytesIO()

    ar = CArchive(dummy, CArchiveMode.write)
    ar.write(Type.uint64, 1)
    ar.write(Type.uint64, 2)
    assert dummy.getvalue() == b"\x01\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00"


def test_read_uint16_and_uint32():
    dummy = BytesIO(b"\x01\x00\x02\x00\x00\x00")

    ar = CArchive(dummy, CArchiveMode.read)
    assert ar.read(Type.uint16) == 1
    assert ar.read(Type.uint32) == 2
