import locale
from io import BytesIO

from pytest import approx, raises

from pycarchive import __version__
from pycarchive.__main__ import CArchive, Type, CArchiveMode

def test_version():
    assert __version__ == "0.1.0"


def test_read_uint16():
    dummy = BytesIO(b"\x01\x00")

    ar = CArchive(dummy, CArchiveMode.READ)
    assert ar.read(Type.UINT16) == 1


def test_write_uint16():
    dummy = BytesIO()

    ar = CArchive(dummy, CArchiveMode.WRITE)
    ar.write(Type.UINT16, 1)
    assert dummy.getvalue() == b"\x01\x00"


def test_read_2_uint16():
    dummy = BytesIO(b"\x01\x00\x02\x00")

    ar = CArchive(dummy, CArchiveMode.READ)
    assert ar.read(Type.UINT16) == 1
    assert ar.read(Type.UINT16) == 2


def test_write_2_uint16():
    dummy = BytesIO()

    ar = CArchive(dummy, CArchiveMode.WRITE)
    ar.write(Type.UINT16, 1)
    ar.write(Type.UINT16, 2)
    assert dummy.getvalue() == b"\x01\x00\x02\x00"


def test_read_uint32():
    dummy = BytesIO(b"\x01\x00\x00\x00")

    ar = CArchive(dummy, CArchiveMode.READ)
    assert ar.read(Type.UINT32) == 1


def test_write_uint32():
    dummy = BytesIO()

    ar = CArchive(dummy, CArchiveMode.WRITE)
    ar.write(Type.UINT32, 1)
    assert dummy.getvalue() == b"\x01\x00\x00\x00"


def test_read_2_uint32():
    dummy = BytesIO(b"\x01\x00\x00\x00\x02\x00\x00\x00")

    ar = CArchive(dummy, CArchiveMode.READ)
    assert ar.read(Type.UINT32) == 1
    assert ar.read(Type.UINT32) == 2


def test_write_2_uint32():
    dummy = BytesIO()

    ar = CArchive(dummy, CArchiveMode.WRITE)
    ar.write(Type.UINT32, 1)
    ar.write(Type.UINT32, 2)
    assert dummy.getvalue() == b"\x01\x00\x00\x00\x02\x00\x00\x00"


def test_read_uint64():
    dummy = BytesIO(b"\x01\x00\x00\x00\x00\x00\x00\x00")

    ar = CArchive(dummy, CArchiveMode.READ)
    assert ar.read(Type.UINT64) == 1


def test_write_uint64():
    dummy = BytesIO()

    ar = CArchive(dummy, CArchiveMode.WRITE)
    ar.write(Type.UINT64, 1)
    assert dummy.getvalue() == b"\x01\x00\x00\x00\x00\x00\x00\x00"


def test_read_2_uint64():
    dummy = BytesIO(b"\x01\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00")

    ar = CArchive(dummy, CArchiveMode.READ)
    assert ar.read(Type.UINT64) == 1
    assert ar.read(Type.UINT64) == 2


def test_write_2_uint64():
    dummy = BytesIO()

    ar = CArchive(dummy, CArchiveMode.WRITE)
    ar.write(Type.UINT64, 1)
    ar.write(Type.UINT64, 2)
    assert (
        dummy.getvalue()
        == b"\x01\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00"
    )


def test_read_uint16_and_uint32():
    dummy = BytesIO(b"\x01\x00\x02\x00\x00\x00")

    ar = CArchive(dummy, CArchiveMode.READ)
    assert ar.read(Type.UINT16) == 1
    assert ar.read(Type.UINT32) == 2


def test_read_int16():
    dummy = BytesIO(b"\xff\xff")

    ar = CArchive(dummy, CArchiveMode.READ)
    assert ar.read(Type.INT16) == -1


def test_write_int16():
    dummy = BytesIO()

    ar = CArchive(dummy, CArchiveMode.WRITE)
    ar.write(Type.INT16, -1)
    assert dummy.getvalue() == b"\xff\xff"


def test_read_int32():
    dummy = BytesIO(b"\xff\xff\xff\xff")

    ar = CArchive(dummy, CArchiveMode.READ)
    assert ar.read(Type.INT32) == -1


def test_write_int32():
    dummy = BytesIO()

    ar = CArchive(dummy, CArchiveMode.WRITE)
    ar.write(Type.INT32, -1)
    assert dummy.getvalue() == b"\xff\xff\xff\xff"


def test_read_int64():
    dummy = BytesIO(b"\xff\xff\xff\xff\xff\xff\xff\xff")

    ar = CArchive(dummy, CArchiveMode.READ)
    assert ar.read(Type.INT64) == -1


def test_write_int64():
    dummy = BytesIO()

    ar = CArchive(dummy, CArchiveMode.WRITE)
    ar.write(Type.INT64, -1)
    assert dummy.getvalue() == b"\xff\xff\xff\xff\xff\xff\xff\xff"


def test_read_float():
    dummy = BytesIO(b"\xcd\xcc\xcc\x3d")

    ar = CArchive(dummy, CArchiveMode.READ)
    assert approx(ar.read(Type.FLOAT)) == 0.1


