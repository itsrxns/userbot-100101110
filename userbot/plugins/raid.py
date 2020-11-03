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
.raid"""

import asyncio
from telethon import events
from userbot import bot
from userbot.system import dev_cmd


@bot.on(dev_cmd(pattern=f"raid", outgoing=True))
async def _(event):
    if event.fwd_from:
        return 
    await event.edit("**⏳ Aggiungo utente selezionato alla lista raid...**")
    await asyncio.sleep(2)
    await event.edit("**✅ Utente aggiunto.**\n**✅ link generato.**)
    await asyncio.sleep(1)
    await event.edit("**🔎 Configurazione raid:**\n ├ Userbot in uso: **647**\n ├ Numero messaggi: **300**\n ├ Messaggi totali: **194.100**\n └ Time sleep: **0.5**\n\n **Utilizza .raidon per avviare il raid, .raidstop per annullare il raid.**")
