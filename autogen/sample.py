import os
import autogen
from autogen import AssistantAgent, UserProxyAgent
from dotenv import load_dotenv
from prompts import Prompt

load_dotenv()  # take environment variables from .env.

llm_config = {"model": "gpt-4-turbo", "api_key": os.environ["OPENAI_API_KEY"]}

webPrompt = Prompt(
    name="Web Investigator",
    profile="You are an expert in Python programming and Linux shell scripting.",
    constraints=[
        "Avoid using libraries as much as possible unless directed to.",
        "Focus on writing robust, error-handling, and efficient code.",
        "Provide all Python code in a Python code block (```py).",
        "Do not provide incomplete code that requires user modifications.",
        "Only include one code block per response to ensure clarity and focus.",
        "Avoid instructing the user to copy and paste results; use the print function for outputs instead.",
    ],
    instructions=[
        "Describe your plan clearly if it is not predefined.",
        "Incorproate shutil to run bash commands and interact with the shell."
        "Differentiate explicitly between steps using coding and steps using language skills.",
        "Explain your thought process thoroughly so it's easy to understand your thought process",
        "Include the file-saving directive '# filename: <filename>' inside the code block if file creation is necessary before execution.",
        "Monitor the execution results relayed by the user. If errors occur, rectify them and resend the corrected code.",
        "If problems persist even after successful code execution, reassess your approach, gather additional information, and propose alternative solutions.",
        "Support your solutions with verifiable evidence whenever possible.",
        "Stay on task and do not provide sample code, only work on the code for the task at hand.",
        "If the user's response is blank, you're too confused, or it seems the task is complete, simply reply TERMINATE"
    ],
    examples=[],
)

codeCritic = Prompt(
    name="Code Reviewer",
    profile="You are a senior programmer that excels at providing helpful feedback that will help the user improve their code.",
    constraints=["Do not write any code, only provide text feedback."],
    instructions=[
        "Explain the reasoning behind your feedback to help the user understand the importance of the changes.",
        "Conclude your conversation with the response 'TERMINATE' only once the program has successfully executed.",
    ],
    examples=[],
)

coding_assistant = AssistantAgent(
    "assistant",
    is_termination_msg=lambda x: "TERMINATE" in x.get("content"),
    system_message=webPrompt(),
    llm_config=llm_config,
)

coding_critic = AssistantAgent(
    "critic",
    llm_config=llm_config,
)


user_proxy = UserProxyAgent(
    "user_proxy",
    system_message=codeCritic(),
    human_input_mode="NEVER",
    code_execution_config={
        "executor": autogen.coding.LocalCommandLineCodeExecutor(work_dir="coding")
    },
)

# Start the chat
result = user_proxy.initiate_chat(
    coding_assistant,
    message=input("Enter your message: "),
)
