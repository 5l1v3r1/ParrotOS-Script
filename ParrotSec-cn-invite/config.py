#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask
from Secrets import SECRETS

app = Flask(__name__)

app.config['SECRET_KEY'] = SECRETS['keys']['secret_key']

app.config['DEBUG'] = False

