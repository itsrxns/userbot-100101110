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
.avast
.avast1
.call
.hack
.linux
.macos
.stock
.windows"""

import asyncio
from telethon import events
from platform import uname
from userbot import CMD_HELP, ALIVE_NAME, bot
from userbot.system import dev_cmd

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "100101110"
# ============================================


@bot.on(dev_cmd(pattern=f"gay", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0, 11)
    #input_str = event.pattern_match.group(1)
    #if input_str == "avast":
    await event.edit("avast")
    animation_chars = [
        
            "**@XxGamerYT303**",
            "**TI STA SCOPANDO**",
            "**OH NO SEI DIVENTATO GAY **",
        ]