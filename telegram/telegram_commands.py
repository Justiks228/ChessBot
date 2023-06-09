from aiogram.types import Message
from telegram.telegram_log.log import log
from aiogram.dispatcher.filters import Command
from telegram.telegram_authorize import new_token
from telegram.telegram_admin import remove_from_blacklist, add_on_blacklist
from telegram.telegram_queue import queue_join, queue_leave
from telegram.telegram_start import start
from telegram.telegram_profile import profile
from telegram.telegram_dashboard import get_top
from telegram.telegram_help import send_manual
from web_django.manage import bot, dp


log.info('bot successful started!')


@dp.message_handler(Command('start'))
async def start_command_handler(message: Message):
	"""Send manual to chat"""

	await start(bot, message)


@dp.message_handler(Command('help'))
async def help_command_handler(message: Message):
	"""Send full manual"""

	await send_manual(bot, message)


@dp.message_handler(Command('profile'))
async def profile_command_handler(message: Message):
	"""Сендит профиль автора сообщения"""

	await profile(bot, message)


@dp.message_handler(Command('queue_join'))
async def queue_join_command_handler(message: Message):
	"""Добавляет человека в очередь"""

	await queue_join(bot, message)


@dp.message_handler(Command('queue_leave'))
async def queue_leave_command_handler(message: Message):
	"""Убирает автора команды из очереди"""

	await queue_leave(bot, message)


@dp.message_handler(Command('dashboard'))
async def dashboard_handler(message: Message):
	"""Отправляет пользователю топ игроков"""

	await get_top(bot, message)


@dp.message_handler(Command('authorization'))
async def authorization_handler(message: Message):
	"""Отправляет код авторизации"""

	await new_token(bot, message)


@dp.message_handler(Command('add_on_blacklist'))
async def add_on_blacklist_handler(message: Message):
	"""Отправляет юзера в бан"""

	await add_on_blacklist(bot, message)


@dp.message_handler(Command('remove_from_blacklist'))
async def add_on_blacklist_handler(message: Message):
	"""Возвращает юзера из бан"""

	await remove_from_blacklist(bot, message)
