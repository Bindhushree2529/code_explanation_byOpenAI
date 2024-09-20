# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 09:05:11 2024

@author: sanih
"""

from openai import OpenAI
client = OpenAI()

instruction = """Explain what this Python code does in one sentence:
number = int(input("Enter a number:"))
primeFlag = True
for i in range(2, number):
    if number % i == 0:
        primeFlag = False
        break
if primeFlag == True:
    print(number, " is prime.")
else:
    print(number, " is not prime.")
"""


response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": instruction
        }
      ]
    },
  
  ],
  
   
  max_tokens=300,
  
)

print(response.choices[0].message.content) 
