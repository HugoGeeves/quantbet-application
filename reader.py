from requests_html import HTMLSession
from math import gcd

# Start a session and make a requst to the quiz page
session = HTMLSession()
quiz_response = session.get('https://quantbet.com/quiz/dev')

# Parse the response html for the quiz text and split the numbers out from it
quiz_text = quiz_response.html.find('#quiz > p:nth-child(1)', first=True).text
numbers = [int(s) for s in quiz_text.split() if s.isdigit()]

# Use the inbuilt gcd calculator to calculate gcd
magic_number = gcd(numbers[0], numbers[1])

# Send a reponse to the quiz server (found from inspecting the network on submit) and print result
quantbet_response = session.post(f'https://quantbet.com/submit', data={'divisor': magic_number})
print(quantbet_response.text)