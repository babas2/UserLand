# Copyright (C) 2020 
# Licensed under the GPL-3.0 License;
# you may not use this file except in compliance with the License.

# UserLand - by BABAŞ #

from . import LANGUAGE, LOGS, bot, PLUGIN_CHANNEL_ID
from json import loads, JSONDecodeError
from os import path, remove
from telethon.tl.types import InputMessagesFilterDocument

pchannel = bot.get_entity(PLUGIN_CHANNEL_ID)
LOGS.info("Dil faylı yüklenir...")
LANGUAGE_JSON = None

for dil in bot.iter_messages(pchannel, filter=InputMessagesFilterDocument):
    if ((len(dil.file.name.split(".")) >= 2) and (dil.file.name.split(".")[1] == "TGjson")):
        if path.isfile(f"./userbot/language/{dil.file.name}"):
            try:
                LANGUAGE_JSON = loads(open(f"./userbot/language/{dil.file.name}", "r").read())
            except JSONDecodeError:
                dil.delete()
                remove(f"./userbot/language/{dil.file.name}")

                if path.isfile("./userbot/language/AZ.TGjson"):
                    LOGS.warn("Varsayılan dil faylı işledilir...")
                    LANGUAGE_JSON = loads(open(f"./userbot/language/AZ.TGjson", "r").read())
                else:
                    raise Exception("Dil faylı sefdir.")
        else:
            try:
                DOSYA = dil.download_media(file="./userbot/language/")
                LANGUAGE_JSON = loads(open(DOSYA, "r").read())
            except JSONDecodeError:
                dil.delete()
                if path.isfile("./userbot/language/AZ.TGjson"):
                    LOGS.warn("Varsayılan dil faylı işledilir...")
                    LANGUAGE_JSON = loads(open(f"./userbot/language/AZ.TGjson", "r").read())
                else:
                    raise Exception("Dil faylı sefdir.")
        break

if LANGUAGE_JSON == None:
    if path.isfile(f"./userbot/language/{LANGUAGE}.TGjson"):
        try:
            LANGUAGE_JSON = loads(open(f"./userbot/language/{LANGUAGE}.TGjson", "r").read())
        except JSONDecodeError:
            raise Exception("json faylı sefdir.")
    else:
        if path.isfile("./userbot/language/AZ.TGjson"):
            LOGS.warn("Varsayılan dil faylı işlədilir...")
            LANGUAGE_JSON = loads(open(f"./userbot/language/AZ.TGjson", "r").read())
        else:
            raise Exception(f"{LANGUAGE} senedini tapa bilmedim.")

LOGS.info(f"{LANGUAGE_JSON['LANGUAGE']} dili yüklendi.")

def get_value (plugin = None, value = None):
    global LANGUAGE_JSON

    if LANGUAGE_JSON == None:
        raise Exception("İlk önce dil faylını yükleyin")
    else: 
        if not plugin == None or value == None:
            Plugin = LANGUAGE_JSON.get("STRINGS").get(plugin)
            if Plugin == None:
                raise Exception("Sef plugin")
            else:
                String = LANGUAGE_JSON.get("STRINGS").get(plugin).get(value)
                if String == None:
                    return Plugin
                else:
                    return String
        else:
            raise Exception("Sef plugin veya string")
