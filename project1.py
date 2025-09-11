print("===   Welcome to the interactive personal data collector!   ===")

name=input("Enter Your Name:-")
age=int(input("Enter Youe Age:-"))
height=float(input("Enter Your Height:-"))
fav_number=int(input("Enter Your Favnumumber:-"))
int_convert=int(height)

print("===  thank you!  here is information We collected: ===")


print("Name",name,"type",type(name),"Memory Address",id(name))
print("age",age,"type",type(age),"Memory Address",id(age))
print("height",height,"type",type(height),"Memory Address",id(height))
print("fav number",fav_number,"type",type(fav_number),"Memory Address",id(fav_number))

current_year=2025
birth_year=current_year-age

print("My birth yaer is approx:",birth_year,"Based on  my age",age)

print(" ===  Thanks  For  using  the personal Data collector. Good byy! ===")