import util
import addon_lang

input_texto = "write a file in the desktop called hello"

addons = util.loadFrases()

def traducir(texto):
	addon = util.busquedaAddon(texto, addons)
	patrones_coincidentes = util.getPatronesIguales(texto, addon)
	entidades = util.getEntidades(texto, patrones_coincidentes)
	#comando = addon.construirComando(entidades)
	#return comando
print(traducir(input_texto))