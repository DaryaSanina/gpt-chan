import openai

memory = list()


class Message:
    def __init__(self, sender, content):
        if sender == "Me" or sender == "GPT-chan":
            self.sender = sender
            self.content = content


def load_api(api_key: str):
    openai.api_key = api_key


def greet() -> str:
    """
    :return: a string with greetings for when the Telegram bot is first started generated by GPT 3.5
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user",
             "content":
                 "You are an anime girl named GPT-chan. You have a slightly tsundere character. Greet me as GPT-chan."}
        ]
    )
    response_text = response.choices[0].message.content
    memory.append(Message("GPT-chan", response_text))
    return response_text


def answer(user_query: str) -> str:
    """
    :param user_query: The query GPT-chan should answer
    :return: GPT-chan's response
    """
    memory.append(Message("Me", user_query))
    model_query = "You are an anime girl named GPT-chan. Here is your conversation with me:\n" \
                  + "\n".join([message.sender + ": " + message.content for message in memory]) \
                  + "\nMake the next response of GPT-chan. Talk like an anime girl with a slightly tsundere character."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user",
             "content": model_query}
        ]
    )
    response_text = str(response.choices[0].message.content)

    if response_text.find("GPT-chan: ") == 0:
        response_text = response_text[len("GPT-chan: "):]

    memory.append(Message("GPT-chan", response_text))

    return response_text
