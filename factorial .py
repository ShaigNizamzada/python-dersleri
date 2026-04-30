def factorial(n):
    result=1
    for i in range (1,n+1):
      result *=i
    return result

value=int(input("Faktoriyelini hesaplamak istediğiniz sayıyı giriniz: "))
print (value, "sayisinin faktoriyeli:", factorial(value))