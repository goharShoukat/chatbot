import gradio as gr
from .services.call_llm import call_llm
from dotenv import load_dotenv


with gr.Blocks() as demo:
    chatbot = gr.Chatbot(type="messages")
    msg = gr.Textbox(placeholder="Type your message here", lines=2, max_lines=10)

    def respond(message, chat_history):
        response = call_llm(message)
        chat_history.append({"role": "user", "content": message})
        chat_history.append({"role": "assistant", "content": response})

        return "", chat_history

    msg.submit(respond, [msg, chatbot], [msg, chatbot])
demo.launch()
