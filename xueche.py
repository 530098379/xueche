#-*-encoding:utf-8-*-
import os
import re
import time
import itchat
from itchat.content import TEXT


@itchat.msg_register(TEXT, isGroupChat=True)
def group_text(msg):
	group = itchat.get_chatrooms(update=True)
	from_user = ''
	from_hour = 0
	to_hour = 0
	hour_add = ''
	msg_str = ''
	send_flg = False
	for g in group:
		if g['NickName'] == '科二':#从群中找到指定的群聊
			from_group = g['UserName']
			for menb in g['MemberList']:
				#print(menb['NickName'])
				if menb['NickName'] == '教练':
					#从群成员列表找到用户,只转发他的消息
					from_user = menb['UserName']
					break

			to_group = g['UserName']
			msg_str = msg['Content']

			if msg_str.find('明') != -1 and msg_str.find('早') != -1:
				hour_add = ''
				for tmp in msg_str[0 : msg_str.find('开始')]:
					if tmp.isdigit():
						hour_add += tmp	

				from_hour = int(hour_add)

				hour_add = ''
				for tmp in msg_str[msg_str.find('开始') : msg_str.find('结束')]:
					if tmp.isdigit():
						hour_add += tmp	

				to_hour = int(hour_add)

				if from_hour >= 7 and to_hour <= 12:
					send_flg = True
					msg['Content'] = '10点到11点，xxxx'

			elif msg_str.find('明') > -1 and (msg_str.find('中午') > -1 or msg_str.find('下午') > -1):
				hour_add = ''
				for tmp in msg_str[0 : msg_str.find('开始')]:
					if tmp.isdigit():
						hour_add += tmp	

				from_hour = int(hour_add)

				hour_add = ''
				for tmp in msg_str[msg_str.find('开始') : msg_str.find('结束')]:
					if tmp.isdigit():
						hour_add += tmp	

				to_hour = int(hour_add) + 12

				if from_hour >= 12 and to_hour <= 17:
					send_flg = True
					msg['Content'] = '1点到2点，xxxx'

			if msg['FromUserName'] == from_group:
				if msg['ActualUserName'] == from_user and send_flg:
					itchat.send('%s'%(msg['Content']),to_group)
			#itchat.send('%s'%(msg['Content']),to_group)
			break

if __name__=='__main__':

    #itchat.auto_login(hotReload=True,enableCmdQR=2)
    itchat.auto_login()

    itchat.run()