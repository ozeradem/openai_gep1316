import time
from dotenv import find_dotenv, load_dotenv
from openai import OpenAI

load_dotenv()

# Enter your Assistant ID here.
ASSISTANT_ID = "asst_p3xGjeDhFW3cGfbkmCD60KhT"

# Make sure your API key is set as an environment variable.
# client = OpenAI(
#   api_key=os.environ.get("CUSTOM_ENV_NAME"),
# )

client = OpenAI()


# Create a thread with a message.
thread = client.beta.threads.create(
    messages=[
        {
            "role": "user",
            # Update this with the query you want to use.
            "content": "Yeteneklerin hakkında bilgi verebilir misin?",
        }
    ]
)

print(f"thread_id: {thread.id}")

# Submit the thread to the assistant (as a new run).
run = client.beta.threads.runs.create(thread_id=thread.id, assistant_id=ASSISTANT_ID)
print(f"👉 Run Created: {run.id}")

# Wait for run to complete.
while run.status != "completed":
    run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
    print(f"🏃 Run Status: {run.status}")
    time.sleep(1)
else:
    print(f"🏁 Run Completed!")

# Get the latest message from the thread.
message_response = client.beta.threads.messages.list(thread_id=thread.id)
messages = message_response.data

# Print the latest message.
latest_message = messages[0]
print(f"💬 Response: {latest_message.content[0].text.value}")