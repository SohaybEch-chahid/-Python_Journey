# -------------------
# -- Loop => While --
# -------------------
# while condition_is_true
#   Code Will Run Until Condition Become False
# -----------------------

a = 0

while a < 15:

    print(a)

    a += 1  # a = a + 1

print("Loop is Done")  # True Become False

# while False:

# print("Will Not Print")

# -----------------
# -- Loop => For --
# -----------------
# for item in iterable_object :
#   Do Something With Item
# -----------------------------
# item Is A Vairable You Create and Call Whenever You Want
# item refer to the current position and will run and visit all items to the end
# iterable_object => Sequence [ list, tuples, set, dict, string of charcaters, etc ... ]
# ---------------------------------------------------------------

myNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in myNumbers:

    # print(number * 17)

    if number % 2 == 0:  # Even

        print(f"The Number {number} Is Even.")

    else:

        print(f"The Number {number} Is Odd.")

else:

    print("The Loop Is Finished")

myName = "Osama"

for letter in myName:

    print(f" [ {letter.upper()} ] ")

# -----------------
# -- Loop => For --
# -- Nested Loop --
# -----------------

peoples = ["Osama", "Ahmed", "Sayed", "Ali"]

skills = ["Html", "Css", "Js"]

for name in peoples:  # Outer Loop

    print(f"{name} Skills Is: ")

    for skill in skills:  # Inner Loop

        print(f"- {skill}")

# Dictionary

peoples = {
    "Osama": {"Html": "70%", "Css": "80%", "Js": "70%"},
    "Ahmed": {"Html": "90%", "Css": "80%", "Js": "90%"},
    "Sayed": {"Html": "70%", "Css": "60%", "Js": "90%"},
}

print(peoples["Osama"])
print(peoples["Ahmed"])
print(peoples["Sayed"])

print(peoples["Osama"]["Css"])
print(peoples["Ahmed"]["Css"])
print(peoples["Sayed"]["Css"])

for name in peoples:

    print(f"Skills and Progress For {name} Is: ")

    for skill in peoples[name]:

        print(f"{skill.upper()} => {peoples[name][skill]}")

# ------------------------------
# -- Advanced Dictionary Loop --
# ------------------------------

mySkills = {"HTML": "80%", "CSS": "90%", "JS": "70%", "PHP": "80%"}

print(mySkills.items())

#######################

for skill in mySkills:

    print(f"{skill} => {mySkills[skill]}")

#######################

for skill_key, skill_progress in mySkills.items():

    print(f"{skill_key} => {skill_progress}")

#######################

myUltimateSkills = {
    "HTML": {"Main": "80%", "Pugjs": "80%"},
    "CSS": {"Main": "90%", "Sass": "70%"},
}

for main_key, main_value in myUltimateSkills.items():

    print(f"{main_key} Progress Is: ")

    for child_key, child_value in main_value.items():

        print(f"- {child_key} => {child_value}")
