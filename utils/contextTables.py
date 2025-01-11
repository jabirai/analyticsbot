import numpy as np
import json
from openai import OpenAI
from dotenv import dotenv_values
vars = dotenv_values(".env")

client = OpenAI(api_key=vars['openapi_key'])

def get_relevant_schemas_from_hierarchy(user_query, hierarchy):
    prompt = f"""
    Here is the database schema hierarchy:
    {hierarchy}
    
    User Query: "{user_query}"
    
    Step 1: Based on the user's query, determine the most relevant schemas and tables.
    Step 2: Output the relevant schema and table names as a same structure given in the input format.
    """

    # Make the OpenAI API call
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an assistant for determining database schema relevance."},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )
    response_text = response.choices[0].message.content

    return response_text

