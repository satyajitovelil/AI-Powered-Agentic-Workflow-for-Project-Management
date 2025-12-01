# TODO: 1 - Import the AugmentedPromptAgent class
from workflow_agents.base_agents import AugmentedPromptAgent
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(os.path.join(os.getcwd(),'.env'))

# Retrieve OpenAI API key from environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")

prompt = "What is the capital of France?"
persona = "You are a college professor; your answers always start with: 'Dear students,'"

# TODO: 2 - Instantiate an object of AugmentedPromptAgent with the required parameters
augmented_agent = AugmentedPromptAgent(openai_api_key, persona)
# TODO: 3 - Send the 'prompt' to the agent and store the response in a variable named 'augmented_agent_response'
augmented_agent_response = augmented_agent.respond(prompt)
# Print the agent's response
print("Printing Augmented Agent's Response...\n")
print(augmented_agent_response)

# TODO: 4 - Add a comment explaining:
print("\n")
print("Explaination for the above response: \n"
"- What knowledge the agent likely used to answer the prompt. \n"
"- The agent most likely used GPT-3.5-turbo’s general world knowledge (its pre-trained knowledge base up to its training cutoff)\n"
"  to know that Paris is the capital of France.\n"

"- How the system prompt specifying the persona affected the agent's response.\n"
"- The Response will be to the point and using the persona we provided as we have prompted it to forget all previous context.\n"
)


