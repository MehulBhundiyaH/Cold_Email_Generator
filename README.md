# COLD_EMAIL_GENERATOR
## Demo Video Link : 
- https://drive.google.com/file/d/1v_ph_OYB-Wd7k4OeYKcyG2k1ul1Bt5ET/view?usp=sharing

Hello !

## Overview

Cold Email Generator is an end-to-end tool designed for software service companies to streamline the process of creating personalized cold emails for job opportunities listed by potential clients. By leveraging advanced AI and database technologies like Llama 3.1, Chroma DB, LangChain, and Streamlit, the tool automates the extraction of job requirements, matches them with relevant portfolios, and generates tailored cold emails, enabling efficient and targeted outreach.

I will walk you through the repo and tell you the steps to use & implement the idea.


- First clone the repo and install all the requirements/ dependencies in your environment.
- Then paste your company's data in the vector database / in the csv file in the same format as given (just try to analyse the given csv data; you'll get it.)
- Then you can even modify the prompt and tune it more based on your usecase(in chains).
- Run the main file located in the app/ folder in the terminal ( streamlit run .\app\main.py )
- You'll see the basic streamlit app interface.
- Paste the link of the job page in the input box and submit.
- Within 30 seconds, the cold email will be ready for your use !

## Features

- Job Requirement Extraction: Automatically extracts key details from job postings on client websites.

- Personalized Email Generation: Crafts tailored cold emails using job requirements and employee skill sets.

- Portfolio Matching: Identifies the most relevant employee profiles for a given job role.

- Semantic Search with Vector Database: Uses Chroma DB to perform semantic searches for skill and job requirement matching.

- Streamlit-based UI: Provides an intuitive user interface for easy interaction and email draft generation.

- Data Cleaning: Includes utility functions to clean and preprocess job requirements and portfolio data for effective processing.

## Tech Stack

- Llama 3.3: Large language model for natural language generation.

- Chroma DB: Lightweight, open-source vector database for semantic search.

- LangChain: Framework for building applications with language models.

- Streamlit: Framework for creating user-friendly web applications.

- Python: Core programming language for development.

## Requirements

- Python 3.8 or higher

- langchain

- chromadb

- streamlit

- pandas

- numpy

- API Key for Llama 3.3 or any compatible LLM

## Usage

### Run the Streamlit application:
               streamlit run app.py

### Use the web interface to:

- Input a job description URL or upload a JSON file containing job details.

- Generate a personalized cold email draft.

- View matching portfolios based on job requirements.

- Review the generated email draft and download it for further use.

## How It Works

 ### Data Extraction:
 - Extracts job requirements from a webpage or JSON file.

 ### Semantic Matching:

- Stores and retrieves employee skills using Chroma DB.

- Matches job requirements with relevant employee portfolios.

### Cold Email Generation:

- Uses Llama 3.1 to create personalized and professional cold emails.

- Incorporates job requirements and matched portfolio details.

### User Interface:

- Facilitates seamless interaction through Streamlit.

- Allows users to submit queries and generate emails in real-time.

## Contributing

 Contributions are welcome! To contribute:

- Fork the repository.

- Create a feature branch.

- Commit your changes.

- Submit a pull request.

## Contact

For questions or suggestions, please contact:

Name: Mehul Bhundiya

Email: bhundiyamehul86@gmail.com
