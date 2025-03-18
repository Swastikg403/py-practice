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

 
#index(substring)
#//returns the index of the substring.raises a value error
d=text.index("world");

#isaplaha()
#// return true if all characters R EALPHABET

#isupper()
#islower()
#isnum()

#join(iterable)

#// joins th elements of an niterable with string as a
#//All elements of list must be string
#Argument pass should be iterable like list
words=["python","is","awesome"]
res=" ".join(words);
print(res)


#rstrip  remove whitspace from right
#lstrip  remove whitspace from left

#strip   remove space from both sides

#lower,upper  convert string to lower/upper


#replace(old,new)
#//replace all occurences of a subsstring with another
print(text.replace("world","python"))


#split(separator)
#// splits the string ino  list using specified separator

text="apple,banaana,orange"
print(text.split(","))


#startwith(prefix)
#//return true if string starts with tha string

#swapcase()
#\\ converts the upper into lower and vice versa

#title()
#// 


#zfill
#// pads the string with 0 on the left
tex="45"
printf(tex,zfill(5))
# 00045



#partition(separator)
#// converts the strinh into tuple by separtor

print("apple-banana-cherry",partition("-"))
#  {"apple","banana","cherry"}


#rpartition(separator)
#// does the same thing from right
# { "cherry","banana","apple"}

#rfind(substring)      returns the highest index if not found then return-1;

