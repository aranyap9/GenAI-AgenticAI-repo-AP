from transformers import pipeline

generator = pipeline(
    "text2text-generation",
    model = "google/flan-t5-base"
)

text = "translate English to Shakespearean: Bro, why is the WiFi so slow today?"

result = generator(text, max_length = 50)

print("===== SHAKESPEAREAN TEXT =====")
print(result[0]['generated_text'])