# coding=utf-8
from distutils.core import setup
import py2exe
import os
import sys

includes = ['exm.sections.*', 'exm.utils.*']
# 要包含的其它库文件

options = {"py2exe":
    {
        "compressed": 1,  # 压缩
        "optimize": 2,
        "ascii": 1,
        "includes": includes,
        "bundle_files": 3  # 设置为1，将所有文件打包成一个exe文件
    }
}
setup(
    options=options,
    zipfile=None,  # 不生成library.zip文件
    console=[{
        "script": "exm.py"
        # "icon_resources": [] #源文件，程序图标
    }]
)
