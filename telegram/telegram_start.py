from aiogram.types import Message
from aiogram import Bot
from database_tools.Connection import connect
from telegram.telegram_core import in_blacklist, recharge
from config.ConfigValues import ConfigValues


@recharge
@in_blacklist
async def start(bot: Bot, message: Message):
	"""send start message"""

	if await (await connect.request("SELECT user_id FROM users WHERE user_id = ?", (message.from_id, ))).fetchone():
		await bot.send_message(message.chat.id, ConfigValues.game_instructions)
		return

	await bot.send_message(message.chat.id, ConfigValues.authorization_instructions)
