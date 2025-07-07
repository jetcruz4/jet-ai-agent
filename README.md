JetCruz AI Agent - MVP Setup

1. Create and activate a virtual environment (optional but recommended)
   python -m venv venv
   source venv/bin/activate (Mac/Linux) or .\venv\Scripts\activate (Windows)

2. Install requirements
   pip install -r requirements.txt

3. Set your OpenAI API Key as an environment variable:
   export OPENAI_API_KEY=your_key_here (Mac/Linux)
   set OPENAI_API_KEY=your_key_here (Windows)

4. Run the app
   streamlit run main.py