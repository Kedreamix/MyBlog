from g4f.client import Client

client = Client()
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", 
         "content": "You are a helpful assistant."},
         {"role": "assistant", 
          "content": "Hello, how can I help you today?"},
          {"role": "user", 
           "content": "Hello"}],
    # ...
)
print(dir(response))
# print(dir(response.usage))
print(response.choices)
# print("prompt_token_used:", response.usage.prompt_tokens,
#       "completion_token_used:", response.usage.completion_tokens,
#       "total_token_used:", response.usage.total_tokens)
# print("response_time:", response.response_ms / 1000.0, 's')
print(dir(response.choices[0]))
print(response.choices[0].message.content)