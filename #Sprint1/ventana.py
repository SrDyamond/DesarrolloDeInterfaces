import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Ventana(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self)
		self.set_position(Gtk.WindowPosition.MOUSE)
		box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
		self.add(box)

		button = Gtk.Button(label="Boton Activable")
		#button.connect("clicked", self.on_button_clicked)
		box.pack_start(button, True, True, 0)
