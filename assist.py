
import openai

openai.api_key = "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"

def ask_gpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Ви говорите від імені Василя Сухомлинського, видатного українського педагога."},
                {"role": "user", "content": prompt},
            ],
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Виникла помилка: {str(e)}"

if __name__ == "__main__":
    question = "Що таке педагогіка любові?"
    print(ask_gpt(question))
