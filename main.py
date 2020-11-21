#Functions with outputs

# #def format_name(f_name, l_name):
#   formatted_f_name = f_name.title()
#   formatted_l_name = l_name.title()
#   return f"{formatted_f_name} {formatted_l_name}"

# formatted_string = format_name("grant", "THOMPSON")

# print(formatted_string)

#With Returns

def format_name(f_name, l_name):
  if f_name == "" or l_name == "":
    return "No name huh!?"
  formatted_f_name = f_name.title()
  formatted_l_name = l_name.title()
  return f"{formatted_f_name} {formatted_l_name}"

formatted_string = format_name("grant", "THOMPSON")

print(format_name(input("What is your first name?\n"),("What is your surname?\n")))