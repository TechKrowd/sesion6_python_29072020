from profesor import Profesor
from alumno import Alumno
from profesor_auxiliar import ProfesorAuxiliar

class Universidad:

	def __init__(self):
		self.__usuarios = list()

	@classmethod
	def new_profesor(cls):
		p = Profesor()
		return p

	@classmethod
	def new_alumno(cls):
		a = Alumno()
		return a

	@classmethod
	def new_auxiliar(cls):
		pa = ProfesorAuxiliar()
		return pa

	def insertar_usuario(self):
		options = [self.new_profesor,self.new_alumno,self.new_auxiliar]
		print("Seleccions el tipo de usuario: ")
		opc = input("1. Profesor\n2. Alumno\n3. Profesor auxiliar")
		if opc.isdigit():
			opc = int(opc)
			if opc<1 or opc>3:
				print("Opción incorrecta")
			else:
				usuario = options[opc-1]()
				usuario.leer_datos()
				self.__usuarios.append(usuario)
				print("Inserción realizada correctamente")
		else:
			print("Formato incorrecto")

	def imprimir(self):
		for usuario in self.__usuarios:
			print(usuario)