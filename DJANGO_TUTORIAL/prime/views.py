from django.shortcuts import render

# Create your views here.
def generate_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        is_prime = all(num % p != 0 for p in primes)
        if is_prime:
            primes.append(num)
        num += 1
    return primes

def index(request):
  amount = 5
  context = {
    'judul':'nwr class',
    'subjudul':'nwr27',
    'nav':[
      ['/', 'home'],
      ['/about', 'about'],
      ['/blog', 'blog'],
      ['/contact', 'contact'],
    ],
    'amount': amount,
    'primes': generate_primes(amount),
  }
  return render(request, 'prime/index.html', context)