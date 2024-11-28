import openai

# Задайте ваш API ключ
openai.api_key = 'your-api-key'

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
