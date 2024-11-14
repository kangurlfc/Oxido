from openai import OpenAI
import os
import requests


class OpenAIAPI:
    # This class retrieves and stores data from the given URL
    def __init__(self, key=None):
        # If API key is not provided, check environment variables
        if key is None:
            key = os.getenv('OPENAI_API_KEY')  # Look for the key in environment variables
        if not key:
            raise ValueError("OpenAI API key is required but not provided.")

        self.client = OpenAI(api_key=key)  # Initialize with API key
        self.url = "https://cdn.oxido.pl/hr/Zadanie%20dla%20JJunior%20AI%20Developera%20-%20tresc%20artykulu.txt"

    @property
    def text(self) -> str:
        response = requests.get(self.url)
        if response.status_code != 200:
            # Making sure the request was successful and correctly handles non ASCII characters
            raise Exception("Failed to retrieve data")
        response.encoding = 'UTF-8'
        with open("artykul_przykladowy.txt", 'w', encoding='utf-8') as file:
            file.write(response.text)
        return response.text

    def prompt(self, prompt: str = None) -> str:
        # Setting up this method for future usability. If the user doesn't provide a prompt, use default.
        try:
            if prompt is None:
                prompt = """
                Format the given text as a HTML body element but without the html,head and body tags.Follow these rules:
    
                1) Only HTML elements — no CSS or JavaScript code is allowed.
    
                2) Identify locations in the text where images would enhance understanding. Insert <figure> elements 
                containing <img src="image_placeholder.jpg" alt="..."> tags at each of these locations, with an alt 
                attribute  containing a detailed description of the image that could be AI-generated. Also, add captions 
                of the generated photo in <figcaption> tags. By default, the images should be placed below the relevant 
                text, but if the context suits it better, wrap the image with right alignment. The language of the alt 
                text and captions should be the same as the language of the main text. 
    
                3) Headers are paragraphs that end without a full stop. Wrap them in <h1>, <h2>, etc., as appropriate, 
                and add anchor links using unique id attributes.
    
                4) Tag each paragraph with <p> tags.
    
                5) Use unordered lists where appropriate to improve readability.
    
                6) Find the most crucial parts of the text and tag them as <strong>. Avoid tagging single words, focus on powerful phrases. Don't overdo it though.
                
                7) Add <hr> before the footnote and then put the footnote in a <small> element.
    
                8) Use italics for company and product names.
                
                Do not wrap the output in any code block or triple quotes. Just provide the raw HTML content.
                """
            client = OpenAI()
            completion = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system",
                     "content": "You are a helpful assistant."},
                    {
                        "role": "user",
                        "content": f"'{self.text}'\n{prompt}"
                    }
                ]
            )
            return completion.choices[0].message.content.strip()
        except Exception as e:
            raise Exception(f"An error occurred: {e}")

    def save(self, filename="artykul.html"):
        # Saving Open AI's output to .html format
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(self.prompt())


def main():
    api = OpenAIAPI()
    api.prompt()
    api.save()


if __name__ == "__main__":
    main()
