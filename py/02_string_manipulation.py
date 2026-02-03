single_quote = 'Hello'
double_quote = "World"
triple_quote = """Multi-line
string"""

print(single_quote)
print(type(single_quote))
print(double_quote)
print(type(double_quote))
print(triple_quote)
print(type(triple_quote))

print(single_quote[0])      #first character
print(single_quote[-1])     #last character
print(single_quote[0:6])    #from start to 5th character
print(single_quote[:6])     #from start to 5th character too
print(triple_quote[7:])     #from 8th charater to finish