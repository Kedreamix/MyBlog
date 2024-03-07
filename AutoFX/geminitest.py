import google.generativeai as genai
import os
GOOGLE_API_KEY = 'AIzaSyCWiiXeTYLDm37lBbl8vgmucR_YlsG2LD8'
genai.configure(api_key=GOOGLE_API_KEY)
print(dir(genai))
model = genai.GenerativeModel('gemini-pro')
response = model.generate_content('Please summarise this document: ...')

print(response.text)