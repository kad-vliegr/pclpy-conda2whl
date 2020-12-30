import os
import shutil
from glob import iglob as glob

SRC_DIR = './env/Library/bin'
DST_DIR = './pclpy_dependencies/bin'

patterns = [
    'pcl_*.dll',

    'boost_*.dll',
    'bzip2.dll',
    'comerr64.dll',
    'flann*.dll',
    'gssapi64.dll',
    'hdf5*.dll',
    'k5sprt64.dll',
    'kfwlogon.dll',
    'krb5_64.dll',
    'krbcc64.dll',
    'las.dll',
    'laszip*.dll',
    'leashw64.dll',
    'libblas.dll',
    'libbz2.dll',
    'libcblas.dll',
    'libcurl.dll',
    'libimalloc.dll',
    'libio*.dll',
    'liblapack.dll',
    'liblz4.dll',
    'liblzma.dll',
    'libssh2.dll',
    'libzstd.dll',

    'mkl_*.dll',
    'qhull*.dll',

    'tcl86t.dll',
    'tk86t.dll'
    'xpprof64.dll',
    'zstd.dll',
    'zlib.dll'
]

for pattern in patterns:
    for path in glob(os.path.join(SRC_DIR, pattern)):
        print('{} -> {}'.format(path, DST_DIR))
        shutil.copy(path, DST_DIR)
