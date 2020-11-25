import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from ventana_producto import Producto

class CeldaProducto(Gtk.Button):
	def __init__(self, nombre, referencia, imagen, url_imagen):
		Gtk.Button.__init__(self)
		box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
		box.pack_start(imagen, True, True, 0)
		box.pack_start(Gtk.Label(label=nombre), False, False, 0)
		box.pack_start(Gtk.Label(label=referencia), False, False, 0)

		self.add(box)
		self.connect("clicked", self.clicado,url_imagen)
		self.referencia=referencia
		self.nombre=nombre
		self.imagen=imagen
	def clicado(self, widget,url_imagen):
		print(self.referencia)
		window = Producto(self.referencia,url_imagen,self.nombre)
		window.show_all()
