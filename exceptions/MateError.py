from config.ConfigValues import ConfigValues
from exceptions.BaseError import BaseError


class MateError(BaseError):
	def __init__(self, color: str):
		raise BaseError(ConfigValues.on_mate_message.replace('{color}', color))
