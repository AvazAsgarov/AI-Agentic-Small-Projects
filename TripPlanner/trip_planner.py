from dotenv import load_dotenv
load_dotenv(override=True)

import os
from openai import OpenAI

api_key = os.getenv("OPENAI_API_KEY")

if api_key:
    print("OPENAI_API_KEY is set")
else:
    raise ValueError("OPENAI_API_KEY is NOT set.")

client = OpenAI(api_key=api_key)
model_name = "gpt-4o-mini"

# Step 1: Select a country
continent = "Asia"
country_prompt = f"Select one country in {continent}. Only output the country name."

response = client.chat.completions.create(
    model=model_name,
    messages=[
        {"role": "user", "content": country_prompt}
    ]
)

country = response.choices[0].message.content.strip()
print("Selected country:", country)

# Step 2: Generate a trip plan
trip_prompt = f"Create a detailed 3-day travel itinerary for {country}. Provide activities, timing, and tips."

response = client.chat.completions.create(
    model=model_name,
    messages=[
        {"role": "user", "content": trip_prompt}
    ],
    max_tokens=400
)

trip_plan = response.choices[0].message.content
print("\nTrip Plan:\n", trip_plan)
