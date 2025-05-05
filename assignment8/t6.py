class PowerCalculator:
     def pow(self, x: float, n: int) -> float:
         
         if n < 0:
             x = 1 / x
             n = -n
 
         result = 1
         current_product = x
 
         while n > 0:
             if n % 2 == 1:  
                 result *= current_product
             current_product *= current_product 
             n //= 2  
 
         return result
 
 calculator = PowerCalculator()
 print(calculator.pow(2, 10))   
 print(calculator.pow(2, -3)) 
 print(calculator.pow(5, 0))    