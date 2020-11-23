import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from cliente_rest import ClienteRest

import threading
import shutil

builder = Gtk.Builder()
builder.add_from_file("producto.glade")

class Producto(Gtk.Window):
	def __init__(self,ref):
		Gtk.Window.__init__(self, title="Producto")
		print(ref)
		solicitar_producto(self,ref)
		window = builder.get_object("window")
