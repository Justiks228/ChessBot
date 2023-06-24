from config.ConfigValues import ConfigValues
from exceptions.BaseError import BaseError


class OnResignError:
	def __init__(self, color: str):
		raise BaseError(ConfigValues.on_resign.replace('{color}', color))
