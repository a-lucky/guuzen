#!/usr/bin/env python

from distutils.core import setup,Extension,os
import string

def cmd1(str):
    return os.popen(str).readlines()[0][:-1]

def cmd2(str):
    return string.split (cmd1(str))

setup(name = "mecab-python",
	version = cmd1("/app/.linuxbrew/bin/mecab-config --version"),
	py_modules=["MeCab"],
	ext_modules = [
		Extension("_MeCab",
			["/app/mecab-python-0.996/MeCab_wrap.cxx",],
			include_dirs=cmd2("/app/.linuxbrew/bin/mecab-config --inc-dir"),
			library_dirs=cmd2("/app/.linuxbrew/bin/mecab-config --libs-only-L"),
			libraries=cmd2("/app/.linuxbrew/bin/mecab-config --libs-only-l"))
			])
