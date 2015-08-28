# cherrypy as http server
# -*- coding:utf-8 -*-
import cherrypy
import werobot

class werobot_run(host,port):
	robot = werobot.WeRoBot(token='testrobot', enable_session=True)

	@robot.subscribe
	def subscribe(message):
    	return '欢迎关注本公众号！'

	@robot.handler
	def echo(message):
    	return '我是WeRoBot机器人'

	#robot.run(server='cherrypy',host='0.0.0.0',port=80)

def raw_wsgi_app('0.0.0.0','80'):

	werobot_run(host,port)

cherrypy.tree.graft(raw_wsgi_app, '/weixin')