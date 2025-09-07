

 🖼️ Image Caption Generator

A deep learning–powered application that automatically generates **human-like captions** for images using the [BLIP model](https://huggingface.co/Salesforce/blip-image-captioning-base).

Built with **Python, PyTorch, Hugging Face Transformers, and Streamlit**, this project helps in **image understanding, accessibility, and content creation**.



 🚀 Features

* Upload an image → get a meaningful caption
* Adjustable parameters: max tokens, beam search, repetition penalty, caption length
* Simple web interface powered by **Streamlit**
* Can be deployed easily on **Streamlit Cloud** or **Hugging Face Spaces**



 📂 Project Structure


.
├── streamlit_app.py      # Main Streamlit app
├── requirements.txt      # Project dependencies
├── .gitignore            # Ignore unnecessary files
└── README.md             # Project documentation




 ⚙️ Installation (Run Locally)

1. **Clone this repo**


git clone https://github.com/<your-username>/<repo-name>.git


2. **Create virtual environment**


python -m venv .venv
# Windows
.venv\Scripts\activate
# Mac/Linux
source .venv/bin/activate


3. **Install dependencies**


pip install -r requirements.txt


4. **Run the app**


streamlit run streamlit_app.py


5. Open in browser: [http://localhost:8501](http://localhost:8501) 🎉



 🌐 Deployment on Streamlit Cloud

1. Push your project to GitHub.
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud).
3. Connect your GitHub repo → select branch → set **main file path** as `streamlit_app.py`.
4. Deploy → get a **public URL** to share!



 🖼️ Example

| Uploaded Image                           | Generated Caption                 |
| ---------------------------------------- | --------------------------------- |
| ![dog](https://i.ibb.co/0jqHpnp/dog.jpg) | "A dog running through the grass" |



 🛠️ Tech Stack

* **Python**
* **Streamlit** (UI)
* **PyTorch** (deep learning backend)
* **Hugging Face Transformers** (BLIP model)
* **PIL / Pillow** (image processing)



 ✨ Future Improvements

* Support for **multiple captions** per image
* Add **translation** (multilingual captions)
* Deploy on **Hugging Face Spaces** for ML community sharing



 🙌 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.




👉 Do you want me to also add a **badges section** (Python, Streamlit, Hugging Face) at the top so your repo looks even more professional on GitHub?
