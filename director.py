import json
import requests

def script(system_prompt, userprompt, url):
    payload = json.dumps({
        "contents": [
            {
                "parts": [
                    {"text": f"{system_prompt}"},
                    {"text": f"{userprompt}"},
                ]
            }
        ],
        "generationConfig": {
            "response_mime_type": "application/json"
        }
    })

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    
    # Parse the JSON response
    response_data = response.json()
    
    # Extract the 'text' value from the first candidate's content
    text_value = response_data["candidates"][0]["content"]["parts"][0]["text"]
    
    return text_value  # Return the extracted string