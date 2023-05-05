#https://platform.openai.com/account/api-keys
#Go to this link and make your own api key and paste it in 5th line

import openai
openai.api_key = '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'
model_engine = "text-davinci-003"
prompt = input("🤖 How can I help you?\n")

while prompt.lower() not in ("no", "n", "no!", "you can't", "you cant", "nothing"):
    
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    response = completion.choices[0].text
    print(f'🤖 {response}')
    
    prompt = input("🤖 What else can I help you with?\n")

print("🤖...")