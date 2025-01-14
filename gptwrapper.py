from openai import OpenAI

client = OpenAI(
  api_key="API_KEY_HERE"
)

def answer(prompt):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        store=True,
        messages=[
            {"role": "user", "content": f{prompt}}
        ]
    )

    return (completion.choices[0].message)

def main():
    print(answer("What's 3 + 6"))

main()
