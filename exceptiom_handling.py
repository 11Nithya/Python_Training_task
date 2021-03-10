#Write a code for reading a file ( all exceptions handled )

s="hello"
try:
    f=open("read.txt","r")
    f_contents=f.read()
    print(f_contents)

except Exception as e:
    print(e)

else:
    print("no error")

finally:
    print("end")
