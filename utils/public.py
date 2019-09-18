#!/user/bin/env python
# -*-coding:utf-8 -*-

#Author:songdandan

import os

def data_dir(catalog=None,filename=None):
	'''查找文件的路径'''
	return os.path.join(os.path.dirname(os.path.dirname(__file__)),catalog,filename)
