#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

import os
import logging
import time

from logging.handlers import RotatingFileHandler

from .translation import Translation

# Change Accordingly While Deploying To A VPS
APP_ID = "15671595"

API_HASH = "bb8f36f9c39a24c7f8b2acbc7ea8c60a"

BOT_TOKEN = "5559957614:AAEjYLf7h-227OigZaT1SFCq1zK3V4J8PG8"

DB_URI = "mongodb+srv://Dave:Dave@cluster0.nvjotuh.mongodb.net/?retryWrites=true&w=majority"

USER_SESSION = os.environ.get("USER_SESSION")

VERIFY = {}

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            "autofilterbot.txt",
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

start_uptime = time.time()


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
