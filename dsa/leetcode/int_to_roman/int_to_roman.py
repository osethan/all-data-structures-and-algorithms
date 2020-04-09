
def int_to_roman(num):
  """
  Convert an integer to a roman number.
  """

  roman = {
      '1': 'I',
      '4': 'IV',
      '5': 'V',
      '9': 'IX',
      '10': 'X',
      '40': 'XL',
      '50': 'L',
      '90': 'XC',
      '100': 'C',
      '400': 'CD',
      '500': 'D',
      '900': 'CM',
      '1000': 'M'
  }
  romanFigs = []
  for i, digit in enumerate(str(num)[-1::-1]):
      tensDigit = str(int(digit) * 10 ** i)
      if tensDigit in roman:
          romanFigs.append(roman[tensDigit])
      else:
          romanFigs.append(addToRoman(roman, int(tensDigit)))
  return ''.join(romanFigs[-1::-1])


def addToRoman(roman, tensDigit):
  romanFig = ''
  while tensDigit > 0:
      for key in list(roman.keys())[-1::-1]:
          if tensDigit < int(key):
              continue
          romanFig += roman[key]
          tensDigit -= int(key)
  return romanFig
