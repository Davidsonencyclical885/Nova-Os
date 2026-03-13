"""
Nova OS
Author: Tanju Aksit
Copyright (c) 2026 Tanju Aksit

This source code is licensed under the Nova OS Author Credit License.
"""


import json
import os

BASE = os.path.dirname(__file__)


def load_json(path):

    if not os.path.exists(path):
        return {}

    try:
        with open(path, "r", encoding="utf8") as f:
            content = f.read().strip()
            if not content:
                return {}
            return json.loads(content)
    except:
        return {}


public_path = os.path.join(BASE, "public")
private_path = os.path.join(BASE, "private")

config = {}


if os.path.exists(public_path):

    for file in os.listdir(public_path):

        if file.endswith(".json"):
            config.update(load_json(os.path.join(public_path, file)))


if os.path.exists(private_path):

    for file in os.listdir(private_path):

        if file.endswith(".json"):
            config.update(load_json(os.path.join(private_path, file)))