#formatting strings i.e add variables to a string.
format_sring = "h"
second = "hello again "
#print without /n at end
print (f"{format_sring} {second}",end = "") #f strings or formatted strings.

#rstrip lstrip strips whitespaces from right and left of string
format_sring = format_sring.lstrip()
second = second.rstrip()
print (f"{format_sring} {second}",end = " manish\n") #f strings or formatted strings.

#endswith("string to be checked",starting index,ending index+1) -->excludes upper limit.
print(format_sring.endswith("world"))
print(format_sring.endswith("h",0,1))
#similarly startswith("prefix",starting index, ending index+1) -->excludes upper limit.
