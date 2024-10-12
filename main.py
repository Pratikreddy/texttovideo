from director import script
from image_generation import image_generator
from audio_generation import generate_audio_clips
import json
import os
import requests
import subprocess  # For running ffmpeg command
from datetime import datetime
from moviepy.editor import TextClip, CompositeVideoClip, ImageClip, concatenate_videoclips

url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro-latest:generateContent?key=AIzaSyC8tc7m4TkAmfOx9cu_bckCc62ZgVDzSBQ"

# Prompting the user for input
context = input("Enter the context along with the Item name: ")


# this would be some pre research.
reqdata = {
    "item": f"{context}",
    "context": "Provide some context or specific detail you want to focus on",
    "origin": "Discuss the geographic and historical origin of the item",
    "inventor": "Identify the inventor(s) or creator(s) if applicable",
    "initial_adoption": "Describe how and where it was first adopted or popularized",
    "manufacturing_process": "Explain how the item is made or produced",
    "cultural_impact": "Analyze the cultural significance or impact of the item",
    "technological_influence": "Discuss any technological influence or advancements due to the item",
    "economic_importance": "Reflect on the economic relevance of the item, including market impact",
    "environmental_impact": "Address any environmental considerations or impacts",
    "legal_aspects": "Mention any notable legal battles or patent issues related to the item",
    "modern_day_usage": "Describe current uses and applications",
    "evolution_over_time": "Trace the evolution or changes in design, function, or popularity over time",
    "future_prospects": "Speculate on future developments or directions for the item"
}

# Predefined JSON structure
expected_format = {
    "title": "suggest a title for the video based on the item",
    "segments": [
        {
            "start_time": 0,
            "end_time": 5,
            "text_1": "Introduce the item with fact and a brief overview.",
            "visual_prompt_1": "engaging image representing the item"
        },
        {
            "start_time": 6,
            "end_time": 10,
            "text_2": "Discuss the historical and geographical origin of the item.",
            "visual_prompt_2": "image depicting the origin or early use"
        },
        {
            "start_time": 11,
            "end_time": 15,
            "text_3": "Describe the inventor or creator, if applicable.",
            "visual_prompt_3": "image of the inventor or relevant patent"
        },
        {
            "start_time": 16,
            "end_time": 20,
            "text_4": "Explain the initial adoption and spread of the item.",
            "visual_prompt_4": "image showing early adoption or spread"
        },
        {
            "start_time": 21,
            "end_time": 25,
            "text_5": "Analyze the impact on technology or culture.",
            "visual_prompt_5": "image that illustrates its impact"
        },
        {
            "start_time": 26,
            "end_time": 30,
            "text_6": "Discuss current applications and uses.",
            "visual_prompt_6": "modern image showing its use today"
        },
        {
            "start_time": 31,
            "end_time": 35,
            "text_7": "Address environmental and ethical considerations.",
            "visual_prompt_7": "image relevant to these considerations"
        },
        {
            "start_time": 36,
            "end_time": 40,
            "text_8": "Speculate on future developments or trends.",
            "visual_prompt_8": "image depicting future potential"
        }
    ]
}

