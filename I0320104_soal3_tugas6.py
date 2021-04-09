for num in range(10, 25):
     for i in range (2, num):
         if num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
             print( num, 'bukan prima')
             break

         else:
             print(num, 'adalah bilangan prima')
             break



