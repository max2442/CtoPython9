def print():
    from cffi import FFI
    ffi = FFI()

    ffi.cdef("""
        static void Main();
    """)
    C = ffi.dlopen(None)
    C.Main()