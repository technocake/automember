#!/usr/bin/python
# coding: utf-8
import requests

from mailgunkey import apikey
import config

def send_message(to, subject, msg):
    return requests.post(
        "https://api.mailgun.net/v3/%s/messages" % config.domain,
        auth=("api", apikey),
        data={"from": "No-Reply <no-reply@%s>" % config.domain,
              "to": to,
              "subject": subject,
              "text": msg})