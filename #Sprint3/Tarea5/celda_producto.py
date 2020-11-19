import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from ventana_producto import Producto
class CeldaProducto(Gtk.Button):
	def __init__(self, nombre, referencia, imagen):
		Gtk.Button.__init__(self)
		box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
		box.pack_start(imagen, True, True, 0)
		box.pack_start(Gtk.Label(label=nombre), False, False, 0)
		box.pack_start(Gtk.Label(label=referencia), False, False, 0)

		self.add(box)
		self.connect("clicked", Producto.mostrarProducto)
