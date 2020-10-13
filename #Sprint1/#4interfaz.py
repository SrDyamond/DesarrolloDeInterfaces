import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Producto")
        boxprincipal = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=30)
        self.add(boxprincipal)

        abox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        boxprincipal.add(abox)

        bbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        boxprincipal.add(bbox)

        image = Gtk.Image()
        image.set_from_file("nombre.PNG")
        abox.pack_start(image, True, True, 50)

        image = Gtk.Image()
        image.set_from_file("tarjeta.PNG")
        bbox.pack_start(image, True, True, 50)




win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
