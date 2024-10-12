import os
from datetime import datetime


# # Function to generate images based on visual prompts
# def image_generator(prompts, path):
    
#     for prompt in prompts:
#         # we need to call this this is inside the path /Users/p/mlx-examples/stable_diffusion
#         #prompt sample python txt2image.py --n_images 4 -q -v --output test.png "train running down the foothills of the snowy himalayas"
#        f"""python txt2image.py --n_images 1 -q -v --output "{path}".png "{prompt}"
#        """

#         # we need to return the full output paths of the images the input "path" that is coming in is actualy created by a date time func in og script 
        

# Function to generate images based on visual prompts


def image_generator(prompts, dir_path):
    generated_image_paths = []
    script_path = "/Users/p/mlx-examples/stable_diffusion/txt2image.py"
    for idx, prompt in enumerate(prompts):
        image_name = f"{dir_path}/image_{idx}.png"
        command = f"python3 {script_path} --n_images 1 -q -v --output \"{image_name}\" \"{prompt}\""
        os.system(command)
        generated_image_paths.append(os.path.abspath(image_name))
    return generated_image_paths

dir_name = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
print(dir_name)
os.makedirs(dir_name, exist_ok=True)

visual_prompts = [
    "Setting: Ancient orchards in South Asia at sunrise. Background: Farmers tend to young mango trees, their silhouettes against the rising sun. Lighting: Early morning light bathes the orchard in a golden hue, casting long, dramatic shadows.",
    "Setting: Cultural festival in India. Background: Locals celebrate with mango decorations and offerings. Lighting: Bright, festive lights illuminate the colorful mango-laden stalls and joyful faces of participants.",
    "Setting: Vast mango plantation in Thailand. Background: Rows of mango trees stretch into the distance, workers harvesting fruit. Lighting: Strong tropical sun highlights the lush greenery and the vibrant yellow and orange mangoes.",
    "Setting: Busy market in Mexico. Background: Vendors display a variety of mangoes, customers engage in lively bartering. Lighting: The harsh midday sun casts sharp shadows, enhancing the vivid colors of the mango array.",
    "Setting: Indian wedding ceremony. Background: Mango leaves and fruits are used in sacred rituals. Lighting: Soft, warm light envelops the scene, creating a serene and auspicious atmosphere.",
    "Setting: Nutritional seminar. Background: A nutritionist discusses the health benefits of mangoes with attendees. Lighting: Indoor lighting complements the presentation, focusing on displayed charts and mango samples.",
    "Setting: International cargo port. Background: Workers load crates of mangoes into a freight ship. Lighting: Late afternoon sun casts a golden glow over the bustling activity, emphasizing the global trade of mangoes.",
    "Setting: Experimental farm focusing on sustainable practices. Background: Technicians monitor mango growth using eco-friendly techniques. Lighting: The setting sun provides a soft backlight, highlighting innovative farming equipment.",
    "Setting: Genetic research lab. Background: Scientists examine mango seedlings for desired traits. Lighting: Bright, clinical lights focus on the meticulous work, emphasizing precision and technology.",
    "Setting: Urban supermarket in Europe. Background: Shoppers select from a wide range of imported mangoes. Lighting: Fluorescent lights illuminate the colorful produce section, spotlighting the mangoes' appeal.",
    "Setting: Culinary school kitchen. Background: Chefs teach students to prepare dishes using mangoes. Lighting: Overhead lights cast a professional glow over the busy, stainless-steel counters.",
    "Setting: Food festival celebrating mango cuisine. Background: Chefs serve mango-inspired dishes to eager attendees. Lighting: Evening lights twinkle around, casting a festive and appetizing glow on the food stalls.",
    "Setting: Industrial packing facility. Background: Workers package mangoes for export, ensuring quality control. Lighting: Bright industrial lighting ensures visibility and highlights the efficiency and cleanliness of the process.",
    "Setting: Traditional home in the Philippines. Background: A family enjoys a meal featuring mango dishes. Lighting: Natural light streams through windows, creating a warm, inviting dining scene.",
    "Setting: Health food store in North America. Background: Customers browse through sections dedicated to tropical fruits, including mangoes. Lighting: Bright and welcoming lights shine down, making the colorful mangoes stand out.",
    "Setting: Agricultural conference. Background: Experts discuss advancements in mango cultivation techniques. Lighting: Conference room lighting focuses on speakers and their multimedia presentations.",
    "Setting: Air cargo facility. Background: Crates of mangoes being loaded onto a plane for international delivery. Lighting: The dusk light casts long shadows across the tarmac, emphasizing the global logistics involved.",
    "Setting: Local farmers market. Background: Farmers sell fresh, organic mangoes directly to consumers. Lighting: Early morning sunlight filters through trees, spotlighting the natural quality of the produce.",
    "Setting: Corporate boardroom. Background: Business leaders strategize on the global mango trade. Lighting: Soft, subtle lighting complements the serious tone of the discussions.",
    "Setting: Online cooking show. Background: A chef demonstrates how to make a mango dessert. Lighting: Bright studio lights ensure every detail is visible, from the slicing of the mango to the final plating."
]


paths = image_generator(visual_prompts,dir_name)