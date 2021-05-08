-- Euler Problem 2

solution = 4613732

function fib(n)
   function fibb(n, a, b)
      if n <= 1 then
         return a
      else
         return fibb(n-1, b, a+b)
      end
   end
   return fibb(n, 0, 1)
end

i=1
f=fib(i)
sum=0
while f < 4000000 do
   if f % 2 == 0 then
      sum = sum + f
   end
   i = i + 1
   f = fib(i)
end

print(sum == solution)

