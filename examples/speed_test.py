import timeit

import cProfile


s = """
from SiLibUSB import SiUSBDevice

sidev = SiUSBDevice()

def FastBlockRead(bytes):
    sidev.FastBlockRead(bytes)

def FastBlockWrite(bytes):
    sidev.FastBlockWrite('\\x00'*bytes)
"""


for i in range(1, 64):
    size = i * (2**10)
    repeat = 5
    read = timeit.timeit(stmt="FastBlockRead( " + str(size) + " )", setup=s, number=repeat)
    write = timeit.timeit(stmt="FastBlockWrite( " + str(size) + " )", setup=s, number=repeat)
    print("size: {}kB; read : {}MB/s; write : {}MB/s".format(float(size) / 1024.0, float(size * repeat) / (1024.0 * 1024.0) / read, float(size * repeat) / (1024.0 * 1024.0) / write))


"""
import pstats
from SiLibUSB import SiUSBDevice

sidev = SiUSBDevice()


def prof():
    for i in range(1, 128):
        sidev.ReadExternal(0x0000, 1024 * 32)
        # sidev.FastBlockWrite( range(0, 1)*1024*32 )


# cProfile.run('prof()')
cProfile.run('prof()', '/tmp/fooprof')

p = pstats.Stats('/tmp/fooprof')
p.sort_stats('time').print_stats(20)

p.sort_stats('cumulative').print_stats(10)
"""
