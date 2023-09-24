import gradio as gr
from happytransformer import HappyTextToText

# Load the pre-trained T5 model
happ_tt = HappyTextToText("T5", "t5-base")

# Define the function to make predictions
def translate(input_text):
    result = happ_tt.generate_text(input_text, max_length=150)  # Adjust max_length as needed
    return result[0]  # Assuming you want the first generated output

# Create a Gradio interface
iface = gr.Interface(
    fn=translate,
    inputs="text",
    outputs="text",
    title="Text-to-Text Translation",
    description="Translate text with a T5 model.",
)

# Launch the Gradio app
iface.launch()
