from aiogram.bot import Bot
from database_tools.Connection import connect
from config.ConfigValues import ConfigValues


async def download_user_avatar(bot: Bot, user_id: int):
	"""Download user profile photo

	:arg bot - bot object
	:arg user_id - user id
	"""

	user_profile_photo = await bot.get_user_profile_photos(user_id)

	if len(user_profile_photo.photos) > 0:

		file = await bot.get_file(user_profile_photo.photos[0][0].file_id)
		await bot.download_file(file.file_path, f'../avatars/{user_id}.png')


def in_blacklist(func):
	async def wrapped(*args, **kwargs):
		if (await (
				await connect.request("SELECT user_id FROM blacklist WHERE user_id = ?", (args[1].from_id, ))
		).fetchone()):
			return await args[0].send_message(args[1].chat.id, ConfigValues.on_blacklsit_message)

		return await func(*args, **kwargs)

	return wrapped