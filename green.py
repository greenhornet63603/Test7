from pyrogram import Client
from pyrogram.sessions import StringSession

# Replace these with your own API ID and API HASH from https://my.telegram.org
api_id = 27400172
api_hash = "56d0a75c5f9a9de6beb5452aa63c2d36"

with Client(StringSession(), api_id=api_id, api_hash=api_hash) as app:
    print("Your new session string:\n")
    print(app.export_session_string())
