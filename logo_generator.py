import requests
import io
from PIL import Image


API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-dev"

headers = {"Authorization": "Bearer hf_your_api_key", "x-wait-for-model" : "true", "x-use-cache": "false"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content

question = input("[+] Enter prompt for logo: ")
print("[+] Creating Logo Please wait....")
image_bytes = query({
	"inputs": f"{question}",
	"target_size" : 200,
	"guidance_scale" : 50,
})

image = Image.open(io.BytesIO(image_bytes))
image.save('logo.png')
print("[+] Done Creating Logo saved in Dir....")
