import gradio as gr
import numpy as np


def predict_profit(rd, admin, marketing):

    data = np.array([[rd, admin, marketing]])

    prediction = model_multi_reg.predict(data)

    return f"💰 Predicted Profit: ${prediction[0]:,.2f}"


css = """

body {
    background: #111827;
}


.gradio-container {
    max-width: 1200px !important;
    margin: auto !important;
}


h1 {
    text-align: center;
    font-size: 45px !important;
    color: #ff7a00;
}


p {
    text-align: center;
    font-size: 20px !important;
}


label span {
    background: #ff7a00 !important;
    color: black !important;
    padding: 8px 12px;
    border-radius: 8px;
    font-size: 18px !important;
    font-weight: bold;
}


input {
    height: 60px !important;
    font-size: 20px !important;
}


button {
    height: 65px !important;
    background: #ff7a00 !important;
    color: white !important;
    font-size: 25px !important;
    font-weight: bold;
}


textarea {
    height: 120px !important;
    font-size: 28px !important;
    text-align: center;
}
footer {
    display: none !important;
}

"""


with gr.Blocks(css=css) as demo:


    gr.Markdown(
        """
        # 🚀 Startup Profit Prediction
        
        Enter startup details to predict the expected profit using Machine Learning
        """
    )


    with gr.Row():

        rd = gr.Number(
            label="💰 Research and Development Spend"
        )

        admin = gr.Number(
            label="🏢 Administration Expenditure"
        )


        marketing = gr.Number(
            label="📢 Marketing Expenditure"
        )


    predict = gr.Button(
        "🚀 Predict Profit"
    )


    result = gr.Textbox(
        label="Prediction Result"
    )


    predict.click(
        predict_profit,
        inputs=[rd, admin, marketing],
        outputs=result
    )


demo.launch(share=True)