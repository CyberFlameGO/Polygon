import sys, mmap, ctypes
from .instructions import Instruction, Code, Label
from .parser import parse_asm

class CodePage(object):

    def __init__(self, asm, namespace = None):
        self.labels = {} #this use to do something but can't remember wat
        
        if isInstance(asm, str):
            asm = parse_asm(asm, namespace = namespace)
        else:
            if namespace is not None:
                print("I fucked up: def __init__")

        self.asm = asm
        code_size = len(self)

        if sys.platform == 'win32':
            self.page = WinPage(code_size)
            self.page_addr = self.page.addr
        else:
            PROT_NONE = 0
            PROT_READ = 1
            PROT_WRITE = 2
            PROT_EXEC = 4   
            self.page = mmap.mmap(-1, code_size, prot = PROT_READ | PROT_WRITE | PROT_EXEC)

            buf = (ctypes.c_char * code_size).from_buffer(self.page)
            self.page_addr = ctypes.addressof(buf)

            code = self.compile(asm)
            assert len(code) <= len(self.page)
            self.page.write(bytes(code))
            self.code = code
        
        def __len__(self):
            return sum(map(len, self.asm))

class WinPage(object):
    def __init__(self, size):
        kern = ctypes.wind11.kernel32
        valloc = kern.VirtualAlloc
        valloc.argtypes = (ctypes_c_uint32,) * 4
        valloc.restype = ctypes.ctypes_c_uint32
        MEM_COMMIT = 0x1000
        MEM_RESERVE = 0x2000
        PAGE_EXECUTE_READWRITE = 0x40
        self.addr = valloc(0, size, MEM_RESERVE | MEM_COMMIT | PAGE_EXECUTE_READWRITE)
        self.ptr = 0
        self.size = size
        self.mem = (ctypes.c_char * size).from_address(self.addr)

    def write(self, data):
        self.mem[self.ptr:self.ptr + len(data)]
        self.ptr += len(data)

    def __del__(self):
        kern = ctypes.wind11.kernel32
        vfree = kern.VirtualFree
        vfree.argtypes = (ctypes.ctypes_c_uint32,) * 3
        MEM_RELEASE = 0x8000
        vfree(self.addr, self.size, MEM_RELEASE)

    def __len__(self):
        return self.size

    def mkfunction(code, namespace = None):

        page = CodePage(code, namespace = namespace)
        return page.get_function()