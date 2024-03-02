"""
	__author__	: codelocked
	__desc__	: String Formatting in Python
	__date__	: Since Oct 2023
"""

# formatting
# --> % 
# --> format inbuilt method
# --> f-strings
# --> template based formating


'''

# Formatting string using % Operator
sentence = "My name is %s and I am belong to %s world. And this is in year %d." % ('raahool','codelocked')
print(sentence)

# Formatting string using format Method
sentence = "My name is {0} and I am belong to {1} world. And this is in year {2}.".format(
    'raahool','codelocked', 2023 )
print(sentence)


sentence = "My name is {0} and I am belong to {1} world. And this is in year {2}.".format(
	'raahool','codelocked', 2023)
print(sentence)



'''
# Stuff related to html
tag = 'h1'
text = "something here"

sentence = f"""
<html>
	<body>
		<{tag}>{text}</{tag}
	</body>
</html>"""


print(sentence)

'''

sentence = "My name is {name} and I am belong to {name} world. And this is in year {year}.".format(
	name='codelocked', year='2023')
print(sentence)



for i in range(1,11):
	print('The value is {:03}'.format(i))



pi = 3.1445654654
print('Pi is equal to {:.2f}'.format(pi))




print(' 1 MB is equal to {:,.2f} bytes'.format(1024**2))

'''
# Understanding Python f-string


