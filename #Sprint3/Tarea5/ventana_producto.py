import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from cliente_rest import ClienteRest
import threading
import shutil


class Producto(Gtk.Window):
	def __init__(self,ref,imagen,nombre):
		Gtk.Window.__init__(self, title="Producto")
		print(ref)
		print(nombre)
		builder = Gtk.Builder()
		builder.add_from_file("producto.glade")
		window = builder.get_object("window")
		#im=builder.get_object(imagen)
		no=builder.get_object(nombre)
		re=builder.get_object(ref)

		contenedor.pack_start(im, True, True, 0)

		self.add(contenedor)
		contenedor=builder.get_object("contenedor")
		contenedor.pack_start(imagen,True,False,0)
