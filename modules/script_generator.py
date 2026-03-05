import openai
import config

openai.api_key = config.OPENAI_API_KEY


def generate_script(title):

    prompt = f"""
Create a YouTube Shorts script.

Topic:
{title}

Structure:
Hook
3 bullet facts
Ending CTA
"""

    r = openai.ChatCompletion.create(

        model="gpt-4o-mini",

        messages=[
            {"role": "user", "content": prompt}
        ]

    )

    return r["choices"][0]["message"]["content"]
