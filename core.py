from exceptions.OnEndTimeError import OnEndTimeError


def on_end_time_error(*args, **kwargs):
	raise OnEndTimeError(kwargs["color"])


def get(from_list: list, path: str, **kwargs):
	"""The method allows you to get an object according to the condition set using **kwargs and path

	:arg: from_list - The list in which the search is performed
	:arg: path - path the path from the class attributes to the class to get (str)
	:arg: **kwarg - Give one argument with the name corresponding to the argument by which the comparison will be made, and put the value itself that you are looking for in the value

	:return: class which you want get

	Ex.:

	print(get(games, "players.timer", time=30))
	# Output: Timer object

	(GOVNOCODE #YANDERECODING #SHITPOST)

	"""

	positions = path.split('.')
	value_name = list(kwargs.keys())[0]

	for obj in from_list:

		for position in positions:

			try:
				obj = obj.__dict__[position]
			except TypeError:
				for i in obj:
					obj = i.__dict__[position]

		if obj.__dict__[value_name] == kwargs[value_name]:
			return obj
