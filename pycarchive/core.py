"""

library to read/write MFC CArchive files

"""


from enum import Enum
import typing


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


class CArchive:
    def __init__(self, file: typing.BinaryIO, mode: CArchiveMode):
        self.mode = mode
        self.file = file

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

    def read(self, type: Type) -> bytes:
        """
        read
        """
        if self.mode != CArchiveMode.read:
            raise Exception('CArchive is not in read mode')


        if type == Type.uint16:
            return int.from_bytes(self.file.read(2), byteorder='little', signed=False)

        raise Exception('Unknown type')