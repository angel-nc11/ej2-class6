
class Alumno():

    def alumno(self, nombre, nota):
        self.nombre=nombre
        self.nota=nota

    def mostrar(self):
        print("nombre: ", self.nombre)
        print("nota: ", self.nota)
        
        if self.nota >=6:
            print("Ha aprobado")

        else:
            print("Ha reprobado")

alumnos=Alumno()

alumnos.alumno("Pedro", 9)
alumnos.mostrar()

alumnos.alumno("Maria", 5)
alumnos.mostrar()

    
