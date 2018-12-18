from filter import Filter
from decorations.vignette import Vignette

class Lomo(Vignette, Filter):
	
	def apply(self):
		self.execute("convert {filename} -channel R -level 33% -channel G -level 33% {filename}")
		self.vignette()