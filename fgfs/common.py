# -*- coding: utf-8 -*-

import os, tempfile

def mktmpfifos(filenames):
    tmpdir = tempfile.mkdtemp()
    filenames = [os.path.join(tmpdir, f) for f in filenames]
    for f in filenames:
        os.mkfifo(f)
    return filena
    mes

