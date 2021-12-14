def chama_Fibonacci(n):
    a = 1
    b = 1

    if n == 1:
        print('0')
    elif n == 2:
        print('0' , '1')
    else:
        print('0')
        print(a)
        print(b)

        for indice in range(n-3):
            soma = a + b
            b = a
            a = soma

            print(soma)

chama_Fibonacci(15)