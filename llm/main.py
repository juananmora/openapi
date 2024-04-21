from fastapi import FastAPI
import requests
import json
from openai import OpenAI
import os

app = FastAPI()

client = OpenAI(base_url="http://host.docker.internal:1234/v1", api_key="not-needed")
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/create_issue")
async def create_issue(title: str, prompt: str):

    print(f"Good! this is the title, {title}")
    print(f"Good! this is the prompt, {prompt}")
    
    token = os.getenv("JIRA_TOKEN")

    history=[
        {"role": "system", "content": "You are the scrummaster of the project. "},
        {"role": "user", "content": prompt} 
    ]

    completion = client.chat.completions.create(
        model="local-model",
        messages=history,
        temperature=0.2,
        max_tokens=1000,
        stream=True,
    )
    new_description=""
    for chunk in completion:
        if chunk.choices[0].delta.content:
            new_description += chunk.choices[0].delta.content
            print(chunk.choices[0].delta.content, end="", flush=True)

    url = "https://juananmora.atlassian.net/rest/api/3/issue"

    payload = json.dumps({
        "fields": {
            "project": {
                "key": "JON"
            },
            "summary": title,
            "description": {
                "content": [
                    {
                        "content": [
                            {
                                "text": new_description,
                                "type": "text"
                            }
                        ],
                        "type": "paragraph"
                    }
                ],
                "type": "doc",
                "version": 1
            },
            "issuetype": {
                "id": "10001"
            }
        }
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': token,
        'Cookie': 'atlassian.xsrf.token=2abe4e90b04d0e0d853e35e8812a2cb24cc6d0a5_lin'
    }


    f = open("./output/issuedescription.md", "w")
    f.write(new_description)
    f.close()
    
    response = requests.request("POST", url, headers=headers, data=payload)
    return {"message": response.text}

@app.post("/dry_run")
async def dry_run(prompt: str):
    print(f"Good! this is the prompt, {prompt}")  

    completion = client.chat.completions.create(
    model="lmstudio-community/Meta-Llama-3-8B-Instruct-GGUF",
    messages=[
        {"role": "system", "content": "Always answer in rhymes."},
        {"role": "user", "content": prompt}
    ],
    temperature=0.7,
    max_tokens=1001
    )

    print(completion.choices[0].message)
    return {"message": completion.choices[0].message}

        