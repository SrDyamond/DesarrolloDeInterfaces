import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Ventana(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self)
		self.set_position(Gtk.WindowPosition.MOUSE)
		label = Gtk.Label(label = "Texto")
		label.set_size_request(300, 150)
		self.add(label)
