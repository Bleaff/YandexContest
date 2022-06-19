#Task code: (-128) - (127)
#Checker && Interactor: 0 - 7
#Case 1: 
# 	if (interactor == 0 || interactor == 4)  && code != 0 -> 3
# 	else if (interactor == 0) && Code == 0 -> checker
#	else if (interactor == 4) && Code == 0 -> 4
#Case 2:
#	if interactor == 1 -> checker
#Case 3:
#	if interactor == 6 -> 0
#Case 4:
#	if interactor == 7 -> 1
#Case 5:
#	else -> interactor

def conclusion(interactor, code, checker):
	if (interactor == 0 or interactor == 4)  and code != 0:
		return 3
	elif (interactor == 0) and code == 0:
		return checker
	elif (interactor == 4) and code == 0:
		return 4
	elif interactor == 1:
		return checker
	elif interactor == 6:
		return 0
	elif interactor == 7:
		return 1
	else:
		return interactor

code = int(input())
i = int(input())
check = int(input())
print(conclusion(i, code, check))
	
	

