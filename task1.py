import re

commonPass=["password"," 12345"," qwerty"," admin"]

def pass_strength(password,user=None):
    if len(password)<8:
        return "Weak" ,2,"Password's must be 8 charachter!"
    
    if not (re.search(r"[a-z]",password))and re.search(r"[A-z]",password) and re.search(r"\d",password) and re.search(r"[!@#$%^&*():|><?]{}",password):
        return "Weak",3,"Password must contain 1 lower case,1upper case letter,1 digit and 1 special charachter"

    if password.lower() in commonPass:
        return "Weak",3,"Common password!"
    
    if user and password.lower() == user.lower():
        return "Weak",2,"Password should not be the same as username."
    
    score=10
    if len(password)<10:
        score-=2
        if not re.search(r"[a-z]",password) and re.search(r"[A-z]",password) and re.search(r"\d",password) and re.search(r"[!@#$%^&*():|><?]{}",password):
          score-=3
        if password.lower() in commonPass:
            score-=3
    if score > 8:
        passstrength="Strong"
    elif score >= 5:
        passstrength="Medium"
    else:
        passstrength="Weak"
    return passstrength,score ,"Password's valid" 
user=input("Enter username: ")
password=input("Enter you password: ")
passstrength,score,results=pass_strength(password,user)
print(f"Password Strength: {passstrength}")
print(f"Score:  {score} /10")
print(f"Results: {results}")
