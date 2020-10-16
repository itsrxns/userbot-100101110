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
.checkcloni"""

import asyncio
from telethon import events
from userbot import bot
from userbot.system import dev_cmd


@bot.on(dev_cmd(pattern=f"checkcloni", outgoing=True))
async def _(event):
    if event.fwd_from:
        return 
    await event.edit("**🔎 Verifico cloni attivi...**")
    await asyncio.sleep(2)
    await event.edit("**✅ 3 cloni attivi trovati.**")
    await asyncio.sleep(2)
    await event.edit("**🤖 Cloni attivi**\n ├ [𝐿𝑒𝑡𝑖𝑧𝑖𝑎ⁿᵃᶻ](t.me/LaMonacaDiMonza) ✅\n ├ [AlessandrO](t.me/Boicottato) ✅\n └ [Marteⁿᵃᶻ💎🔥 ⁪⁬⁮⁮⁮⁮](t.me/dubitante) ✅")
    await asyncio.sleep(1)
    await event.edit("**🤖 Cloni attivi**\n ├ [𝐿𝑒𝑡𝑖𝑧𝑖𝑎ⁿᵃᶻ](t.me/LaMonacaDiMonza) ✅\n ├ [AlessandrO](t.me/Boicottato) ✅\n └ [Marteⁿᵃᶻ💎🔥 ⁪⁬⁮⁮⁮⁮](t.me/dubitante) ✅\n\n**Verifica completata.**")
    await asyncio.sleep(1)
