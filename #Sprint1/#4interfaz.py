import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Producto")
        scrolled = Gtk.ScrolledWindow()
        scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        self.add(scrolled)

        boxprincipal = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=30)
        scrolled.add(boxprincipal)

        abox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        boxprincipal.add(abox)

        bbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        boxprincipal.add(bbox)

        cbox= Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        boxprincipal.add(cbox)

        dbox= Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        boxprincipal.add(dbox)

        ebox= Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        boxprincipal.add(ebox)



        #caja a
        image = Gtk.Image()
        image.set_from_file("nombre.PNG")
        abox.pack_start(image, True, True, 50)

        image = Gtk.Image()
        image.set_from_file("ref.PNG")
        abox.pack_start(image, True, True, 50)
        #caja b
        image = Gtk.Image()
        image.set_from_file("tarjeta.PNG")
        bbox.pack_start(image, True, True, 50)

        image = Gtk.Image()
        image.set_from_file("precio.PNG")
        bbox.pack_start(image, True, True, 50)
        #espacio en blanco
        #title = Gtk.Label()
        #dbox.pack_start(title, True, False, 0)
        #caja c
        button = Gtk.Button(label="Comprar")
        #button.connect("clicked", self.on_button_clicked)
        gtk_button_set_image("comprar.PNG")
        cbox.pack_start(button, True, True, 0)

        button = Gtk.Button(label="Agregar al carrito")
        #button.connect("clicked", self.on_button_clicked)
        cbox.pack_start(button, True, True, 0)

        #caja d
        image = Gtk.Image()
        image.set_from_file("caracteristicas.PNG")
        dbox.pack_start(image, True, True, 50)


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
