
class Usuario:
	def __init__(self, nombre="", email=""):
		self.__nombre = nombre
		self.__email = email

	@property
	def nombre(self):
		return self.__nombre

	@property
	def email(self):
		return self.__email

	def __str__(self):
		return "Nombre: {} E-mail: {}".format(self.__nombre, self.__email)

	def leer_datos(self):
		self.__nombre = input("Introduce el nombre: ")
		self.__email = input("Introduce el email: ")

	
	