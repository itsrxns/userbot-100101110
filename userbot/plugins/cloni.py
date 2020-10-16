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

import asyncio
from telethon import events, version
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME, bot, versions
from userbot.system import dev_cmd

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "100101110"
# ============================================

@bot.on(dev_cmd(pattern=f"cloni", outgoing=True))
async def amireallyalive(cloni):
    """ For .alive command, check if the bot is running. """
    await cloni.edit("**🤖 Cloni attivi**\n" 
                     f" ├ [𝐿𝑒𝑡𝑖𝑧𝑖𝑎ⁿᵃᶻ](t.me/LaMonacaDiMonza) ✅\n"
                     f" └ [AlessandrO](t.me/Boicottato) ✅")
                     
