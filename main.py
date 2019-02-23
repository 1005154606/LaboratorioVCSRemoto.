print("Tercer ejercicio")
import math
a=float(input("Introduce el valor de a: "))
b=float(input("Introduce el valor de b: "))
c=float(input("Introduce el valor de c: "))

d=b**2-4*a*c
if d<0:
	print("No existe solución en los reales")
else:
	x1=(-b+math.sqrt(d))/(2*a)
	x2=(-b-math.sqrt(d))/(2*a)
	print("Solución x1 es", x1)
	print("Solución x2 es", x2)
