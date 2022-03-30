from io import BytesIO

from pytest import approx

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
    assert (
        dummy.getvalue()
        == b"\x01\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00"
    )


def test_read_uint16_and_uint32():
    dummy = BytesIO(b"\x01\x00\x02\x00\x00\x00")

    ar = CArchive(dummy, CArchiveMode.read)
    assert ar.read(Type.uint16) == 1
    assert ar.read(Type.uint32) == 2


def test_read_int16():
    dummy = BytesIO(b"\xff\xff")

    ar = CArchive(dummy, CArchiveMode.read)
    assert ar.read(Type.int16) == -1


def test_write_int16():
    dummy = BytesIO()

    ar = CArchive(dummy, CArchiveMode.write)
    ar.write(Type.int16, -1)
    assert dummy.getvalue() == b"\xff\xff"


def test_read_int32():
    dummy = BytesIO(b"\xff\xff\xff\xff")

    ar = CArchive(dummy, CArchiveMode.read)
    assert ar.read(Type.int32) == -1


def test_write_int32():
    dummy = BytesIO()

    ar = CArchive(dummy, CArchiveMode.write)
    ar.write(Type.int32, -1)
    assert dummy.getvalue() == b"\xff\xff\xff\xff"


def test_read_int64():
    dummy = BytesIO(b"\xff\xff\xff\xff\xff\xff\xff\xff")

    ar = CArchive(dummy, CArchiveMode.read)
    assert ar.read(Type.int64) == -1


def test_write_int64():
    dummy = BytesIO()

    ar = CArchive(dummy, CArchiveMode.write)
    ar.write(Type.int64, -1)
    assert dummy.getvalue() == b"\xff\xff\xff\xff\xff\xff\xff\xff"


def test_read_float():
    dummy = BytesIO(b"\xcd\xcc\xcc\x3d")

    ar = CArchive(dummy, CArchiveMode.read)
    assert approx(ar.read(Type.float)) == 0.1


def test_write_float():
    dummy = BytesIO()

    ar = CArchive(dummy, CArchiveMode.write)
    ar.write(Type.float, 0.1)
    assert dummy.getvalue() == b"\xcd\xcc\xcc\x3d"


def test_read_double():
    dummy = BytesIO(b"\x9a\x99\x99\x99\x99\x99\xb9\x3f")

    ar = CArchive(dummy, CArchiveMode.read)
    assert approx(ar.read(Type.double)) == 0.1


def test_write_double():
    dummy = BytesIO()

    ar = CArchive(dummy, CArchiveMode.write)
    ar.write(Type.double, 0.1)
    assert dummy.getvalue() == b"\x9a\x99\x99\x99\x99\x99\xb9\x3f"


def test_read_int16_and_double():
    dummy = BytesIO(b"\xff\xff\x9a\x99\x99\x99\x99\x99\xb9\x3f")

    ar = CArchive(dummy, CArchiveMode.read)
    assert ar.read(Type.int16) == -1
    assert approx(ar.read(Type.double)) == 0.1

