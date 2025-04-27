from time import sleep

def countdown(n):
  sleep(0.3)
  print(n)
  if n > 1:
    countdown(n - 1)


countdown(7)