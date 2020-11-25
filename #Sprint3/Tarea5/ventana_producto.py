import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from cliente_rest import ClienteRest
import threading
import shutil
import requests

def descargar_imagen(url_imagen):
    # Descargo la imagen
    r = requests.get(url_imagen, stream = True)
    with open("temp.png", 'wb') as f:
        shutil.copyfileobj(r.raw, f)
    imagen = Gtk.Image()
    imagen.set_from_file("temp.png")
    return imagen


class Producto(Gtk.Window):
	def __init__(self,referencia,imagenproducto,nombre):
		Gtk.Window.__init__(self, title="Producto")
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

		imagen=descargar_imagen(imagenproducto)
		vbox0.pack_start(imagen,True,True,0)

		nom = Gtk.Label()
		nom.set_line_wrap(True)
		nom.set_markup("<b>"+nombre+"</b>")
		vbox0.pack_start(nom,True,True,0)

		ref = Gtk.Label(label=referencia)
		ref.set_line_wrap(True)
		ref.set_max_width_chars(50)
		vbox0.pack_start(ref,True,True,0)

		precio = Gtk.Label(label="Precio:13000")
		precio.set_line_wrap(True)
		precio.set_max_width_chars(50)
		hbox1.pack_start(precio,True,True,0)


		reservar = Gtk.Image()
		reservar.set_from_file("boton-reservar.png")
		button = Gtk.Button()
		button.add(reservar)
		button.set_size_request(50,50)
		hbox1.pack_start(button, True, True, 0)
