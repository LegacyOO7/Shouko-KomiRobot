import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
import os
import shutil
import time
from config import Config 
from SmartConverter.Tools.progress import ( TimeFormatter,
  progress_for_pyrogram
)
import subprocess
import asyncio
from .. import TGBot
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from SmartConverter.Plugins.helper import *


@TGBot.on_message(filters.incoming & (filters.video | filters.document))
async def pdf_message(bot, message):
  if message.chat.id not in Config.AUTH_USERS:
    await message.reply_text("🚷 No Outsider Allowed ⚠️\n\nThis Bot is For Private Use Only.")
    return
  
  await message.reply_text(
    text="Sᴇʟᴇᴄᴛ Tʜᴇ Fᴏʀᴍᴀᴛ Yᴏᴜ Wᴀɴɴᴀ Cᴏɴᴠᴇʀᴛ",
    reply_markup=InlineKeyboardMarkup(
      [
        [
          InlineKeyboardButton("✫𝙿𝙳𝙵✫", callback_data="pdf"),
          InlineKeyboardButton("✫𝙴𝙿𝚄𝙱✫", callback_data="epub"),
          InlineKeyboardButton("✫𝙲𝙱𝚉✫", callback_data="cbz")
        ],
        [
          InlineKeyboardButton("✫𝙳𝙾𝙲𝚇✫",callback_data="docx"),
          InlineKeyboardButton("✫𝙳𝙾𝙲✫", callback_data="doc"),
          InlineKeyboardButton("✫𝚃𝚇𝚃✫", callback_data="txt")
        ],
        [
          InlineKeyboardButton("✫𝙼𝙿4✫", callback_data="mp4"),
          InlineKeyboardButton("✫𝙼𝙺𝚅✫", callback_data="mkv"),
          InlineKeyboardButton("✫𝚂𝚃𝚁𝙴𝙰𝙼✫", callback_data="stream")],
      ],
    ),
    quote=True,
    parse_mode="markdown"
  )
  
  