#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8212010986:AAGeDz9VOqjD9-up_1AQ6dwCEKh-csq136s")
    API_ID = int(os.environ.get("API_ID", "27400172"))
    API_HASH = os.environ.get("API_HASH", "56d0a75c5f9a9de6beb5452aa63c2d36")
    AUTH_USERS = os.environ.get("AUTH_USERS", "7540570087")
