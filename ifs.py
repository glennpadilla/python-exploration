age = 16

if age > 17:
    print("You can buy a lottery ticket.")
    print("How many would you like?")
else:
    print("You may not buy a lottery ticket.")
    print("Can I interest you in some candy?")

print("Thank you for your patronage.")

age = 5

if age > 12 and age < 20:
    is_teenager = True
else:
    is_teenager = False

if is_teenager:
    print("Are you on TikTok?")
else:
    print("Are you on Facebook?")

this_is_false = 3 < 2
print(this_is_false)

if "":
    print("Empty string is considered true")
else:
    print("Empty string is considered false")

if 0:
    print("0 is considered true")
else:
    print("0 is considered false")

a = 3
b = 3

print(id(a))
print(id(b))

a = 3.0
b = 3

print(id(a))
print(id(b))

a = "hello"
b = "hello"

print(id(a))
print(id(b))

a = [1,2,3,4]
b = [1,2,3,4]

print(id(a))
print(id(b))

a = (1,2,3,4)
b = (1,2,3,4)

print(id(a))
print(id(b))
