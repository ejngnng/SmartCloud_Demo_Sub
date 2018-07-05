#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import time
import threading

aliveUrl = "http://localhost/index.php/mqtt/sub/alive"

hbInterval = 5.0


def heartbeat():
    requests.post(aliveUrl, "time out")
    global t
    t = threading.Timer(hbInterval, heartbeat)
    t.start()


def main():
    t = threading.Timer(hbInterval, heartbeat)
    t.start()


if __name__ == '__main__':
    main()
