import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Ventana(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self)
		self.set_position(Gtk.WindowPosition.MOUSE)
		box = Gtk.Box()
		self.add(box)

		label = Gtk.Label(label = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum")
		label.set_line_wrap(True)
		label.set_justify(Gtk.Justification.FILL)
		label.set_max_width_chars(50)
		label.set_size_request(300, 150)
		box.pack_start(label, True, True, 0)
