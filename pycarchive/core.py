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

    read = 1
    write = 2


class Type(Enum):
    """
    Type
    """

    unknown = 0
    uint16 = 1
    uint32 = 2
    uint64 = 3
    int16 = 4
    int32 = 5
    int64 = 6
    float = 7
    double = 8
    string = 9


class CArchive:
    def __init__(self, file: typing.BinaryIO, mode: CArchiveMode):
        self.mode = mode
        self.file = file

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

    def read(self, type: Type):
        """
        read
        """
        if self.mode != CArchiveMode.read:
            raise Exception("CArchive is not in read mode")

        if type == Type.uint16:
            return int.from_bytes(self.file.read(2), byteorder="little", signed=False)

        if type == Type.uint32:
            return int.from_bytes(self.file.read(4), byteorder="little", signed=False)

        if type == Type.uint64:
            return int.from_bytes(self.file.read(8), byteorder="little", signed=False)

        if type == Type.int16:
            return int.from_bytes(self.file.read(2), byteorder="little", signed=True)

        if type == Type.int32:
            return int.from_bytes(self.file.read(4), byteorder="little", signed=True)

        if type == Type.int64:
            return int.from_bytes(self.file.read(8), byteorder="little", signed=True)

        if type == Type.float:
            return struct.unpack("f", self.file.read(4))[0]

        if type == Type.double:
            return struct.unpack("d", self.file.read(8))[0]

        if type == Type.string:
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

    def write(self, type: Type, value, encoding: str = "utf-16-le"):
        """
        write
        """
        if self.mode != CArchiveMode.write:
            raise Exception("CArchive is not in write mode")

        if type == Type.uint16:
            return self.file.write(value.to_bytes(2, byteorder="little", signed=False))

        if type == Type.uint32:
            return self.file.write(value.to_bytes(4, byteorder="little", signed=False))

        if type == Type.uint64:
            return self.file.write(value.to_bytes(8, byteorder="little", signed=False))

        if type == Type.int16:
            return self.file.write(value.to_bytes(2, byteorder="little", signed=True))

        if type == Type.int32:
            return self.file.write(value.to_bytes(4, byteorder="little", signed=True))

        if type == Type.int64:
            return self.file.write(value.to_bytes(8, byteorder="little", signed=True))

        if type == Type.float:
            return self.file.write(struct.pack("f", value))

        if type == Type.double:
            return self.file.write(struct.pack("d", value))

        if type == Type.string:
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
