import ollama

res = ollama.chat(
    model = 'llava:13b',
    messages = [
        {'role': 'user',
         'content': 'Discrabe this images in 5-25 words',
         'images': ['./sample_data/Screenshot 2024-10-18 133953.png']
         }
    ]
)

print(res['message']['content'])