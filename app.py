from firefly import Firefly

from helpers import setup_sentry

setup_sentry()
app = Firefly()

@app.function
def fib(n):
    if n==0 or n==1: return n
    if n>10: raise ValueError('n greater than 10 not allowed')
    return fib(n-1) + fib(n-2)

if __name__ == "__main__":
    app.run()
