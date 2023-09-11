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

# not enough tokens with -> openaiModel = "gpt-3.5-turbo"
# 16k tokens
openaiModel = 'gpt-3.5-turbo-16k-0613'

# messages is conversation thread  
messages = [ {"role": "system", "content": 
              "You are a intelligent assistant."} ]
messagesBase = [ {"role": "system", "content": 
              "You are a intelligent assistant."} ]

apiTimeout = 60 # in case openapi not responding which seems to be common. Sometimes if request too big.
interactiveMode=False

# get OpenAPI reply for request
def getReply(messages, request):
    
    messages.append(
            {"role": "user", "content": request},
        )

    # if the call times out it's usually because the conversation or response gets too big
    chat = openai.ChatCompletion.create(
        model=openaiModel, 
        messages=messages,
        request_timeout=apiTimeout
    )    
    reply = chat.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    return messages, reply


import csv
import os

# Function to open the CSV file for writing and return the writer object
def open_csv_file(filename):
    return open(filename, mode='a', newline='')

# Function to append data and label to a CSV file
def append_to_csv(writer, data, label):
    # Create a CSV writer using the provided file object
    csv_writer = csv.writer(writer)
    
    # Write a new row with the data and label
    csv_writer.writerow([data, label])

# default filename
filename = 'entityData.csv'

# Define a list of prompt and label strings with corresponding index values
numberToGenerate = 50
callIterations = 10
placeLabelsInDirectories=False

prompt_prefix =f"generate {numberToGenerate} random"
prompt_instruction = "Do not number the output adding any extra characters or give any text before or after the list"

prompt_list = [
    "IP addresses.",
    "single names.",
    "host names that may contain a digits, underscores or hyphens.",
    "integers between 0 and 1000000 in different formats.",
    "real numbers between 0 and 1000000 in different formats.",
    "dates in different formats.",
    "times in different formats.",
    "sequences of punctuation of length 1 to 3 characters.",
    "english words.",
    "nonsense words.",
    "nonsense characters between 1 and 5 characters."    
    ]

label_list = [
    "IPAddr",
    "Name",
    "HostName",
    "Integer",
    "Real",
    "Date",
    "Time",
    "Punctuation",
    "Word",
    "Nonsense",
    "RandomChars"
    ]

# interactive usage code example
if interactiveMode:
    while True:
        message = input("User : ")
        if message:
            messages, reply = getReply(messages, message)
        print(f"ChatGPT: {reply}")    
    quit()

# normal programmatic mode

# Get the current working directory if we will be writing files in subdirectories
original_directory = os.getcwd()

# use up too many tokens with too big a result so make multiple calls
for j in range(callIterations):

    #reset conversation so we don't get too much context and use too many tokens.
    messages=messagesBase
    
    # walk through prompts
    for i in range(len(prompt_list)):

        # Access each string using the index and perform an action
        prompt = prompt_prefix+" "+prompt_list[i]+" "+prompt_instruction
        label = label_list[i]
        print(label," ",prompt)

        if placeLabelsInDirectories:
            # Put data in subdirectories to stage for training
            # Return to the original directory
            os.chdir(original_directory)
            new_directory_name = label
            os.makedirs(new_directory_name, exist_ok=True)
            # Change the current working directory to the new directory
            os.chdir(new_directory_name)
            filename = label+".csv"

        # open file for append
        file = open_csv_file(filename)

        # run function
        messages, reply = getReply(messages, prompt)
        replies = reply.splitlines()
        print (label," ",replies[0])

        # Iterate through the list of reply lines and print each line separately with index label
        for reply in replies:
            if placeLabelsInDirectories:
                append_to_csv(file, reply)
            else:
                append_to_csv(file, reply, label)
            

quit()

