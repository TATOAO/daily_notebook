import gradio as gr
# pip install gradio

def display_user(user_message, history):
    # Append the new message with the role as a tuple
    if history is None:
        history = []
    history.append((user_message, None))
    return history

def display_assistant(assistant_message, history):
    # Append the new message with the role as a tuple
    if history is None:
        history = []
    history.append((None, assistant_message))
    return history

def update_analysis(history):
    # Analyze the history and generate some analysis text
    analysis_text = ""
    for user_msg, assistant_msg in history:
        if user_msg:
            analysis_text += f"User said: {user_msg}\n"
        if assistant_msg:
            analysis_text += f"Assistant replied: {assistant_msg}\n"
    return analysis_text

# Create the main input box and additional input box
textbox_user = gr.Textbox(placeholder="User", container=False, scale=7)
textbox_asst = gr.Textbox(placeholder="Assistant", container=False, scale=7)

# Create buttons to trigger the inputs
submit_btn_user = gr.Button("User Speak")
submit_btn_asst = gr.Button("Assistant Speak")
# Create a component to show the analysis
analysis_output = gr.Textbox(label="Analysis", placeholder="Analysis will be displayed here", container=True, scale=14, lines=25)


# Update the ChatInterface to include the buttons and link them to the respective functions
with gr.Blocks() as demo:

    with gr.Row():
        with gr.Column(scale=1):
            with gr.Row():
                chatbot = gr.Chatbot(height=500)
            
            with gr.Row():
                textbox_user.render()
                submit_btn_user.render()
            submit_btn_user.click(display_user, inputs=[textbox_user, chatbot], outputs=chatbot)
            
            with gr.Row():
                textbox_asst.render()
                submit_btn_asst.render()
            submit_btn_asst.click(display_assistant, inputs=[textbox_asst, chatbot], outputs=chatbot)

        with gr.Column(scale=1):
            analysis_output.render()

    chatbot.change(update_analysis, inputs=chatbot, outputs=analysis_output)

demo.launch(share=True)


