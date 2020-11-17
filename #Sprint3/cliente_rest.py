import requests

class ClienteRest:

	def __init__(self):
		self.servidor = 'http://localhost:8080'

	def solicitar_lista_productos(self):
		return requests.get('http://localhost:8080/product')

	def solicitar_producto(self, referencia):
		return requests.get('http://localhost:8080/product' + referencia)

	def solicitar_reservas(self, usuario, password_sha):
		if usuario is None:
			usuario = 'developer'
		if password_sha is None:
			password_sha = '9d4e1e23bd5b727046a9e3b4b7db57bd8d6ee684'

		return requests.get('http://localhost:8080/' + usuario + '/reserve?passwordSha=' + password_sha)

	def crear_reserva(self, usuario, password_sha, referencia_producto):
		if usuario is None:
			usuario = 'developer'
		if password_sha is None:
			password_sha = '9d4e1e23bd5b727046a9e3b4b7db57bd8d6ee684'

		return requests.post(self.servidor + '/' + usuario + '/reserve/' + referencia_producto + '?passwordSha=' + password_sha)

	def borrar_reserva(self, usuario, password_sha, referencia_producto):
		if usuario is None:
			usuario = 'developer'
		if password_sha is None:
			password_sha = '9d4e1e23bd5b727046a9e3b4b7db57bd8d6ee684'

		return requests.delete(self.servidor + '/' + usuario + '/reserve/' + referencia_producto + '?passwordSha=' + password_sha)
