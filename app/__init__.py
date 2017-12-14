#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-14 15:31:01
# @Author  : YeHarold (1174484433@qq.com)
# @Link    : https://github.com/Yeharold

from flask import Flask



app = Flask(__name__)
app.secret_key = "fhakfhakfhkd"


import models
import views
