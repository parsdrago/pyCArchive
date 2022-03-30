from io import BytesIO

from pytest import approx
import locale
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


def test_read_asciistring():
    dummy = BytesIO(b"\x05hello")

    ar = CArchive(dummy, CArchiveMode.read)
    assert ar.read(Type.string) == "hello"


def test_read_cp932string():
    locale.getpreferredencoding = lambda: "cp932"
    dummy = BytesIO(b"\x04\x82\xb1\x82\xf1")

    ar = CArchive(dummy, CArchiveMode.read)
    assert ar.read(Type.string) == "こん"


def test_read_cp936string():
    locale.getpreferredencoding = lambda: "cp936"
    dummy = BytesIO(b"\x02\x81\x5c")

    ar = CArchive(dummy, CArchiveMode.read)
    assert ar.read(Type.string) == "乗"


def test_read_utf16lestring():
    dummy = BytesIO(b"\xff\xfe\xff\x05\x68\x00\x65\x00\x6c\x00\x6c\x00\x6f\x00")

    ar = CArchive(dummy, CArchiveMode.read)
    assert ar.read(Type.string) == "hello"


def test_write_asciistring():
    dummy = BytesIO()

    ar = CArchive(dummy, CArchiveMode.write)
    ar.write(Type.string, "hello", encoding="ascii")
    assert dummy.getvalue() == b"\x05hello"


def test_write_cp932string():
    locale.getpreferredencoding = lambda: "cp932"
    dummy = BytesIO()

    ar = CArchive(dummy, CArchiveMode.write)
    ar.write(Type.string, "こん", encoding="cp932")
    assert dummy.getvalue() == b"\x04\x82\xb1\x82\xf1"


def test_write_cp936string():
    locale.getpreferredencoding = lambda: "cp936"
    dummy = BytesIO()

    ar = CArchive(dummy, CArchiveMode.write)
    ar.write(Type.string, "乗", encoding="cp936")
    assert dummy.getvalue() == b"\x02\x81\x5c"


def test_write_utf16lestring():
    dummy = BytesIO()

    ar = CArchive(dummy, CArchiveMode.write)
    ar.write(Type.string, "hello", encoding="utf-16-le")
    assert dummy.getvalue() == b"\xff\xfe\xff\x05h\x00e\x00l\x00l\x00o\x00"
