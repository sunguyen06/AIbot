from openai import OpenAI

client = OpenAI(
  api_key="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"
)

def feedback(ca):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        store=True,
        messages=[
            {"role": "user", "content": f"According to Warren Buffet's idealogy on investments in the stock market. Analyze the following memecoin with this CA: {ca}."}
        ]
    )

    return (completion.choices[0].message)

def main():
    print(feedback("9aLx5SCcoacuK4VVmucy3yu7smR37TWXFyTHnxUQpump"))

main()
