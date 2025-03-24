# ✨ EasyCover AI

[![Python 3.13+](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/streamlit-1.43.2-FF4B4B.svg)](https://streamlit.io)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT4-00A67E.svg)](https://openai.com/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An AI-powered tool that generates customized cover letters by analyzing your resume and job postings.

## 🚀 Features

- PDF resume parsing with PyPDF2
- Automatic job posting analysis using Firecrawl
- Parallel processing for faster results
- Customized cover letter generation with GPT4
- Streamlit web interface

## 🛠️ Quick Start

1. Clone the repository

2. Run it locally

```sh
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

3. Add your OpenAI and Firecrawl API key on the left
4. Upload resume
5. Enter Job posting URL
6. Create cover letter

## :streamlit: → Demo App

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://easycover.streamlit.app/)


1. Add your OpenAI and Firecrawl API key on the left
2. Upload resume
3. Enter Job posting URL
4. Create cover letter


### To set the OpenAI and Firecrawl API key in Streamlit Community Cloud, set the API keys as an environment variable in Streamlit:

1. At the lower right corner, click on `< Manage app` then click on the vertical "..." followed by clicking on `Settings`.
2. This brings the **App settings**, next click on the `Secrets` tab and paste the API keys into the text box as follows:

```sh
OPENAI_API_KEY='xxxxxxxxxx'
FIRECRAWL_API_KEY='xxxxxxxxxx'
```

