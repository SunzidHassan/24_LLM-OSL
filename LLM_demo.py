from PIL import Image
import matplotlib.pyplot as plt
import base64
import numpy as np
import pandas as pd
import os
from dotenv import load_dotenv
from llmPrompt import llmPrompt
from gptPayload import payload

# Load the OpenAI API key from .env file
load_dotenv()
api_key = os.getenv('OPENAPI_KEY')

# get user input of timestamp
i = input("Please enter a timestamp (1-13): ")
if not 1 <= int(i) <= 14:
    i = np.random.randint(1,14)
    print(f"Invalid input, selecting {i} as the timestamp")


# chemical threshold used in the experiment
chmThr = 480
delimiter = "#####"

imagePath = f"Static/{i}.png"
chemical = pd.read_csv('Static/olfactionData').iloc[i,3]

with open(imagePath, "rb") as image_file:
    image_base64 = base64.b64encode(image_file.read()).decode('utf-8')

prompt = llmPrompt(delimiter, chmThr=chmThr, chemical=chemical)
response = payload(api_key, prompt, image_base64)

# Outputs
plt.imshow(image_file)
plt.title("Robot egocentric visual frame")
plt.axis('off')  # Hide the axes
plt.show()

print(f"Chemical concentration: {chemical}")

print(response)
