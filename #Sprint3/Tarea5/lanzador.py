import gi
import threading
import requests

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

def pedir_productos(numero, ventana):
	url = 'http://localhost:8080/product'
	response = requests.get(url)
	if response.ok:
		ventana.label.set_text(str(response.json()))
	else:
		ventana.label.set_text("La petición ha fallado")

def un_producto(numero,ventana):
	url = 'http://localhost:8080/product/R-001'
	response = requests.get(url)
	if response.ok:
		ventana.label.set_text(str(response.json()))
	else:
		ventana.label.set_text("La petición ha fallado")

def pedir_reserva(numero,ventana):
	url = 'http://localhost:8080/developer/reserve?passwordSha=9d4e1e23bd5b727046a9e3b4b7db57bd8d6ee684'
	response = requests.get(url)
	if response.ok:
		ventana.label.set_text(str(response.json()))
		#preguntar si puede devolver u njson array
	else:
		ventana.label.set_text("La petición ha fallado")

class Ventana(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self, title="")
		self.label = Gtk.Label(label="Comenzando...")
		self.add(self.label)
		self.label.set_margin_bottom(50)
		self.label.set_margin_top(50)
		self.label.set_margin_start(100)
		self.label.set_margin_end(100)
		x = threading.Thread(target=pedir_productos, args=(1,self))
		y = threading.Thread(target=un_producto, args=(2,self))
		z = threading.Thread(target=pedir_reserva, args=(3,self))
		x.start()
		y.start()
		z.start()


###############################
#
# Punto de entrada del programa

ventana = Ventana()
ventana.connect("destroy", Gtk.main_quit)
ventana.show_all()

Gtk.main()
