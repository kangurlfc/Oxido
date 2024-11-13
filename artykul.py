from openai import OpenAI
import requests


class OpenAIAPI:
    # this class retrieves and stores data from the given URL
    def __init__(self):
        self.url = "https://cdn.oxido.pl/hr/Zadanie%20dla%20JJunior%20AI%20Developera%20-%20tresc%20artykulu.txt"

    @property
    def text(self) -> str:
        response = requests.get(self.url)
        if response.status_code != 200:
            # making sure the request was successful and correctly handles non ASCII characters
            raise Exception("Failed to retrieve data")
        response.encoding = 'UTF-8'
        with open("artykul_przykladowy.txt", 'w', encoding='utf-8') as file:
            file.write(response.text)
        return response.text

    def prompt(self, prompt: str) -> str:
        client = OpenAI()
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system",
                 "content": "You are a helpful assistant."},
                {
                    "role": "user",
                    "content": f"'{self.text}' - #PROMPT TEXT"
                }
            ]
        )
        return completion.choices[0].message['content']

    def save(self, filename="artykul.html"):
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(self.prompt)


def main():
    api = OpenAIAPI()
    ...

if __name__ == "__main__":
    main()
