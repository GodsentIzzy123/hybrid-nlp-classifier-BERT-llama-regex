from dotenv import load_dotenv
import os
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

def classify_with_llm(log_message):
    prompt = f'''Classify the log message into one of these categories:
    (1) Workflow Error, (2) Deprecation Warning.
    If you cant figure out a category, return "Unclassified".
    Only return the category name. No preamble at all.
    Log message : {log_message}'''


    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
    model="llama-3.3-70b-versatile",
)


    return chat_completion.choices[0].message.content



if __name__ == "__main__":
    print(classify_with_llm("Case Escalation for ticket ID 7324 failed because the assigned support agent was inactive"))
    print(classify_with_llm("The 'ReportGenerator' module will be retired in version 4.0 . Please migrate quickly ]"))
    print(classify_with_llm("System reboot initiated by User 12345."))     
                            

    