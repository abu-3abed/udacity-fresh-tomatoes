import webbrowser

class Movie:

	"""docstring for Movie"""
	def __init__(self, title, storyline, poster_image, trailer_youtube):
		self.title = title
		self.storyline = storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

	def show_trailer(self):
		webbrowser.open_new_tab(self.trailer_youtube)
# title
# storyline
# poster_image
# trailer_youtube
	