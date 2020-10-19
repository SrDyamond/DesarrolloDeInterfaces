import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Ventana(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self)
		self.set_position(Gtk.WindowPosition.CENTER)
		self.set_default_size(100, 200)
		self.set_resizable(False)
		image1 = Gtk.Image()
		image1.set_from_file("penguin.jpg")
		image2 = Gtk.Image()
		image2.set_from_file("lion.jpg")
		image3 = Gtk.Image()
		image3.set_from_file("jiraffe.jpg")

		box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
		box.pack_start(image1, True, True, 0)
		box.pack_start(image2, True, True, 0)
		box.pack_start(image3, True, True, 0)

		scrolled = Gtk.ScrolledWindow()
		scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
		self.add(scrolled)
		scrolled.add(box)
