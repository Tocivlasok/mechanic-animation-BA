def reverseStr(strName):
	strToTransform = (''.join(reversed(strName)))
	return strToTransform

def upperCaseStr(strName):
	strToTransform = strName.upper()
	return strToTransform


if __name__ == '__main__':
	strToTransform = input ("Enter a string to be transformed: ")
	print("Your string Reversed: " + reverseStr(strToTransform))
	print("Your string UpperCased: " + upperCaseStr(strToTransform))
	print("Your string Transofrmed in peculiar way: " + upperCaseStr(reverseStr(strToTransform)))