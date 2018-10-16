#!/usr/local/bin/python
# -*- coding:utf-8 -*-
#CREATOR：ChenHongNan
#QQ：495218034
#CREATE TIME：2017-06-20
#UPDATE TIME：2018-03-15
#更新说明：增加以IP为KEY统计的UV，增加content为KEY的阅读章节数统计
#修复userid中日期格式不为纯数字导致脚本执行出错的问题

import datetime
import sys
import commands
import time
import MySQLdb
import os

#日志文件目录
filedir = '/data/log/'

#脚本提供补跑功能，可以提供参数统计某天的数据，本地需要有该天的日志。
#参数格式为6位数，如：20170620
if len(sys.argv) >= 2:
    days = sys.argv[1:]
    #检查每个日期格式是否正确，原计划删除掉不正确的日期，但是后来觉得怕出错别人没有注意看然后就跑漏了，所以干脆直接退出程序
    for check_argv in days:
        if len(check_argv) != 8 or not check_argv.isdigit():
            print "参数：" + check_argv + " 不符合时间格式 !!!"
            print "示例：" + str(datetime.date.today() + datetime.timedelta(-1)).replace('-','')
            exit()
else:
    days = [str(datetime.date.today() + datetime.timedelta(-1)).replace('-','')]

#日志记录函数
def runlog_write(mess):
    rlf = open(runlog,"a")
    rlf.write(mess+"\n")
    rlf.close()

#MySQL 操作函数
def ggbook_channel(runsql):
    try:
        my2 = MySQLdb.connect(host='localhost',port=3306,user='root',passwd='123456',db='test')
        cursor = my2.cursor()
        cursor.execute(runsql)
        my2.commit()
        return_message = cursor.fetchall()
        for i in return_message:
            print i
        cursor.close()
        my2.close()
    except:
        mess = "[ %s ] MySQL RUN SQL: %s [ ERROR ]" % (time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())),runsql)
        runlog_write(mess)

#开始循环日期
for runday in days:
    #初始化变量，相对于整个项目
    runlog = '/data/shell/ggbook_log_count/log/qudao_count_' + runday + '.log'     #脚本运行日志
    #统计新用户使用的loadfile
    loadfile_QU = '/data/shell/ggbook_log_count/tmp/loadfile_qudao.txt'
    QU = open(loadfile_QU,'w')

    mess='------------------------------------------------ BEGIN[ ' + time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())) + ' ] ------------------------------------------------'
    runlog_write(mess)
    #查找文件存入数组
    files = commands.getstatusoutput("find " + filedir + " -name 'ggbookinf.3g.cn_*_nginx_access.'" + runday + "*.log")[1].split('\n')
    #如果没有文件则退出
    if files == []:
        mess = "日期：" + runday + " 没有文件 ！！！"
        print mess
        runlog_write(mess)
        continue
    #开始循环文件，进行统计
    for run_file in files:
        f = open(run_file,'r')
        all_note = f.readlines()
        for note in all_note:
            #初始化变量，相对于行记录，需要在行操作中初始化
            args_dict = {}        #链接参数组成的字典
            if note.lower().find("windows nt") > -1 or note.lower().find("spider") > -1:
                continue
            note_list = note.replace('"','').split(' ')
            try:
                try:
                    flag = note_list.index('GET') + 1
                except:
                    flag = note_list.index('POST') + 1
            except:
                continue

            #拆分URL,？号切割
            url_group = note_list[flag].split('?')
            ip = note_list[0].split(',')[0]
            #如果没有？则为空。
            if len(url_group) <= 1:
                continue
            else:
                #将参数用&符号分割，变成list
                args_group = url_group[1].split('&')
            for args_note in args_group:
                #将链接参数转换成字典
                if args_note.find('=') > -1:
                    args_dict[args_note.split('=')[0]] = args_note.split('=')[1]
            #渠道推广每日新用户
            if args_dict.get('unionid',False) and args_dict.get('channel',False) and args_dict.get('ggid',False) and str(args_dict['ggid']).isdigit():
                if args_dict['unionid'].find('_' + runday) >= 0 and args_dict.get('a',False) and args_dict['a'] == 'getContent':
                    QU.write(str(runday) + ',' + args_dict['unionid'] + ',' + args_dict['channel'] + ',' + args_dict['ggid'] + '\n')
        f.close()
    QU.close()

    #插入数据库
    #渠道推广每日新用户
    runsql = "LOAD DATA LOCAL INFILE '" + loadfile_QU + "' IGNORE INTO TABLE channel_useractive CHARACTER SET 'utf8' FIELDS TERMINATED BY ',' LINES TERMINATED BY '\\n' (statistical_date,name,channel,ggid);"
    print runsql
    ggbook_channel(runsql)
    mess = "------------------------------------------------ END[ %s ] ------------------------------------------------\n" % (time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())))
    runlog_write(mess)
