# may need to install openapi on system
#pip install openai
import openai
import sys

# Check if the user provided a command-line argument for api key
if len(sys.argv) != 2:
    print("Usage: python .py 'Openai API Key'  eg. 'sk-NotAValidKey98DUwnbpW9bFgQR46qE'")
    sys.exit(1)

# Get the long string from the command-line argument
openai.api_key = sys.argv[1]
print("Using key: "+openai.api_key)

#openai.api_key = ' PUT VALID KEY HERE '
#print("Using key: "+openai.api_key)

messages = [ {"role": "system", "content":
			"You are a intelligent assistant."} ]
while True:
	message = input("User : ")
	if message:
		messages.append(
			{"role": "user", "content": message},
		)
		chat = openai.ChatCompletion.create(
			model="gpt-3.5-turbo", messages=messages
		)
	reply = chat.choices[0].message.content
	print(f"ChatGPT: {reply}")
	messages.append({"role": "assistant", "content": reply})

