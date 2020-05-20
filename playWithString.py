# string = "Let's have a simple string to be reversed and then we'll apply upper case function to the reversed string."
string = input ("Enter a string to be transformed: ")
upperCasedStrReversed = (''.join(reversed(string))).upper()
print("Your string after peculiar trnsformation: " + upperCasedStrReversed)
