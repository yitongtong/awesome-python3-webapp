#!/usr/local/bin python3

# -*- coding: utf-8 -*-

__author__ = 'Copper'

'''
开发环境的标准配置
'''

configs = {
	'debug': True,
	'db' : {
		'host' : '127.0.0.1',
		'port' : 3306,
		'user' : 'root',
		'password' : '1234',
		'db' : 'awesome'
	},
	'session' : {
		'secret' : 'Awesome'
	}
}