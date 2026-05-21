# Create Dictionary
student = {
    "name": "Vikas",
    "age": 20,
    "course": "Python"
}

print(student)


# ...................................
# Access Specific Data
print(student["name"])

# ....................
# Update Data
student["age"] = 21

print(student)

# ..............................................
# Add New Data
student["city"] = "Delhi"

print(student)

# ...........................................
# Delete data
del student["age"]
print(student)




# .....................................
# Nested Dictionary
user = {
    "name": "Vikas",
    "social": {
        "instagram": "vikascodilogy",
        "youtube": "Codilogy"
    }
}

print(user["social"]['youtube'])
