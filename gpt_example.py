# gpt-api-integration/gpt_example.py

import openai

# Set up OpenAI API key
openai.api_key = 'YOUR_API_KEY'

# Example GPT-3 API call
response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Write a poem about AI.",
  max_tokens=50
)

print(response.choices[0].text.strip())
