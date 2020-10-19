import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Ventana(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self)
		self.set_position(Gtk.WindowPosition.MOUSE)
		box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
		self.add(box)

		button = Gtk.CheckButton(label="Boton Activable")
		button.set_size_request(300, 150)
		button.connect("clicked", self.ha_clicado)
		box.pack_start(button, True, True, 0)

	def ha_clicado(self, widget):
			if widget.get_active() == True:
				print("El checkButton ha sido marcado")
			else:
				print("El checkButton ha sido desmarcado")
