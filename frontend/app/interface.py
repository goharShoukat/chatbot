import gradio as gr
import requests
import json

url = "http://127.0.0.1:8000/chat/stream"


def echo(text, request: gr.Request):
    if request:
        payload = {"query": text}
        foo = requests.post(url, data=json.dumps(payload), stream=False)
        bar = foo.content.decode("utf-8")
        return bar


io = gr.Interface(echo, "textbox", "textbox").launch()
