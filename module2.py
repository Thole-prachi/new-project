from sys import argv

script, user_name = argv
say = ">"

print(f"Hello {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"are you happy today {user_name}?")
happy = input(say)

print(f"where do you live {user_name} ?")
lives = input(say)

print(f"what kind of computer do you have ?")
computer = input(say)

print (f"""
       alright,so you said {happy} about liking me.
       you live in {lives}.Not sure where that is.
       and you have a {computer} computer Nice.
       """)