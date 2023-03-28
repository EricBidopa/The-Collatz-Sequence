def collatz(number):
    if number % 2 == 0:
        result = number / 2
        print(result)
        return result
    else:
        result = 3 * number +1
        print(result)
        return result
    
while True:
        try:
             x = int(input("Type an integer"))
             n = collatz(x)
             if n ==1:
              break
             
        except ValueError:
            print("INVALID INPUT, PLEASE ENTER AN INTEGER")
        
