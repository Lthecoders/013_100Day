print("              EXAM GRADE CALCULATOR")
print("              ---------------------\n")

exam_name = input("enter the name of the exam --> ")
max_marks = int(
    input(f"\nwhat is the max marks one can score in {exam_name} ? --> "))

#personal
user_marks = float(
    input(f"\nhow much your SCORE was in that {exam_name} EXAM ? 🤔🤔----> "))

final_user_marks = ((user_marks / max_marks) * 100)
if (final_user_marks) >= 90 and (final_user_marks) <= 100:
  print("\033[32m", "\n\nyou got", final_user_marks,
        "% which is A+🥳🤯\nKEEP IT UP!!!👍", "\033[0m")
  
elif (final_user_marks) >= 80 and (final_user_marks) <= 90:
  print("\033[32m", "\n\nyou got", final_user_marks,
        "% which is A 👍🤯\nGOOD SCORE!!!👍", "\033[0m")
  
elif (final_user_marks) >= 70 and (final_user_marks) <= 80:
  print("\033[33m", "\n\nyou got", final_user_marks,
        "% which is B 👍\nNICE SCORE!!!👍", "\033[0m")
  
elif (final_user_marks) >= 60 and (final_user_marks) <= 70:
  print("\033[33m", "\n\nyou got", final_user_marks,
        "% which is C \n i hope you will do well in next exam👍", "\033[0m")
  
elif (final_user_marks) >= 50 and (final_user_marks) <= 60:
  print("\033[33m", "\n\nyou got", final_user_marks,
        "% which is D \n very poor performace😕😕", "\033[0m")
  
elif (final_user_marks) < 50:
  print("\033[31m", "\n\nyou got", final_user_marks,
        "% which is U \nYou are fail buddy😕😕", "\033[0m")
else:
  print(
      "\033[31m",
      "\n\nwrong input😒 make sure your percentage in decimal and in number form. upto 100 ONLY",
      "\033[0m")