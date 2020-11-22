import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from cliente_rest import ClienteRest

import threading
import shutil

builder = Gtk.Builder()
builder.add_from_file("producto.glade")

class Producto(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self, title="Producto")


	def mostrarProducto(self):
		Gtk.Window.__init__(self, title="Producto")
		builder = Gtk.Builder()
		builder.add_from_file("producto.glade")
		window = builder.get_object("window")

		window.show_all()
