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
		x.start()


###############################
#
# Punto de entrada del programa

ventana = Ventana()
ventana.connect("destroy", Gtk.main_quit)
ventana.show_all()

Gtk.main()