modelbrief = {
    "model_name": "DALL-E 2",
    "description": "An advanced AI image generation model from OpenAI that creates detailed and realistic images from textual descriptions.",
    "strengths": [
        "Produces high-quality, photorealistic images, often surpassing the detail and style requested.",
        "Capable of complex image generation, combining elements creatively in new ways which feel almost like human intelligence.",
        "Supports inpainting and outpainting, allowing modifications and expansions of existing images with context-aware understanding of the scene.",
        "Efficiently generates multiple image variations quickly, offering creative flexibility and rapid prototyping for visual content."
    ],
    "weaknesses": [
        "Struggles with abstract or conceptual prompts, occasionally producing inconsistent or surreal results.",
        "While improving, it still faces challenges in areas requiring historical or factual precision without specific guidance.",
        "Limited ability to generate certain types of images due to ethical and safety filters, such as political figures or sensitive topics.",
        "Can still produce visual artifacts or anomalies, especially in complex scenes or when dealing with intricate details."
    ],
    "best_uses": [
        "Ideal for creating engaging visual content for marketing, educational, and entertainment purposes.",
        "Useful in design and architecture for visualizing renovations, products, or new concepts.",
        "Supports creative projects, allowing artists and creators to experiment with styles and concepts beyond their manual capabilities."
    ],
    "limitations": [
        "Not suitable for creating accurate maps, graphs, or other specific informational graphics.",
        "May not always adhere to strict historical or factual accuracy without highly detailed prompts.",
        "Content generation is restricted to avoid generating harmful or misleading images.",
        "The need for careful prompt design to avoid unwanted or unexpected elements in the generated images."
    ]
}
modelbrief2 = {
    "model_name": "DALL-E-3",
    "description": "An advanced AI image generation model from OpenAI that creates highly detailed and realistic images from textual descriptions. It integrates closely with ChatGPT for enhanced prompt refinement.",
    "strengths": [
        "Exceptional at generating high-resolution images, offering significant improvements over its predecessor in terms of detail and fidelity.",
        "Enhanced ability to interpret and generate images from detailed prompts thanks to integration with ChatGPT, which helps refine inputs for better results.",
        "Capable of creative image manipulations such as inpainting and outpainting, allowing for extensive modifications and expansions of existing images.",
        "Supports various image styles and sizes, offering flexibility in output that can cater to specific aesthetic or practical needs."
    ],
    "weaknesses": [
        "Complex or abstract concepts can sometimes challenge the model, leading to unpredictable or less accurate renditions.",
        "While it has safety protocols to prevent generating inappropriate content, these can also limit the scope of creative outputs in sensitive areas.",
        "Requires refined prompt engineering to achieve the best results, which might pose a learning curve for new users.",
        "Some users have noted occasional issues with image consistency, especially when dealing with very detailed or nuanced prompts."
    ],
    "best_uses": [
        "Ideal for professional artists, designers, and content creators who need high-quality visuals for projects or presentations.",
        "Useful in marketing and advertising for generating compelling visual content quickly and cost-effectively.",
        "Supports educational and research activities where visual representation can enhance understanding and engagement."
    ],
    "limitations": [
        "Not suitable for generating explicit or potentially harmful content due to ethical guidelines and restrictions.",
        "May not always handle highly abstract artistic concepts effectively, requiring more literal or clearly defined prompts.",
        "The quality of results can vary based on the specificity and clarity of the prompts provided by the user."
    ]
}
modelbrief3 = {
    "model_name": "gTTS",
    "description": "Google Text-to-Speech (gTTS) is a Python library and CLI tool that interfaces with Google's Text-to-Speech API. It converts text into natural-sounding spoken audio. gTTS supports multiple languages and is commonly used in applications that require spoken feedback or audio content.",
    "strengths": [
        "Supports a wide range of languages, making it versatile for international applications.",
        "Produces clear and natural-sounding voice outputs, enhancing user engagement and understanding.",
        "Easy to integrate with Python applications, beneficial for rapid development and deployment.",
        "Lightweight and requires minimal setup, accessible even for beginners in programming."
    ],
    "weaknesses": [
        "Dependent on internet connectivity, as it needs to contact Google's servers to generate audio.",
        "Limited control over voice modulation and emotional intonation compared to more advanced speech synthesis tools.",
        "Usage limits and potential costs associated with Google's API, depending on the scale of usage."
    ],
    "adaptations": [
        "Adapt the length of text to ensure compatibility with the audio duration specified in video segments.",
        "Generate succinct and clear audio segments that align with the visual content's timing and pacing."
    ],
    "limitations": [
        "Not suitable for applications requiring offline capabilities, as it cannot function without an internet connection.",
        "Lacks advanced features like speech emotion or different speaking styles, which are available in more specialized TTS systems.",
        "While it supports many languages, the quality of speech generation can vary between them."
    ]
}

system_instructions = [
        "Output strictly valid JSON only. Ensure the text fields are concise to fit within the designated timestamps for audio. the timestampse are in seconds",
        "Maintain key integrity; ensure all fields are accurately populated.",
        "Ensure a high correlation between visual prompts and the narrative text to enhance content relevance and viewer engagement.",
        " strictly output only 13 words per 5 seconds for text_n field",
        "follow the models strengths and weknesses carefully",
        "use the follow along lines so all my content can have a theme"
    ]
