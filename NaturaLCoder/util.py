import glob
import addon_lang
import spacy
import re

def remove_stop_words(text):
	nlp = spacy.load("en_core_web_sm")
	doc = nlp(text)
	filtered_words = [token.text for token in doc if not token.is_stop]
	return ' '.join(filtered_words)

def find_between(texto):
	patrones = re.findall(r'<<.+?>>',texto)
	n_patrones = []
	for patron in patrones:
		n_patrones.append(patron.replace("<<", "").replace(">>", ""))
	return n_patrones

def find_patron(texto, patron):
	return re.findall(patron,texto)

def convertirPatron(patron):
	terminos = patron.split(" ")
	n_patron = ""
	for termino in terminos:
		if('$' in termino):
			n_patron = n_patron + ".+? "
		else:
			n_patron = n_patron + termino + " "
	return n_patron.strip()

def getEntidades(texto, patrones):


def getPatronesIguales(text, addon):
	patrones_iguales = []
	for patron_frase in addon.patrones:
		patrones_iguales = []
		for patron in patron_frase:
			patron_check = convertirPatron(patron)
			patrones_iguales.append(find_patron(text, patron_check))
			if(len(patrones_iguales) == len(patron_frase)):
				return patron_frase
			


def getPuntuacionCoincidencias(texto, palabras_addon):
	puntuacion = 0
	for palabra_addon in palabras_addon:
		if(palabra_addon in texto):
			puntuacion += 1
	return puntuacion

def busquedaAddon(texto, addons):
	puntuacion = 0
	addon_mejor = None
	for addon in addons:
		frases_addon = addon.frases
		palabras_addon = []
		for frase_addon in frases_addon:
			frase_addon = remove_stop_words(frase_addon)
			palabras_frase_addon = frase_addon.split(" ")
			palabras_addon = palabras_addon + palabras_frase_addon
		puntuacion_addon = getPuntuacionCoincidencias(texto, palabras_addon)
		if(puntuacion_addon > puntuacion):
			puntuacion = puntuacion_addon
			addon_mejor = addon
	return addon_mejor

def loadFrases():
	addons = []	
	directorios = glob.glob("addons/*")
	for directorio in directorios:
		frases = []
		ficheros = glob.glob(directorio + "/*")
		for fichero in ficheros:
			frases_fichero = open(fichero).readlines()
			frases = frases + frases_fichero
		addon = addon_lang.Addon_lang(directorio.split("\\")[1], frases)
		addons.append(addon)
	return addons


	#frases = open("addons")
