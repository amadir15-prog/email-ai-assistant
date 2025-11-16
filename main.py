from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=["GET"])
def home():
    return "AI Email Assistant is running!"

@app.route("/reply", methods=["POST"])
def reply():
    data = request.json
    customer_email = data.get("email", "")

    prompt = f"""
Jesteś asystentem AI obsługującym sklep internetowy.
Twoim zadaniem jest tworzenie profesjonalnych, uprzejmych i rzeczowych odpowiedzi na maile klientów.

Mail od klienta:
{customer_email}

Napisz najlepszą możliwą odpowiedź:
"""

    completion = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    reply_text = completion.choices[0].message["content"]

    return jsonify({"reply": reply_text})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
