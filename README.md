# ATS-Measure-Scraping



**Description**:

This Python script is designed to automate the collection of data from the Antarctic Treaty System's official website. It scrapes information related to various documents, such as measures and resolutions, and organizes this data into a structured format.


**Functionality**:

The script uses the requests library to access and download content from a specified range of document pages on the ATS website.
BeautifulSoup from the bs4 package is employed to parse the HTML content of each page, extracting relevant information.
Extracted data includes document number, subject, status, category, topics, title, and content.
The script iteratively processes each document, starting from the most recent (document number 808) and working backward.
To avoid overwhelming the server, a pause of 1 second is implemented between requests.
The extracted information is compiled into a pandas DataFrame and subsequently saved as a CSV file named 'scraped_content.csv'.

**Usage**:

Ensure you have Python installed along with the required libraries: requests, beautifulsoup4, and pandas.
Run the script to start the data scraping process. The script outputs a CSV file containing all scraped data.

**Dataset Description**:
This dataset created represents a complete archive of measures, resolutions, and decisions from the Antarctic Treaty System (ATS). It holds a wide range of documents, with details of important agreements and actions taken under the ATS framework. Each record in the dataset includes a unique document number, subject, status, category, and topics related to the Antarctic Treaty and its associated meetings.

Below is a description for each column in the dataset:

*  **Document_Number**: This column assigns a unique identifier to each document in the dataset, facilitating easy reference and organization.

*  **Subject**: This field describes the main focus or topic of the document. It provides a brief overview of the content and purpose of each resolution or decision.

*  **Status**: Indicates the current state or outcome of the document, such as whether it was adopted, proposed, or is still under consideration. This helps in understanding the progress and implementation of various measures.

*  **Category**: Categorizes each document into a specific area of interest or relevance within the Antarctic Treaty System. Examples might include environmental protection, scientific research, tourism, etc.

*  **Topics**: This column lists the specific topics or issues addressed in the document. It provides a more detailed view of the subjects within the broader category.

*  **Title**: The official title of the document. This often includes the resolution or decision number and the year, offering a formal and precise reference.

*  **Content**: This field contains the full text of the document. It is essential to understand the specifics of each measure or resolution.

*  **Measure**: Denotes the type of action taken, such as a resolution, a measure, or a decision. This helps classify the documents according to the nature of the action.

*  **Year**: Indicates the year in which the document was issued or the resolution was passed. This is crucial for historical context and temporal analysis.

*  **ATCM**: Refers to the specific Antarctic Treaty Consultative Meeting during which the document was discussed or adopted. It provides context about the meeting where the decisions were made.

*  **Feature**: This could refer to specific features or characteristics of the document or the meeting, such as special declarations or themes.

*  **City**: The city where the ATCM was held. This geographical information adds to the understanding of where the decisions were made, which can be relevant for regional studies and analyses.

**Acknowledgement:**

Research funded by Australian Research Council SRIEAS Grant SR200100005 Securing Antarctica’s Environmental Future.


**Note**:

This script is intended for educational or research purposes. Always respect the website's terms of service and use web scraping responsibly.
Handle errors and exceptions appropriately to avoid disruption of the website's normal functioning.
Modify the range of document numbers as needed based on the specific requirements of your project.
