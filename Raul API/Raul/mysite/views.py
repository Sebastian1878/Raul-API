from django.http import JsonResponse

def fibonacci(n):
    fib = [0, 1] + [0] * (n-1)
    lista = []
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]
        lista.append(fib[i])
    return lista

def fibo_view(request, n):
    result = fibonacci(n)
    return JsonResponse({'result': result})
