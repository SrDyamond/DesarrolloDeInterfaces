import gi
#from gi.repository import GdkPixbuf
import requests
import shutil
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
#from catalogocontrolador import descargar_imagen
def descargar_imagen(url_imagen):
    # Descargo la imagen
    r = requests.get(url_imagen, stream = True)
    with open("temp.png", 'wb') as f:
        shutil.copyfileobj(r.raw, f)
    imagen = Gtk.Image()
    imagen.set_from_file("temp.png")
    return imagen

class Ebrozone(Gtk.Window):
    def __init__(self,referencia,imagenproducto,nombre2):
        Gtk.Window.__init__(self, title="Ebrozone")
        self.set_default_size(1280 , 720 )
        
        scrolled = Gtk.ScrolledWindow()
        scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        self.add(scrolled)
        
        hbox0 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        scrolled.add(hbox0)
        self.add(hbox0)
        
        vbox0 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        hbox0.pack_start(vbox0,True,True,0)
        
        vbox1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        hbox0.pack_start(vbox1,True,True,0)
        
        hbox1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        vbox1.pack_start(hbox1,True,True,0)
        
        #image = Gtk.Image()
        #image.set_from_file("tortuga.png")
        imagen=descargar_imagen(imagenproducto)
        vbox0.pack_start(imagen,True,True,0)
        
        nombre = Gtk.Label()
        nombre.set_line_wrap(True)
        nombre.set_markup("<b>"+nombre2+"</b>")
        vbox0.pack_start(nombre,True,True,0)
        
        ref = Gtk.Label(label=referencia)
        ref.set_line_wrap(True)
        ref.set_max_width_chars(50)
        vbox0.pack_start(ref,True,True,0)
        
        precio = Gtk.Label(label="7500€")
        precio.set_line_wrap(True)
        precio.set_max_width_chars(50)
        hbox1.pack_start(precio,True,True,0)
        
        descripcion = Gtk.Label(label="Preciosa descripción de unha cousa fermosa como é esta Carmiña, é unha tortuguiña moi cariñosa, moi atenta e que sempre che deixa un sorriso na cara, ten 3 anos 50k km sempre piscina nunca océano, preparada para rally.")
        descripcion.set_line_wrap(True)
        descripcion.set_max_width_chars(50)
        vbox1.pack_start(descripcion,True,True,0)
        
        
        
        
        carrito = Gtk.Image()
        carrito.set_from_file("carrito.png")
        button = Gtk.Button()
        button.add(carrito)
        button.set_size_request(50,50)
        hbox1.pack_start(button, True, True, 0)
        
#window = Ebrozone()
#window.connect("destroy", Gtk.main_quit)
#window.show_all()

#Gtk.main()
