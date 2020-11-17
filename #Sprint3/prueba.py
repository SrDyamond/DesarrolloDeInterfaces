import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from celda_producto import CeldaProducto

# Crear una imagen desde un archivo
imagen = Gtk.Image()
imagen.set_from_file('patatatruck.png')

# Crear la celda de prueba
celda = CeldaProducto('Nombre de prueba', 'Referencia de prueba 00001', imagen)

# Crear una ventana y añadirla y mostrarla
window = Gtk.Window(title='Prueba')
window.connect("destroy", Gtk.main_quit)
window.add(celda)
window.show_all()

Gtk.main()
