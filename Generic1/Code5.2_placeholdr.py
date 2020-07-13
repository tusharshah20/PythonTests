#using formatted string & place holders
#
first = "queen"
last = "elizabeth"
#simple concatenation
msg = first + ' [' + last + '] is a queen' 
print(msg)

#{}--defining place holders in a formatted string
msgf = f'{first} [{last}] is a queen'
print(msgf)
