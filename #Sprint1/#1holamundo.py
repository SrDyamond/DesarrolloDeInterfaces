import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

window = Gtk.Window(title="Hola mundo")
window.show()
window.connect("destroy", Gtk.main_quit)
Gtk.main()
