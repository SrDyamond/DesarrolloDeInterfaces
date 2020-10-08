import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class PasswordWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Contraseña")

        ibox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        self.add(ibox)
"""
        image = Gtk.Image()
        image.set_from_file("producto.png")
        ibox.pack_start(image, True, True, 0)
"""

        self.entry = Gtk.Entry()
        self.entry.set_text("IMAGEN")
        ibox.pack_start(self.entry, True, True, 0)

        dbox = Gtk.Box(spacing=5)

        self.entry = Gtk.Entry()
        self.entry.set_text("IMAGEN")
        ibox.pack_start(self.entry, True, True, 0)

window = PasswordWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()

Gtk.main()
