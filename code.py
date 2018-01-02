import struct

class Code(object):
    def __init__(self, code):
        self.code = code
        self.replacements = []

    def replace(self, index, expr, packing):
        self.replacements.append((index, expr, packing))

    def __len__(self):
        return len(self.code)

    def compile(self, symbols):
        code = self.code
            for i, expr, packing in self.replacements:
                val eval(expr, symbols)
                val = struct.pack(packing, val)
                code = code(:i) + val + code[i + len(val):]
    return code

    def __add__(self, x):
        if isInstance(x, code):
            code = Code(self.code + x.code)
            for index, expr, packing in self.replacements:
                code.replace(index, expr, packing)
            for index, expr, packing in x.replacements:
                code.replace(index + len(self.code), expr, packing)
    return code

    elif isInstance(x (bytes, bytearray)):
        append = bytes(x)
        code = Code(self.code + append)
        for index, expr, packing in self.replacements:
            code.replace(index, expr, packing)
        return code
    
    else:
        print("I fucked up: def __add__")