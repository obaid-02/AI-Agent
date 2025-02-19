# Architecture and Decision-Making Process

## Overview
The AI Agent is designed to automate a series of business intelligence tasks. The agent is capable of autonomous decision-making and task execution by integrating several key components, including API calls, web scraping, and prompt-based text generation via a large language model. The primary functionalities include:

- **Retrieving Company News:** Uses SERPAPI to fetch the latest news headlines related to a company.
- **Generating LinkedIn Messages:** Constructs personalized and professional connection notes using a Groq-powered language model.
- **Analyzing Company Websites:** Scrapes and processes website content to analyze the company's value proposition, sales motion, and pricing structure.
- **Answering Company Questions:** Combines scraped data with user inquiries to provide detailed answers about a company.

## Agent Architecture

### 1. Input/Output Interface
- **Flask Web Application:**  
  The web interface is built using Flask, which provides forms for user inputs and displays the generated outputs. Each task (news, LinkedIn message, analysis, and Q&A) has its own dedicated page with clear navigation.

### 2. External Integrations
- **SERPAPI:**  
  Retrieves up-to-date news articles based on user-provided company names. The agent parses the JSON response to extract relevant headlines.
- **Groq API:**  
  Utilizes a large language model (e.g., `llama-3.3-70b-versatile`) to generate text responses. This API is responsible for creating personalized LinkedIn messages, detailed company analyses, and responses to company questions.

### 3. Data Retrieval and Processing
- **Web Scraping Module:**  
  The agent uses the `requests` library to fetch website content and `BeautifulSoup` to parse HTML, extracting clean, visible text for analysis.
- **Preprocessing:**  
  Extracted data is cleaned and formatted before being integrated into prompts for the language model.

### 4. Prompt Engineering
- **Custom Prompts for Each Task:**  
  Depending on the task, the agent constructs tailored prompts:
  - For LinkedIn message generation, the prompt includes details such as the contact's name, job title, company, and common interests.
  - For company analysis, the scraped website content is combined with instructions to examine the company’s value proposition, sales strategy, and pricing structure.
  - For answering company questions, the prompt includes both the user’s question and relevant website content.
- **Language Model Interaction:**  
  The crafted prompt is sent to the Groq API, which processes the information and returns a text-based response. This response is then formatted for display on the web interface.

## Decision-Making Process

1. **User Input Acquisition:**
   - Users enter required data via web forms (e.g., company name, website URL, contact details, or specific questions).
   - Based on the selection, the corresponding function is triggered.

2. **Task Execution:**
   - **Company News:**  
     The agent sends a request to SERPAPI and processes the returned JSON to extract and display news headlines.
   - **LinkedIn Message Generation:**  
     Using the provided contact details, the agent constructs a prompt and calls the Groq API to generate a personalized connection note.
   - **Company Analysis:**  
     The agent scrapes the target website, cleans the extracted text, and builds a prompt for the Groq API to analyze the company’s value proposition, sales motion, and pricing structure.
   - **Company Q&A:**  
     A combination of the scraped website data and the user's question is fed into the language model to produce a detailed answer.

3. **Response Generation and Delivery:**
   - The language model processes the input prompt and generates a response.
   - The generated response is then displayed on the appropriate result page, with navigation options for further exploration (e.g., Back or Home buttons).

## Extensibility and Future Enhancements
- **Modular Design:**  
  The architecture is modular, allowing new functionalities or data sources to be integrated with minimal changes to existing code.
- **Scalability:**  
  Future enhancements can include additional analysis capabilities or alternative language model backends.
- **Improved Prompt Engineering:**  
  As the agent is refined, prompt designs can be optimized further to improve response relevance and quality.

---

*This documentation outlines the core components of the AI Agent and explains how its various modules work together to achieve autonomous decision-making and task execution.*
