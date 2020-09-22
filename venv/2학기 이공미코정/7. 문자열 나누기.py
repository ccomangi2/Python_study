ticker = "btc_krw"
print(ticker.split("_"))

def 문자열쪼개기(string, sep):
   result = string
   for i in range(len(string)):
      result = string.split(sep)
   return result


phone_number = "010-1111-2222"
a = 문자열쪼개기(phone_number, "-")
print(a)