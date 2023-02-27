def fibonacci(n):
    # Verifica se o número informado é igual a 0 ou 1
    if n == 0 or n == 1:
        return n
    
    # Inicia os valores da sequência com 0 e 1
    a, b = 0, 1
    
    # Calcula os valores da sequência até o valor desejado
    for i in range(2, n+1):
        c = a + b
        a, b = b, c
    
    # Verifica se o número informado pertence à sequência de Fibonacci
    if c == n:
        return f'O número {n} pertence à sequência de Fibonacci.'
    else:
        return f'O número {n} não pertence à sequência de Fibonacci.'

# Exemplo de uso
numero = int(input('Digite um número: '))
resultado = fibonacci(numero)
print(resultado)
