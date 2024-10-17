from PIL import Image
import cv2
import base64
import numpy as np
import pandas as pd
import yaml
from llmPrompt import llmPrompt
from gptPayload import payload

def display_image(imagePath):
    img = Image.open(imagePath)
    img_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    cv2.imshow('Image Window', img_cv)
    cv2.waitKey(5000)
    cv2.destroyAllWindows()

# Load the OpenAI API key from .env file
config = yaml.load(open('config.yaml'), Loader=yaml.FullLoader)
api_key = config['OPENAI_KEY']
gpt_model = config['OPENAI_CHAT_MODEL']

# get user input of timestamp
i = input("Please enter a timestamp (1-13): ")
if not 1 <= int(i) <= 14:
    i = np.random.randint(1,14)
    print(f"Invalid input, selecting {i} as the timestamp")
else:
    i = int(i)

# chemical threshold used in the experiment
chmThr = 480
delimiter = "#####"
imagePath = f"assets/simulationData/{i}.png"
chemical = pd.read_csv('assets/simulationData/olfactionData.csv').iloc[i,3]

# LLM response
with open(imagePath, "rb") as image_file:
    image_base64 = base64.b64encode(image_file.read()).decode('utf-8')

prompt = llmPrompt(delimiter, chmThr=chmThr, chemical=chemical)
response = payload(api_key, prompt, image_base64, gpt_model)

# Outputs
print(f"Chemical concentration: {chemical}")
print(response)
display_image(imagePath)