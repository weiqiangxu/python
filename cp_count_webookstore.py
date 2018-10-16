#!/usr/local/bin/python
# -*- coding:utf-8 -*-
#CREATOR：ChenHongNan
#QQ：495218034
#CREATE TIME：2017-10-25

import datetime
import sys
import commands
import time
import MySQLdb

#日志文件目录
filedir='/data/log/'
mysqlhost='localhost'
mysqlport=3306
mysqluser='root'
mysqlpasswd='123456'
mydb='advertise_user'
# project=['webookstore']
exclude_url=['/index.php?m=Home&c=Recharge&a=getAjaxHtml&tmp=wx',
'/index.php?m=Home&c=User&a=verify',
'/index.php?m=Home&c=User&a=ajaxchk',
'/index.php?m=Home&c=User&a=sendSMS',
'/index.php?m=Home&c=User&a=otloginIn',
'/index.php?m=Home&c=User&a=loginIn',
'/index.php?m=Wexin&signature=',
'/index.php?m=Home&c=User&a=otlogin']


qudao = []
qudao_sql="SELECT channel_name FROM wechat_feedback"
myc=MySQLdb.connect(host=mysqlhost,port=mysqlport,user=mysqluser,passwd=mysqlpasswd,db=mydb)
cursor=myc.cursor()
cursor.execute(qudao_sql)
qudao_group=cursor.fetchall()
myc.close()
for i in qudao_group:
    qudao.append(i[0])

#脚本提供补跑功能，可以提供参数统计某天的数据，本地需要有该天的日志。
#参数格式为6位数，如：20170620
if len(sys.argv) >= 2:
    days=sys.argv[1:]
    #检查每个日期格式是否正确，原计划删除掉不正确的日期，但是后来觉得怕出错别人没有注意看然后就跑漏了，所以干脆直接退出程序
    for check_argv in days:
        if len(check_argv) != 8 or not check_argv.isdigit():
            print "参数：" + check_argv + " 不符合时间格式 !!!"
            print "示例：" + str(datetime.date.today() + datetime.timedelta(-1)).replace('-','')
            exit()
else:
    days=[str(datetime.date.today() + datetime.timedelta(-1)).replace('-','')]

#日志记录函数
def runlog_write(mess):
    try:
        rlf=open(runlog,"a")
    except:
        rlf=open(runlog,"w")
    rlf.write(mess+"\n")
    rlf.close()

#MySQL 操作函数
def mysql_insert(runsql):
    try:
        myc=MySQLdb.connect(host=mysqlhost,port=mysqlport,user=mysqluser,passwd=mysqlpasswd,db=mydb)
        cursor=myc.cursor()
        cursor.execute(runsql)
        myc.commit()
        return_message=cursor.fetchall()
        for i in return_message:
            print i
        cursor.close()
        myc.close()
    except:
        mess="[ %s ] MySQL RUN SQL: %s [ ERROR ]" % (time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())),runsql)
        runlog_write(mess)

