import requests

class ClienteRest:
	def solicitar_lista_productos(self):
		response = requests.get('http://localhost:8080/product')
		return response.json()

	def solicitar_producto(self, referencia):
		response = requests.get('http://localhost:8080/product/' + referencia)
		return response.json()

	def solicitar_reserva(self,referencia,username):
		response = requests.get("http://localhost:8080/"+username+"/reserve/"+referencia)
		return response.json()

	def crear_reserva(self,referencia,username):
		response = requests.post("http://localhost:8080/"+username+"/reserve/"+referencia")
		return response.json()

	def borrar_reserva(seld,referencia,username):
		response = requests.delete("http://localhost:8080/"+username+"/reserve/"+referencia")
		return response.json()
