import os
from flask import Flask, render_template, request, redirect, url_for, flash
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from phi.agent import Agent
from phi.model.groq import Groq
# Load environment variables
load_dotenv()

# Retrieve the API keys from the environment
SERPAPI_KEY = os.getenv("SERPAPI_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not set. Please check your environment variables.")
if not SERPAPI_KEY:
    raise ValueError("No API key found! Please set the SERPAPI_KEY environment variable.")

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this in production

# --------------------------------------------
# TASK 1: Get Company News
# --------------------------------------------
def get_company_news(company_name):
    url = f"https://serpapi.com/search.json?engine=google_news&q={company_name}&api_key={SERPAPI_KEY}"
    response = requests.get(url)
    data = response.json()
    if "news_results" in data:
        return [news["title"] for news in data["news_results"]]
    return []

# --------------------------------------------
# TASK 2: Generate LinkedIn Message
# --------------------------------------------


# Initialize the Groq agent (adjust the model id if needed)
agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    api_key=GROQ_API_KEY
)

def generate_linkedin_message(name, job_title, company, common_interest=None):
    prompt = (
        f"Write a personalized LinkedIn connection message for {name}, who is a {job_title} at {company}. "
    )
    if common_interest:
        prompt += f"I noticed we both have an interest in {common_interest}. "
    prompt += (
        "The message should be friendly, professional, and explain how connecting could be mutually beneficial. "
        "The message should always start with a greeting and end with a call to action. "
        "Please ensure the response is well-structured single paragrah with formatting with each new line in the next line."
    )
    response = agent.run(prompt)
    return response.content

# --------------------------------------------
# Helper function for TASKS 3 & 4: Scrape Website Content
# --------------------------------------------
def scrape_website(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except Exception as e:
        raise Exception(f"Failed to access {url}: {e}")
    soup = BeautifulSoup(response.text, "html.parser")
    text = soup.get_text(separator="\n")
    clean_text = "\n".join(line.strip() for line in text.splitlines() if line.strip())
    return clean_text

# --------------------------------------------
# TASK 3: Analyze Company Info
# --------------------------------------------
def analyze_company_info(url):
    website_content = scrape_website(url)
    prompt = (
        "Based on the following website content, please provide a detailed analysis of the company's value proposition, "
        "sales motion, and pricing structure. The analysis should be clear, concise, and highlight the main points.\n\n"
        "Website Content:\n"
        f"{website_content}\n"
    )
    response = agent.run(prompt)
    return response.content

# --------------------------------------------
# TASK 4: Answer Company Question
# --------------------------------------------
def answer_company_question(url, question):
    website_content = scrape_website(url)
    prompt = (
        "Based on the following website content, please answer the following question about the company in a clear and concise manner.\n\n"
        f"Question: {question}\n\n"
        "Website Content:\n"
        f"{website_content}\n"
    )
    response = agent.run(prompt)
    return response.content

# --------------------------------------------
# Flask Routes
# --------------------------------------------
@app.route('/')
def index():
    return render_template('index.html')

# --- Route for Task 1: Company News ---
@app.route('/news', methods=['GET', 'POST'])
def news():
    if request.method == 'POST':
        company = request.form.get('company')
        if not company:
            flash("Please enter a company name.")
            return redirect(url_for('news'))
        news_headlines = get_company_news(company)
        return render_template('news_result.html', company=company, headlines=news_headlines)
    return render_template('news.html')

# --- Route for Task 2: LinkedIn Message ---
@app.route('/linkedin', methods=['GET', 'POST'])
def linkedin():
    if request.method == 'POST':
        name = request.form.get('name')
        job_title = request.form.get('job_title')
        company = request.form.get('company')
        common_interest = request.form.get('common_interest')
        if not (name and job_title and company):
            flash("Please fill out all required fields.")
            return redirect(url_for('linkedin'))
        message = generate_linkedin_message(name, job_title, company, common_interest)
        return render_template('linkedin_result.html', message=message)
    return render_template('linkedin.html')

# --- Route for Task 3: Analyze Company Info ---
@app.route('/analyze', methods=['GET', 'POST'])
def analyze():
    if request.method == 'POST':
        website = request.form.get('website')
        if not website:
            flash("Please enter a website URL.")
            return redirect(url_for('analyze'))
        # Add protocol if missing
        if not website.startswith("http"):
            website = "https://" + website
        if not website.endswith(".com"):
            website = website + ".com"
        try:
            analysis = analyze_company_info(website)
        except Exception as e:
            flash(str("The website you entered is invalid! Please enter a valid website."))
            return redirect(url_for('analyze'))
        return render_template('analyze_result.html', website=website, analysis=analysis)
    return render_template('analyze.html')

# --- Route for Task 4: Answer Company Question ---
@app.route('/question', methods=['GET', 'POST'])
def question():
    if request.method == 'POST':
        website = request.form.get('website')
        user_question = request.form.get('question')
        if not website or not user_question:
            flash("Please fill out all required fields.")
            return redirect(url_for('question'))
        if not website.startswith("http"):
            website = "https://" + website
        if not website.endswith(".com"):
            website = website + ".com"
        try:
            answer = answer_company_question(website, user_question)
        except Exception as e:
            flash(str("The website you entered is invalid! Please enter a valid website."))
            return redirect(url_for('question'))
        return render_template('question_result.html', website=website, answer=answer)
    return render_template('question.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
