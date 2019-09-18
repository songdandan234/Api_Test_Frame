#!/user/bin/env python
# -*-coding:utf-8 -*-

#Author:songdandan

import json
from utils.public import *

class OperationJson:
	def getReadJson(self):
		with open(data_dir(catalog='data',filename='requestData.json'),encoding='utf-8') as f:
			return json.load(f)

	def get_json_data(self,keyword):
		return self.getReadJson()[keyword]

opera=OperationJson()
print(opera.getReadJson())