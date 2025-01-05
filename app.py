from flask import Flask, render_template, request
from groq import Groq

app = Flask(__name__)

# API key Groq
AI_KEY = "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"
client = Groq(api_key=AI_KEY)

@app.route("/", methods=["GET", "POST"])
def index():
    chat_response = ""
    if request.method == "POST":
        user_input = request.form["user_input"]
        
        # Kirim input ke API Groq
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": user_input}],
            model="llama-3.3-70b-versatile",
        )
        
        chat_response = chat_completion.choices[0].message.content
    
    return render_template("index.html", chat_response=chat_response)

if __name__ == "__main__":
    app.run(debug=True)
