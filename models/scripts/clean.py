"""
clean.py
author(s): khuynh
description: this is a helper script to clean a set of facebook messages.
it outputs the facebook messages into a single .txt file with each message
on its own line

link to download your facebook messages:
https://www.facebook.com/dyi/?referrer=yfi_settings
"""
import json
import string
from pathlib import Path

DIRECTORY_MESSAGES = Path("messages/inbox").resolve()
PERSON_NAME = "Jai Miles"

messages = []
printable = set(string.printable)

for directory in DIRECTORY_MESSAGES.iterdir():
    if PERSON_NAME.split(" ")[0].lower() in str(directory):
        directory_person = DIRECTORY_MESSAGES / directory

        for f in directory_person.iterdir():
            if f.suffix == ".json":
                with f.open("r") as message_json:
                    conversation = json.load(message_json)
                    conversation = [
                        "".join(
                            filter(lambda x: x in printable, message.get("content", ""))
                        )
                        for message in conversation["messages"]
                        if message["sender_name"] == PERSON_NAME
                    ]

                    messages += conversation

with open(f"{PERSON_NAME.split(' ')[0].lower()}.txt", "w", encoding="utf-8") as to_file:
    for message in messages:
        to_file.write(message)
        to_file.write("\n")
