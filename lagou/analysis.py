'''
Function:
	分析拉勾网招聘数据
作者:
	Charles
公众号:
	Charles的皮卡丘
'''
import os
import pickle
from pyecharts import Bar
from pyecharts import Pie
from pyecharts import Funnel


# 柱状图(2维)
def DrawBar(title, data, savepath='./results'):
	if not os.path.exists(savepath):
		os.mkdir(savepath)
	bar = Bar(title)
	attrs = [i for i, j in data.items()]
	values = [j for i, j in data.items()]
	bar.add('', attrs, values, mark_point=["min", "max"], is_convert=True)
	bar.render(os.path.join(savepath, '%s.html' % title))


# 饼图
def DrawPie(title, data, savepath='./results'):
	if not os.path.exists(savepath):
		os.mkdir(savepath)
	pie = Pie(title, title_pos='center')
	attrs = [i for i, j in data.items()]
	values = [j for i, j in data.items()]
	pie.add('', attrs, values, is_label_show=True, radius=[30, 50], rosetype="radius", legend_pos="left", legend_orient="vertical")
	pie.render(os.path.join(savepath, '%s.html' % title))


# 漏斗图
def DrawFunnel(title, data, savepath='./results'):
	if not os.path.exists(savepath):
		os.mkdir(savepath)
	funnel = Funnel(title, title_pos='center')
	attrs = [i for i, j in data.items()]
	values = [j for i, j in data.items()]
	funnel.add("", attrs, values, is_label_show=True, label_pos="inside", label_text_color="#fff", legend_pos="left", legend_orient="vertical")
	funnel.render(os.path.join(savepath, '%s.html' % title))


if __name__ == '__main__':
	with open('info.pkl', 'rb') as f:
		data = pickle.load(f)
	'''
	salaryDict = {}
	for key, value in data.items():
		average = 0
		num = 0
		for v in value:
			num += 1
			salary = v[-1]
			salary = salary.split('-')
			try:
				tmp = (float(salary[0].replace('k', '').replace('K', '')) + float(salary[0].replace('k', '').replace('K', ''))) / 2
			except:
				continue
			average += tmp
		salaryDict[key] = average / num
	DrawBar(title='部分城市Python相关岗位平均薪资柱状图', data=salaryDict, savepath='./results')
	'''
	'''
	eduDict = {}
	for key, value in data.items():
		for v in value:
			edu = v[-3]
			if edu in eduDict:
				eduDict[edu] += 1
			else:
				eduDict[edu] = 1
	DrawPie(title='部分城市Python相关岗位应聘学历要求', data=eduDict, savepath='./results')
	'''
	'''
	companySizeDict = {}
	for key, value in data.items():
		for v in value:
			companySize = v[5]
			if companySize in companySizeDict:
				companySizeDict[companySize] += 1
			else:
				companySizeDict[companySize] = 1
	DrawFunnel(title='部分城市招聘Python相关岗位的公司规模', data=companySizeDict, savepath='./results')
	'''
	jobNatureDict = {}
	for key, value in data.items():
		for v in value:
			jobNature = v[6]
			if jobNature in jobNatureDict:
				jobNatureDict[jobNature] += 1
			else:
				jobNatureDict[jobNature] = 1
	DrawBar(title='部分城市Python相关岗位工作性质', data=jobNatureDict, savepath='./results')

	industryFieldDict = {}
	for key, value in data.items():
		for v in value:
			industryField = v[4]
			try:
				industryFields = industryField.split(',')
			except:
				continue
			if len(industryFields) == 1:
				industryFields = industryField.split(' ')
			if len(industryFields) == 1:
				industryFields = industryField.split('、')
			for industryField in industryFields:
				industryField = industryField.strip(' ')
				if industryField in industryFieldDict:
					industryFieldDict[industryField] += 1
				else:
					industryFieldDict[industryField] = 1
	DrawPie(title='部分城市Python相关岗位工作领域', data=industryFieldDict, savepath='./results')