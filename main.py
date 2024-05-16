from openai import OpenAI

print("")

image_query = input("What image do you want to create?\n")

print("")

client = OpenAI()

image_response = client.images.generate(
  model="dall-e-3",
  prompt=image_query,
  n=1,
  size="1024x1024"
)

print(image_response.data[0].revised_prompt)
print(image_response.data[0].url)