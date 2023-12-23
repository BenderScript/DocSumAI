import json
import os
import time

import openai
from dotenv import load_dotenv
from colorama import Fore, Style


def check_run(client, thread_id, run_id):
    while True:
        # Refresh the run object to get the latest status
        run = client.beta.threads.runs.retrieve(
            thread_id=thread_id,
            run_id=run_id
        )

        if run.status == "completed":
            print(f"{Fore.GREEN} Run is completed.{Style.RESET_ALL}")
            break
        elif run.status == "expired":
            print(f"{Fore.RED}Run is expired.{Style.RESET_ALL}")
            break
        else:
            print(f"{Fore.YELLOW} OpenAI: Run is not yet completed. Waiting...{run.status} {Style.RESET_ALL}")
            time.sleep(1)  # Wait for 1 second before checking again


def show_json(obj):
    print(json.loads(obj.model_dump_json()))


def submit_message(client, assistant_id, thread, user_message):
    client.beta.threads.messages.create(
        thread_id=thread.id, role="user", content=user_message
    )
    return client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant_id,
    )


# Pretty printing helper
def pretty_print(messages):
    print("# Messages")
    for m in messages:
        print(f"{m.role}: {m.content[0].text.value}")
    print()


def get_response(client, thread):
    messages = client.beta.threads.messages.list(thread_id=thread.id)
    show_json(messages)
    return messages


def create_thread_and_run(client, user_input, assistant_id):
    thread = client.beta.threads.create()
    print(f"{Fore.MAGENTA} Thread Info: {thread.id} {Style.RESET_ALL}")
    show_json(thread)
    run = submit_message(client, assistant_id, thread, user_input)
    return thread, run


def main():
    load_dotenv(override=True, dotenv_path=".env")  # take environment variables from .env.
    openai.api_key = os.getenv("OPENAI_API_KEY")

    client = openai.Client()

    print(f"{Fore.MAGENTA} Welcome to Large Document Summarization Assistant. I am here to help you summarize very "
          f"large files...{Style.RESET_ALL}\n")
    print(f"{Fore.MAGENTA} You can type `quit` to exit ...{Style.RESET_ALL}\n")

    assistant = client.beta.assistants.create(
        name="Document Summarization Assistant",
        instructions="You are document summarization assistant. You will summarize large documents",
        model="gpt-4-1106-preview"
    )

    doc_sum_id = assistant.id

    # Upload the file
    file = client.files.create(
        file=open(
            "./files/llm_survey.pdf",
            "rb",
        ),
        purpose="assistants",
    )
    # Update Assistant
    assistant = client.beta.assistants.update(
        doc_sum_id,
        tools=[{"type": "retrieval"}],
        file_ids=[file.id],
    )
    print(f"{Fore.MAGENTA} Assistant Info: {assistant.id} {Style.RESET_ALL}")
    show_json(assistant)

    thread, run = create_thread_and_run(client,
                                        "Summarize the document A Survey of Large Language Models. It is a large "
                                        "document so make sure the summary captures the important points",
                                        doc_sum_id
                                        )

    print(f"{Fore.MAGENTA} Run Info: {assistant.id} {Style.RESET_ALL}")
    show_json(run)

    check_run(client, thread.id, run.id)
    pretty_print(get_response(client, thread))


if __name__ == "__main__":
    main()
