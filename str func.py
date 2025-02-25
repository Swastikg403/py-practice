#capitalise()
 #// converts the first letter of string into uppercase
text="hello world"
new=text.capitalize()  #=>Hello world
print(new)

#casefold()
 # // converts the string to lowercase  more suitable for insensitive conversions

#centre(width,fillchar)
# //centers the string within the specified width,paddding with the specfied character
ntext="python"
result=ntext.center(10,"*")  #=> **python**
print(result)

#count(substring)
 # // returns the number of occurences of a substtring in a string
str="banana"
a=str.count("a")
print(a)

#endswith(suffix)
# // returns true if the string ends with the specified ssuffix
b=str.endswith("a")
print(b)

#find(substring)
 # // returns the lowest index of the substring .return -1 if not found
c=text.find("world")
print(c)


#format()
#// format the string using placeholders{}
final="hello,{}, you are {} years old.".format("swastik",19)
print(final)
 # no. of placeholders= no. opf arguments

 
#