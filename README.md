# pyCArchive
python library to read/write [MFC CArchive](https://docs.microsoft.com/en-us/cpp/mfc/serialization-in-mfc?view=msvc-170) serialized file

## SAMPLE

``` python
from pycarchive import CArchive, CArchiveMode, Type

with open(path, "wb") as f:
    with CArchive(dummy, CArchiveMode.write) as ar:
        ar.write(Type.string, "hello")
        ar.write(Type.int16, -1)

with open(path, "rb") as f:
    with CArchive(dummy, CArchiveMode.read) as ar:
        ar.read(Type.string)
        ar.read(Type.int16)

```
