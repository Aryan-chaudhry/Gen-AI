import tiktoken

encoder = tiktoken.encoding_for_model("gpt-4o")

text = "Hey There! my name is Aryan"

tokens = encoder.encode(text)

print("Tokens", tokens)

decode = encoder.decode([25216, 3274, 0, 922, 1308, 382, 107851, 270])

print("Decoded", decode)