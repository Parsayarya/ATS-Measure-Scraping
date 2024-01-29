import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# Initialize a DataFrame to store scraped data
data = pd.DataFrame(columns=['Document_Number', 'Subject', 'Status', 'Category', 'Topics', 'Title', 'Content'])

base_url = 'https://www.ats.aq/devAS/Meetings/Measure/'

for i in range(808, 0, -1):
    """
    Iterates through the specified range of document numbers to scrape data.
    
    :param i: Document number to be scraped.
    """

    # Construct the specific URL
    url = f"{base_url}{i}"

    try:
        response = requests.get(url)
        response.raise_for_status()

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find elements containing the required information
        elements = soup.find_all('span', class_='characteristics__item__text__text')
        content_div = soup.find('div', class_='text-container')
        Title = soup.find('h1', class_='title')

        if len(elements) >= 0:
            # Extract the required information from the elements
            subject = elements[0].get_text(strip=True) if len(elements) > 0 else None
            status = elements[1].get_text(strip=True) if len(elements) > 1 else None
            category = elements[2].get_text(strip=True) if len(elements) > 2 else None
            topics = elements[2].get_text(strip=True) if len(elements) > 3 else None
            content = content_div.get_text(strip=True) if content_div else None
            title = Title.get_text(strip=True) if content_div else None
            
            # Add the extracted information to the DataFrame
            data.loc[len(data)] ={
                'Document_Number': i,
                'Subject': subject,
                'Status': status,
                'Category': category,
                'Topics': topics,
                'Title': title,
                'Content': content
            }
        else:
            print(f"Couldn't find enough information on page {i}")

        # Pause between requests to avoid overloading the server
        time.sleep(1)

    except requests.HTTPError as e:
        # Handle HTTP errors
        print(f"Failed to retrieve page {i}: {e}")
    except requests.RequestException as e:
        # Handle other request-related errors
        print(f"A request error occurred: {e}")

# Save the scraped data to a CSV file
data.to_csv('scraped_content.csv', index=False)
