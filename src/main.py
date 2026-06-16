from agents.intake_agent import intake
from parsers.text_parser import read_text_file

user_query = read_text_file("data/user_query.txt")

info = intake(user_query)
print(info)