import gi
import requests
import threading
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib
from cliente_rest import ClienteRest
from celda_producto import CeldaProducto
import shutil

def descargar_imagen(url_imagen):
	# Descargo la imagen
	r = requests.get(url_imagen, stream = True)
	with open("temp.png", 'wb') as f:
		shutil.copyfileobj(r.raw, f)
	imagen = Gtk.Image()
	imagen.set_from_file("temp.png")
	return imagen

"""
Carga los productos del API REST.
"""
def cargar_productos(flowbox):
	cliente = ClienteRest()
	productos = cliente.solicitar_lista_productos().json()
	celdas = []
	for producto in productos:
		nombre = producto.get("name")
		referencia = producto.get("reference")
		url_imagen = producto.get("imagenPath")
		imagen = descargar_imagen(url_imagen)
		celda = CeldaProducto(nombre, referencia, imagen)
		celdas.append(celda)

	GLib.idle_add(mostrar_productos_ui_thread, flowbox, celdas)

"""
Añade celdas de producto a un flowbox y las muestra.
"""
def mostrar_productos_ui_thread(flowbox, celdas_productos):
	for celda in celdas_productos:
		flowbox.add(celda)
	flowbox.show_all()

class CatalogoControlador():
	def __init__(self, objeto_constructor):
		contenedor = objeto_constructor.get_object("contenedor_productos")
		hilo = threading.Thread(target=cargar_productos, args=(contenedor,))
		hilo.start()
