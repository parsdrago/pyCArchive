"""

library to read/write MFC CArchive files

"""


import locale
import struct
import typing
from enum import Enum


class CArchiveMode(Enum):
    """
    CArchiveMode
    """

    READ = 1
    WRITE = 2


class Type(Enum):
    """
    Type
    """

    UNKNOWN = 0
    UINT16 = 1
    UINT32 = 2
    UINT64 = 3
    INT16 = 4
    INT32 = 5
    INT64 = 6
    FLOAT = 7
    DOUBLE = 8
    STRING = 9


class CArchive:
    """
    CArchive
    """

    def __init__(self, file: typing.BinaryIO, mode: CArchiveMode):
        self.mode = mode
        self.file = file

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

    def read(self, variable_type: Type):
        """
        read
        """
        if self.mode != CArchiveMode.READ:
            raise Exception("CArchive is not in read mode")

        if variable_type == Type.UINT16:
            return int.from_bytes(self.file.read(2), byteorder="little", signed=False)

        if variable_type == Type.UINT32:
            return int.from_bytes(self.file.read(4), byteorder="little", signed=False)

        if variable_type == Type.UINT64:
            return int.from_bytes(self.file.read(8), byteorder="little", signed=False)

        if variable_type == Type.INT16:
            return int.from_bytes(self.file.read(2), byteorder="little", signed=True)

        if variable_type == Type.INT32:
            return int.from_bytes(self.file.read(4), byteorder="little", signed=True)

        if variable_type == Type.INT64:
            return int.from_bytes(self.file.read(8), byteorder="little", signed=True)

        if variable_type == Type.FLOAT:
            return struct.unpack("f", self.file.read(4))[0]

        if variable_type == Type.DOUBLE:
            return struct.unpack("d", self.file.read(8))[0]

        if variable_type == Type.STRING:
            count, encoding = self.__read_string_header()
            return self.file.read(count).decode(encoding)

        raise Exception("Unknown type")

    def __read_string_header(self):
        count = self.file.read(1)
        if count != b"\xff":
            return (
                int.from_bytes(count, byteorder="little"),
                locale.getpreferredencoding(),
            )

        count = self.file.read(2)

        if count != b"\xfe\xff":
            if count != b"\xff\xff":
                return (
                    int.from_bytes(count, byteorder="little"),
                    locale.getpreferredencoding(),
                )

            count = self.file.read(4)
            return (
                int.from_bytes(count, byteorder="little"),
                locale.getpreferredencoding(),
            )

        count = self.file.read(1)
        if count != b"\xff":
            return int.from_bytes(count, byteorder="little") * 2, "utf-16-le"

        count = self.file.read(2)
        if count != b"\xff\xff":
            return int.from_bytes(count, byteorder="little") * 2, "utf-16-le"

        count = self.file.read(4)
        return int.from_bytes(count, byteorder="little") * 2, "utf-16-le"

    def write(self, variable_type: Type, value, encoding: str = "utf-16-le"):
        """
        write
        """
        if self.mode != CArchiveMode.WRITE:
            raise Exception("CArchive is not in write mode")

        if variable_type == Type.UINT16:
            return self.file.write(value.to_bytes(2, byteorder="little", signed=False))

        if variable_type == Type.UINT32:
            return self.file.write(value.to_bytes(4, byteorder="little", signed=False))

        if variable_type == Type.UINT64:
            return self.file.write(value.to_bytes(8, byteorder="little", signed=False))

        if variable_type == Type.INT16:
            return self.file.write(value.to_bytes(2, byteorder="little", signed=True))

        if variable_type == Type.INT32:
            return self.file.write(value.to_bytes(4, byteorder="little", signed=True))

        if variable_type == Type.INT64:
            return self.file.write(value.to_bytes(8, byteorder="little", signed=True))

        if variable_type == Type.FLOAT:
            return self.file.write(struct.pack("f", value))

        if variable_type == Type.DOUBLE:
            return self.file.write(struct.pack("d", value))

        if variable_type == Type.STRING:
            count = len(value)
            text = value.encode(encoding)
            if encoding in ["utf-16-le", "utf-16le"]:
                self.file.write(b"\xff\xfe\xff")
            else:
                count = len(text)
            if count < 0xFF:
                self.file.write(count.to_bytes(1, byteorder="little"))
            elif count < 0xFFFF:
                self.file.write(b"\xff")
                self.file.write(count.to_bytes(2, byteorder="little"))
            elif count < 0xFFFFFF:
                self.file.write(b"\xff\xff")
                self.file.write(count.to_bytes(4, byteorder="little"))
            else:
                self.file.write(b"\xff\xff\xff")
                self.file.write(count.to_bytes(4, byteorder="little"))

            return self.file.write(text)

        raise Exception("Unknown type")