def test_write_float():
    dummy = BytesIO()

    ar = CArchive(dummy, CArchiveMode.WRITE)
    ar.write(Type.FLOAT, 0.1)
    assert dummy.getvalue() == b"\xcd\xcc\xcc\x3d"


def test_read_double():
    dummy = BytesIO(b"\x9a\x99\x99\x99\x99\x99\xb9\x3f")

    ar = CArchive(dummy, CArchiveMode.READ)
    assert approx(ar.read(Type.DOUBLE)) == 0.1


def test_write_double():
    dummy = BytesIO()

    ar = CArchive(dummy, CArchiveMode.WRITE)
    ar.write(Type.DOUBLE, 0.1)
    assert dummy.getvalue() == b"\x9a\x99\x99\x99\x99\x99\xb9\x3f"


def test_read_int16_and_double():
    dummy = BytesIO(b"\xff\xff\x9a\x99\x99\x99\x99\x99\xb9\x3f")

    ar = CArchive(dummy, CArchiveMode.READ)
    assert ar.read(Type.INT16) == -1
    assert approx(ar.read(Type.DOUBLE)) == 0.1


def test_read_asciistring():
    dummy = BytesIO(b"\x05hello")

    ar = CArchive(dummy, CArchiveMode.READ)
    assert ar.read(Type.STRING) == "hello"


def test_read_long_asciistring():
    dummy = BytesIO(b"\xff\xe8\03" + b"a" * 1000)

    ar = CArchive(dummy, CArchiveMode.READ)
    assert ar.read(Type.STRING) == "a" * 1000


def test_write_asciistring():
    dummy = BytesIO()

    ar = CArchive(dummy, CArchiveMode.WRITE)
    ar.write(Type.STRING, "a" * 1000)
    assert dummy.getvalue() == b"\xff\xe8\03" + b"a" * 1000


def test_read_cp932string():
    locale.getpreferredencoding = lambda: "cp932"
    dummy = BytesIO(b"\x04\x82\xb1\x82\xf1")

    ar = CArchive(dummy, CArchiveMode.READ)
    assert ar.read(Type.STRING) == "こん"


def test_read_cp936string():
    locale.getpreferredencoding = lambda: "cp936"
    dummy = BytesIO(b"\x02\x81\x5c")

    ar = CArchive(dummy, CArchiveMode.READ)
    assert ar.read(Type.STRING) == "乗"


def test_read_utf16lestring():
    dummy = BytesIO(b"\xff\xfe\xff\x05\x68\x00\x65\x00\x6c\x00\x6c\x00\x6f\x00")

    ar = CArchive(dummy, CArchiveMode.READ)
    assert ar.read(Type.STRING) == "hello"


def test_write_asciistring():
    dummy = BytesIO()

    ar = CArchive(dummy, CArchiveMode.WRITE)
    ar.write(Type.STRING, "hello", encoding="ascii")
    assert dummy.getvalue() == b"\x05hello"


def test_write_cp932string():
    locale.getpreferredencoding = lambda: "cp932"
    dummy = BytesIO()

    ar = CArchive(dummy, CArchiveMode.WRITE)
    ar.write(Type.STRING, "こん", encoding="cp932")
    assert dummy.getvalue() == b"\x04\x82\xb1\x82\xf1"


def test_write_cp936string():
    locale.getpreferredencoding = lambda: "cp936"
    dummy = BytesIO()

    ar = CArchive(dummy, CArchiveMode.WRITE)
    ar.write(Type.STRING, "乗", encoding="cp936")
    assert dummy.getvalue() == b"\x02\x81\x5c"


def test_write_utf16lestring():
    dummy = BytesIO()

    ar = CArchive(dummy, CArchiveMode.WRITE)
    ar.write(Type.STRING, "hello", encoding="utf-16-le")
    assert dummy.getvalue() == b"\xff\xfe\xff\x05h\x00e\x00l\x00l\x00o\x00"


def test_read_asciistring_with_null():
    dummy = BytesIO(b"\x05hello\x00")

    ar = CArchive(dummy, CArchiveMode.READ)
    assert ar.read(Type.STRING) == "hello"


def test_read_string_and_int16():
    dummy = BytesIO(b"\x05hello\xff\xff")

    ar = CArchive(dummy, CArchiveMode.READ)
    assert ar.read(Type.STRING) == "hello"
    assert ar.read(Type.INT16) == -1


def test_read_using_with():
    dummy = BytesIO(b"\x05hello\xff\xff")

    with CArchive(dummy, CArchiveMode.READ) as ar:
        assert ar.read(Type.STRING) == "hello"
        assert ar.read(Type.INT16) == -1


def test_write_file_opend_with_read_mode():
    dummy = BytesIO(b"\x05hello\xff\xff")

    with CArchive(dummy, CArchiveMode.READ) as ar:
        with raises(Exception):
            ar.write(Type.STRING, "hello")


def test_read_file_opend_with_write_mode():
    dummy = BytesIO()

    with CArchive(dummy, CArchiveMode.WRITE) as ar:
        with raises(Exception):
            ar.read(Type.STRING)
