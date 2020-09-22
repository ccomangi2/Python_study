def 문자열대체(string, old, new):
     result = string
     for i in range(len(string)):
         if string[i]==old:
              result = result[:i] + new + result[i+1:]

     return result


phone_number = "010-1111-2222"
a = 문자열대체(phone_number, "-", " ")
print(a)