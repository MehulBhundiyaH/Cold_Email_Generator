from langchain_groq import ChatGroq

llm = ChatGroq(
    temperature=0,
    groq_api_key='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',
    model_name="llama-3.3-70b-versatile"
)
response = llm.invoke("The first person to land on moon was ... ")
# print(response.content)


### Web Scrapping
from langchain_community.document_loaders import WebBaseLoader
loader = WebBaseLoader("https://jobs.nike.com/job/R-48983?from=job%20search%20funnel")
page_data=loader.load().pop().page_content
# print(page_data)


from langchain_core.prompts import PromptTemplate
prompt_extract = PromptTemplate.from_template(
    """
    ### SCRAPPED TEXT FROM WEBSITE:
    {page_data}
    ### INSTRUCTIONS:
    The scrapped text is from the career's page of a website.
    Your job is to extract the job postings and return them in JSON format containing following keys: 'role','experience','skills' and 'description'.
    Only return the valid JSON.
    ### VALID JSON(NO PREAMBLE):
    """
)

chain_extract = prompt_extract | llm
res = chain_extract.invoke(input={'page_data':page_data})
# print(type(res.content))  # since it is in str format, we need to make it a JSON object (dict) , and for which we have to use parser for JSON

from langchain_core.output_parsers import JsonOutputParser
json_parser = JsonOutputParser()
json_res = json_parser.parse(res.content)
# print(json_res)
# print(type(json_res))     # It will be dictionary


### Now taking the data of the people's portfolio of our company and our company's projets' portfolio to write releveant mail

import pandas as pd
df = pd.read_csv("C://WIMAPPLY//Cold Email Generator//app//resource//my_portfolio.csv")
# print(df)


### Making its chromadb database
import chromadb
import uuid
 
client = chromadb.PersistentClient('vectorstore')   # Persistent client use karyu kem ke e disk par data store kari lese ane next time use  mate kaam aavse.
collection = client.get_or_create_collection(name="portfolio") 

if not collection.count():
    for _, row in df.iterrows():
        collection.add(documents=row["Techstack"],
        metadatas = {"links": row["Links"]},
        ids=[str(uuid.uuid4())])

# links = collection.query(query_texts=["Experience in Python","Expertise in React"],n_results=2).get('metadatas')
# print(links)

job=json_res
# print(job['skills'])    # These are basically the skills required in the job post.

### Now we have to pass all the skills required to the code of the links query. Basically above in place of "Experience in Python", we can paste our required skills and get the relevant portfolio links from our company & our sompanys' employees
links = collection.query(query_texts=job['skills'],n_results=2).get('metadatas')
# print(links)






### Now here we are generating he mail (giving the prompt for cold-email generation) 

prompt_email = PromptTemplate.from_template(
        """
        ### JOB DESCRIPTION:
        {job_description}
        
        ### INSTRUCTION:
        You are Mohan, a business development executive at AtliQ. AtliQ is an AI & Software Consulting company dedicated to facilitating
        the seamless integration of business processes through automated tools. 
        Over our experience, we have empowered numerous enterprises with tailored solutions, fostering scalability, 
        process optimization, cost reduction, and heightened overall efficiency. 
        Your job is to write a cold email to the client regarding the job mentioned above describing the capability of AtliQ 
        in fulfilling their needs.
        Also add the most relevant ones from the following links to showcase Atliq's portfolio: {link_list}
        Remember you are Mohan, BDE at AtliQ. 
        Do not provide a preamble.
        ### EMAIL (NO PREAMBLE):
        
        """
        )

chain_email = prompt_email | llm
res = chain_email.invoke({"job_description": str(job), "link_list": links})
print(res.content)   ### This is our generated cold-email. 

