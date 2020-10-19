import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class ComponenteAdivinanza(Gtk.Box):
	def __init__(self, adivinanza, solucion):
		Gtk.Box.__init__(self, orientation=Gtk.Orientation.VERTICAL, spacing=5)
		label = Gtk.Label(label=adivinanza)
		label.set_size_request(200, 100)
		label.set_line_wrap(True)
		label.set_max_width_chars(50)
		button = Gtk.Button(label="Ver respuesta")
		button.connect("clicked", self.on_button_clicked)
		self.solucion = solucion
		self.pack_start(label, True, True, 0)
		self.pack_start(button, False, False, 0)

	def on_button_clicked(self, widget):
		window = Gtk.Window(title="")
		window.set_position(Gtk.WindowPosition.MOUSE)
		label = Gtk.Label(label=self.solucion)
		label.set_padding(80, 20)
		window.add(label)
		window.show_all()
