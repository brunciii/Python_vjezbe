def je_prost(broj):
    for rezultat in range (0,broj):
        if broj%2!=0:
            return False
        else:
            return True

print(je_prost(2)) #Ispis: True
print(je_prost(10)) #Ispis: False
print(je_prost(17)) #Ispis: True
    
        
