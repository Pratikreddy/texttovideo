# image_generation.py
from openai import OpenAI
api_key = ""
client = OpenAI(api_key=api_key)

# Function to generate images based on visual prompts
def image_generator(prompts):
    generated_images = []
    for prompt in prompts:
        response = client.images.generate(
            model="dall-e-2",
            prompt=prompt,
            size="1024x1024",
            #quality="hd",
            quality="standard",
            n=1
        )
        image_url = response.data[0].url
        generated_images.append(image_url)
    return generated_images

