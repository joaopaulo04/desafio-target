def verifica_fibonacci(numero):
    fib1, fib2 = 0, 1

    if numero == fib1 or numero == fib2:
        return True

    while fib2 <= numero:
        fib1, fib2 = fib2, fib1 + fib2

        if numero == fib2:
            return True

    return False

numero_digitado = int(input("Digite um número para verificar se ele pertence à sequência de Fibonacci: "))

if verifica_fibonacci(numero_digitado):
    print(f"O número {numero_digitado} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero_digitado} não pertence à sequência de Fibonacci.")
