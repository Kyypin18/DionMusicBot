# © github.com/SeorangDion
# https://github.com/SeorangDion/DionMusicBot/tree/dion/dion/modules/alive.py

from os import path
from pyrogram import Client, filters
from pyrogram import __version__ as pyrover
from pyrogram.types import Message
from dion import app
from pytgcalls import __version__ as pytover

from dion.config import (
    SUPPORT,
    UPDATE,
    BOT_USERNAME,
)
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



DION_IMG = "https://telegra.ph/file/f65b5b2d6c97e21cbed1d.jpg"


@app.on_message(filters.command(["malive", f"malive@{BOT_USERNAME}"]))
async def alive(client, message):
    await client.send_photo(message.chat.id,
        photo=f"{DION_IMG}",
        caption=f"""**Holla {message.from_user.mention()}.** \n
✘ **I'm Working Properly for you** \n
✘ **Pyrogram Version : `{pyrover}`** \n
✘ **PyTgCalls Version: `{pytover.__version__}`** \n
✘ **Using New Version** \n
**Thanks For Using Me 🔥**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ᴜᴘᴅᴀᴛᴇs", url=f"t.me/skytrixch"
                    ),
                    InlineKeyboardButton(
                        "sᴜᴘᴘᴏʀᴛ", url=f"t.me/wibuhouse"
                    )
                ]
            ]
        )
    )
