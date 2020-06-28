  print('                 1')
  class RomanNumber(int):
      def __new__(cls, value, base=10):
          try:
              return super(cls, cls).__new__(cls, value)
          except:
              val = cls.to_int(value.upper())
              return super(cls, cls).__new__(cls, val)

      def to_int(value):
          roman = {
              'M': 1000, 'CM': 900, 'D': 500,
              'CD': 400, 'C': 100, 'XC': 90,
              'L': 50, 'XL': 40, 'X': 10,
              "IX": 9, 'V': 5, 'IV': 4, "I": 1
          }
          ready = 0
          for i in range(len(value)):
              try:
                  if value[i]+value[i+1] in roman:
                      ready += roman[ value[i]+value[i+1] ]
                  else:
                      raise Exception
              except:
                  ready += roman[value[i]]
          return ready

  roman_number = RomanNumber('MXXXVIII')
  print(
      f'''{roman_number + roman_number}
  {roman_number - roman_number}
  {roman_number / roman_number}
  {roman_number * 2}
  {roman_number > roman_number+1}
  {roman_number < roman_number+1}
  {roman_number >= roman_number}'''
  )

print('                 2')
class Range:
    def __init__(self, start, end=0, step=1):
        if not end:
            self.end = start-1
            self.start = -1
        elif step < 0:
            self.start = start+1
            self.end = end+1
        else:
            self.start = start-1
            self.end = end-1

        if not step:
            raise ValueError('step must not be 0')
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.end and self.step > 0:
            raise StopIteration
        
        if self.start <= self.end and self.step < 0:
            raise StopIteration

        self.start += self.step
        return self.start

for i in Range(1, 10):
   print(i)

 print('                 3')
 class Str(str):
     def __new__(cls, val):
         return super(cls, cls).__new__(cls, val)

     def __matmul__(self, other):
         return f'{self}@{other}.com'
    
     def __rmatmul__(self, other):
         return self.__matmull__(other, self)

     def __truediv__(self, other):
         return f'{self}/{other}'

     def __rtruediv__(self, other):
         return self.__truediv__(other, self)

 path = Str('path')
 prefix = Str('usr')
 print(prefix / path)

 gmail = Str('gmail')
 mail = Str('mail')
 print(mail @ gmail)
