import sys
from .instructions import *
from .register import *
from .pointer import byte, word, dword, qword
from .codepage import CodePage, mkFunction
from .label import label
from .util import *

if sys.maxsize > 2**32:
    ARCH = 64
    else:
        ARCH = 32
