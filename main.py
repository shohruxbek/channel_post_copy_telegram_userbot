from pyrogram import Client, filters, types
import re

api_id = *** #api_id https://my.telegram.org/auth?to=apps dan olinadi
api_hash = "***" #api_hash https://my.telegram.org/auth?to=apps dan olinadi

app = Client("my_account", api_id=api_id, api_hash=api_hash)

CHANNEL_ID = -1001001766948  #qaysi kanaldan postlarni olish kerak bo'lsa shu kanal ID raqami yoziladi. Hozirda @kunuzofficial kanali ID raqami yozilgan
CHANNEL_TITLE = "Kun.uz | Дубликат" #2-kanalni nomi yoziladi
CHANNEL_POST = -1001628372763 #1-kanaldagi postlar qaysi kanalga tushishi kerak bo'lsa o'sha channel ID yoziladi
CHANNEL_POST_USERNAME_URL = "https://t.me/kunuz_offi" #2-kanal linki yoziladi

print(".")
print("...")
print("... ...")
print("... ... ...")
print("... ... ... ...")
print("... Bot ishga tushdi ...")
print("... ... ... ...")
print("... ... ...")
print("... ...")
print("...")
print(".")

# channel post

@app.on_message(filters=filters.channel)
def my_handler(client: Client, message: types.Message):
    if message.chat.id != CHANNEL_ID:
        return
    print(message)
    if message.text:
        if message.text.find("Реклама") > 0:
            return
        app.send_message(CHANNEL_POST, text+"\n"+CHANNEL_POST_USERNAME_URL)

    if message.photo:
        if message.caption.find("Реклама") > 0:
            return
        file_id = message.photo.file_id

        ce = message.caption_entities
        my_list = []
        for val in ce:

            if str(val.type) == "MessageEntityType.TEXT_LINK":
                val.url = CHANNEL_POST_USERNAME_URL

            my_list.append(val)
        caption = message.caption.replace('Kun.uz ', CHANNEL_TITLE+" ")
        app.send_photo(CHANNEL_POST, file_id, caption, "HTML", my_list)

    if message.video:
        if message.text.find("Реклама") > 0:
            return
        file_id = message.video.file_id

        ce = message.caption_entities
        my_list = []
        for val in ce:

            if str(val.type) == "MessageEntityType.TEXT_LINK":
                val.url = CHANNEL_POST_USERNAME_URL

            my_list.append(val)
        caption = message.caption.replace('Kun.uz ', CHANNEL_TITLE+" ")
        app.send_video(CHANNEL_POST, file_id, caption, "HTML", my_list)

app.run()