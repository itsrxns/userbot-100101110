# Copyright © 2020 di 100101110 Github, <https://github.com/100101110>.
#
# Questo file fa parte del progetto <https://github.com/100101110/userbot-100101110>,
# e viene rilasciato in base alla "Licenza GNU Affero General Public v3.0".
# Si prega di consultare <https://github.com/100101110/userbot-100101110/blob/master/LICENSE>
#
# Tutti i diritti riservati.
# 
# Crediti: @100101110
#
"""Commands:
.stopraid"""

import asyncio
from telethon import events
from userbot import bot
from userbot.system import dev_cmd


@bot.on(dev_cmd(pattern=f"stopraid", outgoing=True))
async def _(event):
    if event.fwd_from:
        return 
    await event.edit("**🚫 INTERROMPO RAID 🚫**")
    await asyncio.sleep(0.5)
    await event.edit("**‼️ RAID INTERROTTO ‼️**")
