#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5826620184:AAF9pb2yd-ptpiHuYXz---W9SWRnAK2YG4I")
    # The Telegram API things
    API_ID = int(os.environ.get("API_ID", 16393106))
    API_HASH = os.environ.get("API_HASH", "061fbf1aff7eecf2edb8434ddbab7a7d")
    AUTH_USERS = os.environ.get("OWNER", "5295973607 611969501")

