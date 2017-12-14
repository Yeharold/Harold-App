#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-14 14:58:48
# @Author  : YeHarold (1174484433@qq.com)
# @Link    : https://github.com/Yeharold

import sqlite3 as db 



conn = db.connect("app/database/app.db",check_same_thread = False)
c = conn.cursor()