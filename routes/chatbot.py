from flask import Blueprint, render_template, request
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "stabilityai/stablelm-tuned-alpha-7b"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

bp = Blueprint('chatbot', __name__)

@bp.route('/chatbot', methods=['GET', 'POST'])
def chatbot():
    if request.method == 'POST':
        message = request.form['message']
        response = generate_response(message)
        return {'message': message, 'response': response}
    return render_template('chatbot.html')

def generate_response(input_text):
    input_ids = tokenizer.encode(input_text + tokenizer.eos_token, return_tensors='pt')
    output = model.generate(input_ids, max_length=1000, do_sample=True)
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response
