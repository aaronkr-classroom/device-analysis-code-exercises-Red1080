a=132 #0b10000100=1byte=8bits=2^8
b=45 #0b00101101
fmt0='{:<10}'
fmt1='0b{:08b} 0x{:02x} {:3}'
n=30
print("bitwise AND:")
print(fmt0.format('a'),fmt1.format(a,a,a))
print(fmt0.format('b'),fmt1.format(b,b,b))
print('-'*n)
print(fmt0.format('a&b'),fmt1.format(a&b,a&b,a&b))


print("bitwise OR:")
print(fmt0.format('a'),fmt1.format(a,a,a))
print(fmt0.format('b'),fmt1.format(b,b,b))
print('-'*n)
print(fmt0.format('a|b'),fmt1.format(a|b,a|b,a|b))


print("bitwise XOR:")
print(fmt0.format('a'),fmt1.format(a,a,a))
print(fmt0.format('b'),fmt1.format(b,b,b))
print('-'*n)
print(fmt0.format('a&^b'),fmt1.format(a^b,a^b,a^b))

print("bitwise AND:")
print(fmt0.format('a'),fmt1.format(a,a,a))
print('-'*n)
print(fmt0.format('~a'),
      fmt1.format(~a&0xFF,
                  ~a&0xFF,
                  ~a&0xFF))


print("bitwise leftshoft:") #<<
print(fmt0.format('a'),fmt1.format(a,a,a))
print('-'*n)
print(fmt0.format('<<2'),
      fmt1.format(a<<2&0xFF,
                  a<<2&0xFF,
                  a<<2&0xFF))

print("bitwise rightshoft:") #<<
print(fmt0.format('a'),fmt1.format(a,a,a))
print('-'*n)
print(fmt0.format('>>2'),
      fmt1.format(a>>2&0xFF,
                  a>>2&0xFF,
                  a>>2&0xFF))




