#!/user/bin/env python
# -*-coding:utf-8 -*-

#Author:songdandan
import xlrd
from xlutils.copy import copy
from utils.public import *

class ExcelVariable:
	'''指定每列内容'''
	StepId=0
	Description=1
	Url=2
	Data=3
	ExpectResult=4
	Result=5

def getStepId():
	'''获取StepId列'''
	return ExcelVariable.StepId

def getDescription():
	'''获取Description列'''
	return ExcelVariable.Description

def getUrl():
	'''获取Url列'''
	return ExcelVariable.Url

def getData():
	'''获取Data列'''
	return ExcelVariable.Data

def getExpectResult():
	'''获取ExpectResult列'''
	return ExcelVariable.ExpectResult

def getResult():
	'''获取Result列'''
	return ExcelVariable.Result

class OperationExcel:
	def getExcel(self):
		'''获取整个excel文件'''
		db=xlrd.open_workbook(data_dir(catalog='data',filename='data.xls'))
		sheet=db.sheet_by_index(0)
		return sheet

	def get_rows(self):
		'''获取excel的行数'''
		return self.getExcel().nrows

	def get_row_cel(self,row,col):
		'''获取单元格内容'''
		return self.getExcel().cell_value(row,col)

	def get_url(self,row):
		'''获取请求地址'''
		return self.get_row_cel(row,getUrl())

	def get_request_data(self,row):
		'''获取请求参数'''
		return self.get_row_cel(row,getData())

	def get_expect_result(self,row):
		'''获取期望结果'''
		return self.get_row_cel(row,getExpectResult())

	def get_result(self,row):
		'''获取实际结果'''
		return  self.get_row_cel(row,getResult())

	def get_stepid(self,row):
		'''获取执行步骤Id'''
		return  self.get_row_cel(row,getStepId())

opera=OperationExcel()
print(opera.get_request_data(1))