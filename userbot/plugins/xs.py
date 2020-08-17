import asyncio
from heroku_config import Var
from telethon.tl.functions.users import GetFullUserRequest
from userbot.plugins.sql_helper.mute_sql import is_muted, mute, unmute
from userbot.system import command
from userbot import ALIVE_NAME

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "100101110"
BOTLOG = True
BOTLOG_CHATID = Var.PRIVATE_GROUP_ID

@command(outgoing=True, pattern=r"^.x ?(\d+)?")
async def startgmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await event.edit(f"`{DEFAULTUSER}:`**💢Si è verificato un errore!💢**")
        await asyncio.sleep(3)
        private = True
    reply = await event.get_reply_message()
    if event.pattern_match.group(1) is not None:
        userid = event.pattern_match.group(1)
    elif reply is not None:
        userid = reply.sender_id
    elif private is True:
        userid = event.chat_id
    else:
        return await event.edit(f"`{DEFAULTUSER}:`**🚫Rispondi ad un user per mutare🚫**")
    chat_id = event.chat_id
    replied_user = await event.client(GetFullUserRequest(userid))
    if is_muted(userid, "gmute"):
        return await event.edit(f"`{DEFAULTUSER}:`**💢User già mutato💢**")
    try:
        mute(userid, "x")
    except Exception as e:
        await event.edit("Error occured!\nError is " + str(e))
    else:
        await event.edit(f"`{DEFAULTUSER}:`**✅UTENTE MUTATO CON SUCCESSO.**")
    if BOTLOG:
      await event.client.send_message(
                    BOTLOG_CHATID, "#MUTE\n"
                    f"USER: [{replied_user.user.first_name}](tg://user?id={userid})\n"
                    f"CHAT: {event.chat.title}(`{event.chat_id}`)")

@command(outgoing=True, pattern=r"^.d ?(\d+)?")
async def endgmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await event.edit(f"`{DEFAULTUSER}:`**Si è verificato un errore!⚠️**")
        await asyncio.sleep(3)
        private = True
    reply = await event.get_reply_message()
    if event.pattern_match.group(1) is not None:
        userid = event.pattern_match.group(1)
    elif reply is not None:
        userid = reply.sender_id
    elif private is True:
        userid = event.chat_id
    else:
        return await event.edit(f"`{DEFAULTUSER}:`**Rispondi ad un user per unmutare.**")
    chat_id = event.chat_id
    replied_user = await event.client(GetFullUserRequest(userid))
    if not is_muted(userid, "gmute"):
        return await event.edit(f"`{DEFAULTUSER}:`**🚫User non mutato🚫**")
    try:
        unmute(userid, "d")
    except Exception as e:
        await event.edit("Error occured!\nError is " + str(e))
    else:
        await event.edit(f"`{DEFAULTUSER}:`**✅unmute eseguito.**")
    if BOTLOG:
      await event.client.send_message(
                    BOTLOG_CHATID, "#UNMUTE\n"
                    f"USER: [{replied_user.user.first_name}](tg://user?id={userid})\n"
                    f"CHAT: {event.chat.title}(`{event.chat_id}`)")          

@command(incoming=True)
async def watcher(event):
    if is_muted(event.sender_id, "d"):
        await event.delete()