# Joining the instructions into a single string with each instruction on a new line for clarity
system_prompt = "Please follow these instructions:\n" + "\n".join(system_instructions)
# Constructing user prompt
userprompt = f"strict instructions: {context}. Here's the expected_format: {json.dumps(expected_format)}. follow along the lines of : {reqdata}. remember this script will be used to generate media from visual_prompt_n using the model: {modelbrief} and will produce audio from text_1 using the model: {modelbrief3}."

response = script(system_prompt, userprompt, url)
content = json.dumps(response)
#print (content)

response_json = json.loads(response)# Store the title in a variable
title = response_json['title']
# Store the segments as a list
segments = response_json['segments']

# Output the stored data
print("Title:", title)
print("Segments:", json.dumps(segments, indent=4))

visual_prompts = [segment[f'visual_prompt_{i+1}'] for i, segment in enumerate(segments)]

# Generating images
images_urls = image_generator(visual_prompts)

print(images_urls)

# Creating a directory with the current timestamp
dir_name = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
print(dir_name)
os.makedirs(dir_name, exist_ok=True)

#download urls
for idx, url in enumerate(images_urls):
    response = requests.get(url)
    file_path = os.path.join(dir_name, f"image_{idx+1}.png")
    if response.status_code == 200:
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded and saved: {file_path}")
    else:
        print(f"Failed to download image from {url}")

# Creating video clips from images
def create_video_clip(image_paths, fixed_duration=6):
    clips = [ImageClip(image).set_duration(fixed_duration) for image in image_paths]
    return concatenate_videoclips(clips, method="compose")


def add_subtitles(video, segments):
    composite_clips = [video]  # Start with the main video clip
    for idx, segment in enumerate(segments):
        text = segment.get(f'text_{idx+1}', '')  # Extract text
        start_time = segment.get('start_time', 0)
        end_time = segment.get('end_time', start_time + 5)  # Default duration 5 seconds

        # Creating the subtitle clip
        subtitle_clip = TextClip(
            text, fontsize=60, color='white', font='Impact',
            size=(video.size[0] * 0.8, None),  # Set width to 80% of the video width
            method='caption', align='South', stroke_color='orange2', stroke_width=3.5,
        )

        # Set subtitle clip start and duration times
        subtitle_clip = subtitle_clip.set_start(start_time).set_duration(end_time - start_time)

        # Set position to center and make sure it maintains 10% margin
        subtitle_clip = subtitle_clip.set_position(('center', 'bottom')) #horizontal,vertical

        composite_clips.append(subtitle_clip)
        print("subtitles added")
    
    # Return a composite clip that includes the video and subtitles
    return CompositeVideoClip(composite_clips)

# Creating final video with ffmpeg
def create_final_video(composite_video, audio, output_path):
    temp_video_path = output_path.replace('.mp4', '_temp.mp4')
    composite_video.write_videofile(temp_video_path, codec="libx264", fps=24)
    audio.write_audiofile(output_path.replace('.mp4', '_temp_audio.mp3'))
    ffmpeg_command = [
        'ffmpeg',
        '-i', temp_video_path,
        '-i', output_path.replace('.mp4', '_temp_audio.mp3'),
        '-c:v', 'copy',
        '-c:a', 'aac',
        '-strict', 'experimental',
        output_path
    ]
    subprocess.run(ffmpeg_command, check=True)


temp_audio_dir = os.path.join(dir_name, 'temp_audio')
os.makedirs(temp_audio_dir, exist_ok=True)

image_files = [os.path.join(dir_name, f"image_{i+1}.png") for i in range(len(images_urls))]
image_durations = [(item['end_time'] - item['start_time']) for item in segments]

initial_video = create_video_clip(image_files)
subtitled_video = add_subtitles(initial_video, segments)
audio_clips = generate_audio_clips(segments, temp_audio_dir)
final_video_path = os.path.join(dir_name, f"{title}_final.mp4")
create_final_video(subtitled_video, audio_clips, final_video_path)

print(f"Final video with subtitles and audio saved to {final_video_path}")
