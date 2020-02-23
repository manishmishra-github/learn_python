var_string = "hello world how are you doing!!!"
			 #[01234567........................]	
#strings are immutable data types in python, means it can not be changed once defined.

print(var_string)
print(var_string[2:4]) #excludes upper limit i.e 4
print(var_string[::-1]) #reverse string
print(var_string[::2]) #skip one letter

#var_string[2] = 'p' #will give error coz updation is not allowed.
var_string = "HEllo" #it can be reassigned.

#string methods
print(var_string.title()) #capitalizes first character of every word.
print(var_string.upper())
#del(var_string)	#deltes the string from memory #can not delete a character i.e del(var_string[2]). 
print(var_string.lower()) #hence error

