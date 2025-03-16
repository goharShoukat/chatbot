import gradio as gr
import requests
import json

url = "http://127.0.0.1:8000/chat/stream"


def call_llms(text):
    payload = {"query": text}
    foo = requests.post(url, data=json.dumps(payload), stream=False)
    bar = foo.content.decode("utf-8")
    return bar


with gr.Blocks() as demo:
    chatbot = gr.Chatbot(type="messages")
    msg = gr.Textbox()
    clear = gr.ClearButton([msg, chatbot])

    def respond(message, chat_history):
        response = call_llms(message)
        chat_history.append({"role": "user", "content": message})
        chat_history.append({"role": "assistant", "content": response})

        return "", chat_history

    msg.submit(respond, [msg, chatbot], [msg, chatbot])
demo.launch()
