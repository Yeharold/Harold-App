#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-14 14:58:35
# @Author  : YeHarold (1174484433@qq.com)
# @Link    : https://github.com/Yeharold

from flask import request,render_template,url_for,redirect
from app import *



@app.route('/index')
def index():

	return "hello flask"