#开始循环日期
for runday in days:
    #初始化变量，相对于整个项目
    runlog='/data/shell/cp_count/log/webookstore_runlog_' + runday + '.log'     #脚本运行日志
    loadfile='/data/shell/cp_count/tmp/webookstore_loadfile_' + runday + '.txt' #统计二次留存率使用的文件
    qudaopv={}              #渠道对应日期的PV统计。
    PV={}                   #总PV
    ckuid_group={}          #存放COOKIE列表
    UV={}                   #总UV
    new_user={}             #新增用户数
    indexpv={}              #首页PV
    index_ckuid=[]          #统计首页UV用的列表
    indexuv={}              #首页UV
    bookid_group={}         #书籍统计使用的字典
    bookid_ckuid=[]         #书籍UV统计使用的列表
    bookiduv={}             #书籍UV
    allchannel_group={}     #总渠道统计使用的字典
    allchannel_ckuid=[]     #总渠道UV统计使用的列表
    allchanneluv={}         #总渠道UV
    channel_group={}        #来源渠道统计使用的字典
    channel_ckuid=[]        #来源渠道UV统计使用的列表
    channeluv={}            #来源渠道UV
    load_uniq=[]            #loadfile去重
    channel_bid_uid={}      #统计推广链接
    channel_uid=[]          #推广链接UID去重
    channel_dckuid={}       #推广链接UV
    officialaccounts_group=[] #存放officialaccounts列表
    mess='------------------------------------------------ BEGIN[ ' + time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())) + ' ] ------------------------------------------------'
    runlog_write(mess)

    #初始化渠道PV统计（对应日期的统计）
    for i in qudao:
        qudaopv[i]={}

    lf=open(loadfile,'w')
    #查找文件存入数组
    files=commands.getstatusoutput("find " + filedir + " -name 'webookstore.xuan.access_*'" + runday + "*.log")[1].split('\n')
    #如果没有文件则退出
    if files == ['']:
        mess = "项目：webookstore. 日期：" + runday + " 没有文件 ！！！"
        print mess
        runlog_write(mess)
        continue
    #开始循环文件
    for run_file in files:
        f=open(run_file,'r')
        for note in f.readlines():
            #初始化变量，相对于行记录，需要在行操作中初始化
            args_dict={}        #链接参数组成的字典
            #只要状态为200和302的记录，其他跳过
            status=note.find('"status=200"')
            if status < 0:
                continue
            #去掉 Windows NT 和 Spider
            if note.lower().find("windows nt") > -1 or note.lower().find("spider") > -1:
                continue
            note_split=note.split("\"")
            url_note=note_split[1].split()[1]
            #去掉不统计的链接
            for exurl in exclude_url:
                if url_note.find(exurl) > -1:
                    continue
            #拆分URL,？号切割
            url_group=note_split[1].split('?')
            #如果没有？则为空。
            if len(url_group) <= 1:
                args_group=[]
            else:
                #将参数用&符号分割，变成list
                args_group=url_group[1].split('&')
            for args_note in args_group:
                #将链接参数转换成字典
                if args_note.find('=') > -1:
                    args_dict[args_note.split('=')[0]]=args_note.split('=')[1]
            dckuid='-'
            dchannel='-'
            officialaccounts='0'
            for row_note in note_split:
                #找出dckuid
                if row_note.find("dckuid=") > -1:
                    dckuid=row_note.split("=")[1]
                #找出dchannel
                if args_dict.get('channel',False):
                    dchannel=args_dict['channel']
                if args_dict.get('officialaccounts',False) and str(args_dict['officialaccounts']).isdigit():
                    officialaccounts=args_dict['officialaccounts']
            if officialaccounts == '0':
                continue
            if officialaccounts not in officialaccounts_group:
                officialaccounts_group.append(officialaccounts)
            #总PV
            PV[officialaccounts] = PV.get(officialaccounts,0) + 1
            #统计总UV
            if not ckuid_group.get(officialaccounts + '_' + dckuid,False):
                UV[officialaccounts] = UV.get(officialaccounts,0) + 1
                #统计新用户
                if dckuid != '-':
                    if dckuid.split('_')[1] == runday:
                        new_user[officialaccounts] = new_user.get(officialaccounts,0) + 1
            ckuid_group[officialaccounts + '_' + dckuid]=ckuid_group.get(officialaccounts + '_' + dckuid,0) + 1
            #统计首页PV和UV
            request_url=note_split[1].split()
            if request_url[1].find("m=Home&c=Index&a=index") > -1:
                indexpv[officialaccounts] = indexpv.get(officialaccounts,0) + 1
                if officialaccounts + '_' + dckuid not in index_ckuid and dckuid != '-':
                    indexuv[officialaccounts] = indexuv.get(officialaccounts,0) + 1
                    index_ckuid.append(officialaccounts + '_' + dckuid)
            #统计个别渠道天数的PV（2017-10-09添加的统计）
            if dchannel in qudaopv:
                qudaopv[dchannel][dckuid.split('_')[1]] = qudaopv[dchannel].get(dckuid.split('_')[1],0) + 1
            #统计总渠道PV 和 UV
            if dchannel != '-' and dchannel != '':
                allchannel_group[officialaccounts + '_' + dchannel] = allchannel_group.get(officialaccounts + '_' + dchannel,0) + 1
                allchannel_cookie=officialaccounts + '_' + dchannel + dckuid
                if allchannel_cookie not in allchannel_ckuid:
                    allchanneluv[officialaccounts + '_' + dchannel] = allchanneluv.get(officialaccounts + '_' + dchannel,0) + 1
                    if dckuid != '-':
                        lf.write(runday + ',' + dckuid + ',' + dchannel + '\n')
                    allchannel_ckuid.append(allchannel_cookie)
            #统计书籍 PV 和 UV,如果参数中包含bookid字段。
            if args_dict.get('bookid',False):
                #bookid PV
                bookid_group[officialaccounts + '_' + args_dict['bookid']]=bookid_group.get(officialaccounts + '_' + args_dict['bookid'],0) + 1
                #去掉dckuid为空的记录
                if dckuid != '-':
                    #使用bookid + cookie 来确认是否为书籍的唯一COOKIE
                    bookid_cookie=officialaccounts + '_' + args_dict['bookid'] + '_' + dckuid
                    if bookid_cookie not in bookid_ckuid:
                        bookid_ckuid.append(bookid_cookie)
                        #统计bookid UV
                        bookiduv[officialaccounts + '_' + args_dict['bookid']]=bookiduv.get(officialaccounts + '_' + args_dict['bookid'],0) + 1
            #统计渠道 PV 和 UV ,如果参数中包含channel_name字段。
            if args_dict.get('channel',False):
                #channel PV
                channel_group[officialaccounts + '_' + args_dict['channel']]=channel_group.get(officialaccounts + '_' + args_dict['channel'],0) + 1
                #去掉dckuid为空的记录
                if dckuid != '-':
                    #使用channel_name + cookie 来确认是否为渠道的唯一COOKIE
                    channel_cookie=args_dict['channel'] + '_' + dckuid
                    if channel_cookie not in channel_ckuid:
                        channel_ckuid.append(channel_cookie)
                        #统计bookid UV
                        channeluv[officialaccounts + '_' + args_dict['channel']]=channeluv.get(officialaccounts + '_' + args_dict['channel'],0) + 1
                    if args_dict.get('bookid',False) and args_dict.get('chapterid',False):
                        #channel_book_url = 'http://book.3g.cn/' + pjt + '/' + args_dict['bookid'] + '/' + args_dict['chapterid'] + '/' + args_dict['channel'] + '.html'
                        channel_book_url = url_note
                        channel_book_uid = args_dict['channel'] + '_' + args_dict['bookid'] + '_' + args_dict['chapterid'] + '_' + dckuid
                        channel_bid_uid[channel_book_url] = channel_bid_uid.get(channel_book_url,0) + 1
                        if channel_book_uid not in channel_uid:
                            channel_dckuid[channel_book_url] = channel_dckuid.get(channel_book_url,0) + 1
                            channel_uid.append(channel_book_uid)
        f.close()
    #统计单页面PV
    #单页面UV的统计公式：cookie为空（-）和新用户都是今天刚来的，因为今天之前来过的话，今天访问就会产生COOKIE
    #那cookie为空的总数减去新用户得到的数量就是今天来的却只点了一次的用户，然后再加上今天之前的那些cookie只点了一次的总数，就是总的单页面UV
    for officialaccounts in officialaccounts_group:
        pjt=''
        if officialaccounts == '2':
           pjt = 'ggbook'
        elif officialaccounts == '3':
           pjt = 'wx'
        elif officialaccounts == '4':
           pjt = 'wxbook'
        elif officialaccounts == '5':
           pjt = 'ms'
        elif officialaccounts == '6':
           pjt = 'tts'
        elif officialaccounts == '7':
           pjt = 'wys'
        elif officialaccounts == '1':
           pjt = 'diversionbook'
        else:
           pjt = 'diversionbook'

        singleuv=0
        for scookie in ckuid_group:
            if scookie != officialaccounts + '_' + '-':
                if scookie.split('_')[2] != runday and ckuid_group[scookie] == 1 and scookie.split('_')[0] == officialaccounts:
                    singleuv+=1
        #2017-06-26说统计不正常，去掉所有dckuid为空的记录
        #singleuv=singleuv + ckuid_group.get('-',0) - new_user
        #UV要加上那些来过却没有产生cookie的UV
        #UV=UV + ckuid_group.get('-',0) - new_user - 1
        #print "首页PV,首页UV，总PV，总UV，新用户，单页面UV"
        #runsql="call proc_wechat_today_tongji(" + str(indexpv) + ',' + str(indexuv) + ',' + str(PV) + ',' + str(UV) + ',' + str(ckuid_group.get('-',0)) + ',' + str(singleuv) + ",'" + pjt + "')"
        runsql="call proc_wechat_today_tongji_new(" + str(indexpv.get(officialaccounts,0)) + ',' + str(indexuv.get(officialaccounts,0)) + ',' + str(PV.get(officialaccounts,0)) + ',' + str(UV.get(officialaccounts,0)) + ',' + str(new_user.get(officialaccounts,0)) + ',' + str(singleuv) + ",'" + pjt + "')"
        # print runsql
        mysql_insert(runsql)

        #print "书籍统计"
        for book_id in bookid_group:
            if book_id.split('_')[0] == officialaccounts:
                runsql="call proc_wechat_book_log_tongji_new(" + str(book_id.split('_')[1]) + ',' + str(bookid_group[book_id]) + ',' + str(bookiduv.get(book_id,1)) + ",'" + pjt + "')"
                # print runsql
                mysql_insert(runsql)

        #print "渠道统计"
        for channel in allchannel_group:
            if channel.split('_')[0] == officialaccounts:
                runsql='call proc_wechat_channel_link_tongji_new("' + str(channel.split('_')[1]) + '",' + str(channel_group.get(channel,0)) + ',' + str(channeluv.get(channel,0)) + ',' + str(allchannel_group.get(channel,0)) + ',' + str(allchanneluv.get(channel,0)) + ",'" + pjt + "')"
                # print runsql
                mysql_insert(runsql)
    #print "渠道推广链接统计"
    for channelurl in channel_bid_uid:
        runsql='call proc_wechat_channel_link("' + channelurl + '",' + str(channel_bid_uid.get(channelurl,0)) + ',' + str(channel_dckuid.get(channelurl,0)) + ')'
        # print runsql
        mysql_insert(runsql)
    #浩荣说这玩意不用了，统计还在统，就是没有插入库，如果脚本有慢的情况，可以考虑把这个统计去掉，为避免后期需要，我这里保留统计。
    #runsql="LOAD DATA LOCAL INFILE '" + loadfile + "' INTO TABLE wechat_channel_user character set 'utf8' FIELDS TERMINATED BY ',' LINES TERMINATED BY '\\n';"
    #print runsql
    #mysql_insert(runsql)
    #渠道对应日期的PV统计
    for i in qudaopv:
        for a in qudaopv[i]:
            runsql='call proc_wechat_user_feedback("' + i + '","' + a + '",' + str(qudaopv[i].get(a,0)) + ')'
            # print runsql
            mysql_insert(runsql)
    #runsql='call proc_wechat_user_feedback_tongji();'
    #print runsql
    #mysql_insert(runsql)
    mess="------------------------------------------------ END[ %s ] ------------------------------------------------\n" % (time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())))
    runlog_write(mess)
    lf.close()
