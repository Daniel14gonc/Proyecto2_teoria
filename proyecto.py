alpha = lambda x: x + 1
beta = lambda x: 2 * x

cero = lambda f: lambda x: x
uno = lambda f: lambda x: f(x)
dos = lambda f: lambda x: f(f(x))
tres = lambda f: lambda x: f(f(f(x)))
cuatro = lambda f: lambda x: f(f(f(f(x))))
cinco = lambda f: lambda x: f(f(f(f(f(x)))))

sucesor = lambda n: lambda f: lambda x: f(n(f)(x))
suma = lambda a: lambda b: lambda f: lambda x: a(f)(b(f)(x))
multiplicacion = lambda a: lambda b: lambda f: lambda x: a(b(f))(x)
potencia = lambda a: lambda b: lambda f: lambda x: b(a)(f)(x)


# Alpha

print(dos(alpha)(0))
print("Sucesor de dos: ", sucesor(dos)(alpha)(cero(alpha)(0)))
print("4 + 3: ", suma(cuatro)(tres)(alpha)(cero(alpha)(0)))
print("5 * 3: ", multiplicacion(cinco)(tres)(alpha)(cero(alpha)(0)))
print("4 ^ 3: ", potencia(cuatro)(tres)(alpha)(cero(alpha)(0)))