import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Ventana(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self)
		self.set_position(Gtk.WindowPosition.CENTER)
		label = Gtk.Label(label = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.")
		label.set_line_wrap(True)
		label.set_max_width_chars(50)
		label.set_justify(Gtk.Justification.FILL)

		button = Gtk.Button(label = "Pulsa")
		button.set_size_request(50, 50)

		box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
		self.add(box)
		box.pack_start(label, True, False, 0)
		box.pack_start(button, True, True, 0)
