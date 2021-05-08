-- Project Euler Problem 5

-- greatest common divisor
function gcd(a, b)
   if b == 0 then
      return a
   end
   return gcd(b, a % b)
end

-- lowest common multiple
function lcm(a, b)
   return a * b / gcd(a, b)
end

result = 1
for i = 1, 20 do
   result = lcm(i,result)
end

print(result)
