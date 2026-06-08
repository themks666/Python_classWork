name = "rohim"
age=34
print("name : ", name)
print("name : "+ name)
print(f"name : {name} and age : {age}")
print("name : {} and age : {}".format(name, age))         
print(f"name : {name } \n age : {age}")

print("this is a heart : \u2764")
print(name.upper())

#name1, age = input("enter anme and age ").split()
#print(name1, age)
message= "i love you "
message = message.replace("love", "hate")
print(message.startswith("love"))
print(message.split())
new_message = "i, am, manish"
print(new_message.join(","))