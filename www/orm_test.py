#!/usr/local/bin python3

# -*- coding: utf-8 -*-

__author__ = 'Copper'

import asyncio, orm
from models import User


async def connecDB(loop):
    username = 'root'
    password = '1234'
    dbname = 'awesome'
    await orm.create_pool(loop, user=username, password=password, db=dbname)


async def destoryDB():
    await orm.destory_pool()


# async def test_findAll(loop):
# 	await connecDB(loop)
# 	# userlist = await User.findAll(orderBy='name', limit=2)
# 	userlist = await User.findAll()
# 	print('all users: %s' % userlist)
# 	await destoryDB()

# async def test_findNumber(loop):
# 	await connecDB(loop)
# 	id = await User.findNumber('id')
# 	name = await User.findNumber('name')
# 	print('id: %s; name:%s' % (id, name))
# 	await destoryDB()

# async def test_find(loop):
# 	await connecDB(loop)
# 	user = await User.find('00150167812261268c77eb227a5481cb8c5f39013da2ff9000')
# 	print('user: %s' % user)
# 	await destoryDB()

async def test_insert(loop):
    await connecDB(loop)
    for x in range(100):
        name = 'User_%03d' % x
        email = 'User_%03d@example.com' % x
        user = User(name=name, email=email, passwd='1234567890', image='about:blank')
        await user.save()
    await destoryDB()


# async def test_update(loop):
# 	await connecDB(loop)
# 	user = await User.find('00150167812261268c77eb227a5481cb8c5f39013da2ff9000')
# 	if user is not None:
# 		user.name = 'zona'
# 		user.passwd = 'password'
# 		print('user.name: %s, user.passwd:%s' % (user.name, user.passwd))
# 		await user.update()
# 		print('user update:%s' % user)
# 	await destoryDB()

# async def test_remove(loop):
# 	await connecDB(loop)
# 	user = await User.find('00150167812261268c77eb227a5481cb8c5f39013da2ff9000')
# 	if user is not None:
# 		await user.remove()
# 		print('user remove:%s' % user)
# 	await destoryDB()

loop = asyncio.get_event_loop()

# loop.run_until_complete(test_findAll(loop))
# loop.run_until_complete(test_findNumber(loop))
# loop.run_until_complete(test_find(loop))
loop.run_until_complete(test_insert(loop))
# loop.run_until_complete(test_update(loop))
# loop.run_until_complete(test_remove(loop))

loop.close()

