import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Producto")
        self.set_default_size(600, 450)
        self.set_border_width(30)
        scrolled = Gtk.ScrolledWindow()
        scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        self.add(scrolled)
        #inicializao a box principal
        boxprincipal = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        scrolled.add(boxprincipal)
        #init boxes
        abox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        boxprincipal.add(abox)

        bbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        boxprincipal.add(bbox)

        cbox= Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        boxprincipal.add(cbox)

        dbox= Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        boxprincipal.add(dbox)

        ebox= Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        boxprincipal.add(ebox)
        #box a
        titulo = Gtk.Label()
        titulo.set_markup('<span size="xx-large" weight="bold">Geforce RTX 3070</span>')
        abox.pack_start(titulo, True, True, 10)

        ref = Gtk.Label()
        ref.set_markup('<span size="xx-large" weight="bold">REF-3645741</span>')
        abox.pack_start(ref, True, True, 10)
        #box b
        image = Gtk.Image()
        image.set_from_file("tarjeta.PNG")
        bbox.pack_start(image, True, True, 10)

        precio = Gtk.Label()
        precio.set_markup('<span size="xx-large" weight="bold">899 Euros</span>')
        bbox.pack_start(precio, True, True, 10)
        #espacio en blanco
        #title = Gtk.Label()
        #dbox.pack_start(title, True, False, 0)
        #box c
        comprar=Gtk.Image()
        comprar.set_from_file("comprar.PNG")
        button=Gtk.Button()
        button.add(comprar)
        #button.set_size_request(50,50)
        button.connect("clicked", self.on_button_clicked)
        cbox.pack_start(button, True, False, 0)

        carrito=Gtk.Image()
        carrito.set_from_file("carrito.PNG")
        #button.set_size_request(50,50)
        button = Gtk.Button()
        button.add(carrito)
        button.set_size_request(50,50)
        button.connect("clicked", self.on_button1_clicked)
        cbox.pack_start(button, True, False, 0)

        #box d
        image = Gtk.Image()
        image.set_from_file("caracteristicas.PNG")
        dbox.pack_start(image, True, True, 50)

    def on_button_clicked(self, widget):
        print("Comprado")

    def on_button1_clicked(self, widget):
        print("Agregado al carrito")


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
