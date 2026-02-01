import numpy
import ctypes
import sys
import os

# Carico la lireria libsomme (libsomme.so) che è presente nella cartella di lavoro  ('.')
_libserie = numpy.ctypeslib.load_library('libserie', '.')

# definizoine tipi di input (argtypes) e di output (restypes) per la funzione sum_n di libsomme 
_libserie.fib.argtypes = [ctypes.c_int]
_libserie.fib.restype  = ctypes.c_double

_libserie.fib_ratio.argtypes = [ctypes.c_int]
_libserie.fib_ratio.restype  = ctypes.c_double

# utilizzo di _libsomme.sum_n
# il parametro n va necessariamente convertito in int
def fib(n):
    return _libserie.fib(int(n))
def fib_ratio(n):
    return _libserie.fib_ratio(int(n))

