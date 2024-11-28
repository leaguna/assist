import openai
import os

# Завантажте API ключ з змінних середовища
openai.api_key = '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'

# Запит до асистента
def get_assistant_response(user_input):
    try:
        # Створення запиту до API OpenAI
        response = openai.Completion.create(
            model="gpt-3.5-turbo",  # Використовуємо модель GPT-3.5 Turbo
            prompt=user_input,  # Текст, на основі якого модель генерує відповідь
            max_tokens=150  # Ліміт символів на одну відповідь
        )
        
        # Повертаємо текст відповіді
        return response['choices'][0]['text'].strip()

    except Exception as e:
        return f"Виникла помилка: {e}"

# Приклад використання асистента
if __name__ == "__main__":
    user_input = input("Введіть запит: ")
    response = get_assistant_response(user_input)
    print("Відповідь асистента:", response)
