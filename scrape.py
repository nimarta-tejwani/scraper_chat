import requests
from bs4 import BeautifulSoup

def scrape_data_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        soup = BeautifulSoup(response.text, 'html.parser')
        # Find all <p> tags and extract their text content
        paragraphs = soup.find_all('p')
        # Combine the text content from all paragraphs into a single string
        data = "\n".join(paragraph.get_text() for paragraph in paragraphs)
        return data
    except requests.exceptions.RequestException as e:
        return f"Error fetching data: {str(e)}"
    


# url = "https://www.iba-suk.edu.pk"
# print(scrape_data_from_url(url))