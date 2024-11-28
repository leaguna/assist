
import openai

openai.api_key = "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"

def ask_gpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Ви говорите від імені Василя Сухомлинського, видатного українського педагога. Ваш стиль доброзичливий, мотивуючий і спрямований на допомогу у навчанні."},
                {"role": "user", "content": prompt},
            ],
        )
        return response['choices'][0]['message']['content']
   
   
    except Exception as e:
        return f"Виникла помилка: {str(e)}"
context = "Ви говорите як Василь Сухомлинський, видатний педагог України. Ваш стиль - доброзичливий і мудрий."

def get_response(prompt):
    full_prompt = context + "\n\n" + prompt
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=full_prompt,
        max_tokens=150,
        temperature=0.7,
    )
    return response.choices[0].text.strip()
    
if __name__ == "__main__":
    question = "Що таке педагогіка любові?"
    print(ask_gpt(question))
