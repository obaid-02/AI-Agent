# Mudkudu AI Agent Web App

This agent is capable of autonomous decision-making and task execution tailored to MadKudu’s business needs. It can:

- **Research B2B Accounts:** Identify relevant news to help a salesperson justify collaborations.
- **Generate LinkedIn Messages:** Create personalized and professional connection notes.
- **Analyze Company Websites:** Understand a company’s value proposition, sales motion, and pricing structure.
- **Answer Company Questions:** Retrieve information by scraping websites or using other approaches.

> **Demo:**  
> *(Insert demo videos and screenshots here)*

---

## Table of Contents

1. [Requirements](#requirements)
2. [Setup and Configuration](#setup-and-configuration)
   - [Setting Up API Keys](#setting-up-api-keys)
   - [Creating the `.env` File](#creating-the-env-file)
3. [Installation and Running Locally](#installation-and-running-locally)
4. [Project Structure](#project-structure)
5. [Usage](#usage)
6. [License](#license)

---

## Requirements

- **Python:** Version 3.7 or above.
- **Pip:** The Python package manager.
- **Virtual Environment (recommended):** e.g., `venv` or `conda`.
- **Dependencies:**
  - [Flask](https://flask.palletsprojects.com/)
  - [python-dotenv](https://pypi.org/project/python-dotenv/)
  - [Requests](https://pypi.org/project/requests/)
  - [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/)

---

## Setup and Configuration

### Setting Up API Keys

This project requires two external APIs for full functionality:

1. **SERPAPI (for company news):**
   - **Sign Up:** Visit [SERPAPI](https://serpapi.com/) and create an account.
   - **API Key:** After logging in, navigate to your dashboard to obtain your API key.

2. **GROQ API (for AI agent tasks):**
   - **Sign Up:** Go to the official Groq website (or the relevant API provider’s website) and sign up.
   - **API Key:** Retrieve your API key from the account dashboard after signup.

### Creating the `.env` File

In the root of your project (or inside your `WebApp/` folder, wherever your code loads the environment variables), create a file named `.env` with the following content:
Replace the placeholder text (`your_serpapi_key_here`, etc.) with the actual keys you obtained from the respective API providers.

---
# Setup Steps for Mudkudu AI Agent Web App

This guide will walk you through setting up and running the Mudkudu AI Agent Web App locally.

---

## 1. Clone the Repository

Open your terminal and run the following commands:

```bash
git clone https://github.com/yourusername/MudkuduAIAgent.git
cd MudkuduAIAgent/WebApp
```
![image](https://github.com/user-attachments/assets/21403bef-68a6-4ff9-8718-ce413a1143f0)

## 2. Set Up a Virtual Environment

```bash
conda create --name mudkudu_env python=3.11.10
conda activate mudkudu_env
```
## 3. Install Dependencies

```bash
pip install -r requirements.txt
```
* Otherwise, install the packages manually using pip:
`pip install `

## 4. Run the Application
With your virtual environment activated and API keys configured, start the Flask application:

```bash
   python app.py
```

## 5. Access the Web Application

Open your web browser and navigate to http://127.0.0.1:5000 to access the Mudkudu AI Agent Web App.


