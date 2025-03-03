from personas.alumno import Alumno
from personas.persona import Persona
from personas.profesor import Profesor
from personas.director import Director

persona = Persona("Sebastian",23,4648451,"Masculino")
alumno = Alumno("Pablito",13,69554133,"masculino","Tercero de secundaria",332,120)
profesor =Profesor("Camilo",67,99559595,"Masculino","Matematicas","Maestro")
director =Director("Sergio",98,98989255,"Masculino","Director","Mañana","Solo de su esposa jajaj")

persona.mostrar_informacion()
persona.presentacion()
print("----------------------------------")
print("Misiones de un Alumno:")
alumno.mostrar_informacion()
alumno.estudiar()
alumno.hacer_tarea()
alumno.aprobar()
print("................................")
print("Misiones de un profesor")
profesor.mostrar_informacion()
profesor.enseñar()
profesor.educar()
print("----------------------------------")
print("misiones de un director")
director.mostrar_informacion()
director.administrar()
director.decomisos()
director.toma_desiciones()