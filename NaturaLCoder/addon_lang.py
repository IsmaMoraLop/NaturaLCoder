import util

class Addon_lang:
	def __init__(self, tema, frases):
		self.tema = tema
		self.frases = frases
		self.patrones = self.get_patrones()
	def get_patrones_frase(self, frase):
		patrones = util.find_between(frase)
		return patrones

	def get_patrones(self):
		patrones = []
		for frase in self.frases:
			patrones.append(self.get_patrones_frase(frase))
		return patrones

