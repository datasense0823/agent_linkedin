import os
from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from tools.webscrap import webscrap
from tools.linkedin_url import linkedin_url

# Load environment variables
load_dotenv()

def generate_profile_summary_and_facts_single_step(name: str):
    # Initialize the LLM
    llm = ChatOpenAI(temperature=0, model_name="gpt-4")
    
    # Define tools
    tools_for_agent = [linkedin_url, webscrap]
    
    # React agent setup
    react_prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)
    
    # Single agentic input prompt
    prompt = f"""
You are an intelligent assistant. Given a Person's {name} Your task is to generate:
    - A brief LinkedIn summary highlighting key aspects of the profile.
    - Two interesting facts about the person derived from the profile.
    - Linked in Profile PIC URL

Please provide the final output as a JSON object with keys 'summary' and 'interesting_facts'.
"""
    
    # Execute the agent
    result = agent_executor.invoke(input={"input": prompt})
    return result["output"]

# Example usage
if __name__ == "__main__":
    name = input("Enter the full name: ")
    result = generate_profile_summary_and_facts_single_step(name)
    print("Generated Output:\n", result)
