def is_punctuator(ch):
  file_path = "D:\python project\project\lexical-analyzer\punctuators.txt"
  with open(file_path, 'r') as file:
    content = file.read()

    return ch in content


def valid_identifier(string):
  if string[0].isdigit() or is_punctuator(string[0]):
    return False
  return all(not is_punctuator(ch) for ch in string[1:])


def is_operator(ch):
  file_path1 = "D:\python project\project\lexical-analyzer\operators.txt"
  with open(file_path1, 'r') as file:
    content1 = file.read()
  return ch in content1


def is_keyword(string):
  file_path2 = "D:\python project\project\lexical-analyzer\keywords.txt"
  with open(file_path2, 'r') as file:
    content3 = file.read()
  return string in content3


def is_number(string):
  numOfDecimal = 0
  for ch in string:
    if numOfDecimal > 1 and ch == '.':
      return False
    elif numOfDecimal <= 1 and ch == '.':
      numOfDecimal += 1
    elif not ch.isdigit() and (ch != '-' or string.index(ch) != 0):
      return False
  return True


def parse(string):
  left = 0
  right = 0
  length = len(string)
  while right < length and left <= right:
    if not is_punctuator(string[right]):
      right += 1
    elif is_punctuator(string[right]) and left == right:
      if is_operator(string[right]):
        print(string[right], "IS AN OPERATOR")
      right += 1
      left = right
    elif is_punctuator(string[right]) and left != right or (right == length
                                                            and left != right):
      sub = string[left:right]
      if is_keyword(sub):
        print(sub, "IS A KEYWORD")
      elif is_number(sub):
        print(sub, "IS A NUMBER")
      elif valid_identifier(sub) and not is_punctuator(string[right - 1]):
        print(sub, "IS A VALID IDENTIFIER")
      elif not valid_identifier(sub) and not is_punctuator(string[right - 1]):
        print(sub, "IS NOT A VALID IDENTIFIER")
      left = right


c = '''def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

number = 17
if is_prime(number):
    print(number, "is a prime number")
else:
    print(number, "is not a prime number")
    '''

parse(c)
