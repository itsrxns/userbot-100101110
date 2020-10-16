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
    await cloni.edit("**✅ Userbot di** [Gucci RxnS 4L #VVS 💎⌚🇮🇹](t.me/lordrxns) **online.**\n\n" 
                     f"**Informazioni userbot:**\n"
                     f"**• ℹ️ Telethon:** {version.__version__}\n"
                     f"**• 🐍 Python:** {versions.__python_version__}\n"
                     f"**• 👤 Username:** {DEFAULTUSER}\n\n"
                     f"**Informazioni server:**\n"
                     f"**• ℹ️ Tipologia:** Server dedicato 10 Gbps\n"
                     f"**• 🖥 OS:** Debian GNU/Linux 10 (buster)\n"
                     f"**• 🛡 Processore:** Intel Xeon Dual E5-2650 v4\n"
                     f"**• 🛡 RAM:** 512GB\n"
                     f"**• 💿 SSD:** 8TB\n"
                     f"**• 🔥 DDoS Protection:** 100 Gbps\n"
                     f"**• 🌐 Velocità porta:** 10 Gbps\n"
                     f"**• 📥 Download medio:** 9500 Mbps\n"
                     f"**• 📤 Upload medio:** 8700 Mbps")
