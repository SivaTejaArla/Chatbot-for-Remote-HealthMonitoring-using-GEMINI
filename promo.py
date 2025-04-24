from google import genai

client = genai.Client(api_key="AIzaSyD9jPbIPfyP8lUlWoJur-OXLkylxcx0DP8")

dat = "who are you"
response = client.models.generate_content(
    model="gemini-2.0-flash", contents= dat
)
print(response.text)