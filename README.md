This project aims to analyze Instagram post insights using the Instagram Graph API, store the fetched data in AstraDB, and process the data through Langflow integrated with Google Gemini API.

---

## 1. Using Instagram Graph API via Meta for Developers

### Process to Access the Instagram API:

- Registered a **Meta Developer account** and created an **Instagram App** to gain access to the Instagram Graph API.
- Generated an **Access Token** by setting up **OAuth** authentication using the App credentials.
- Utilized the **Instagram Business Account** to request necessary API permissions, including `instagram_basic`, `instagram_manage_insights`, and `pages_read_engagement`.
- After authorization, API requests were made to the following key endpoints:
    - `/me/accounts` to retrieve account info.
    - `/media` for post details.
    - `/media_insights` for fetching engagement metrics like likes, comments, and reach.

---

## 2. Storing Data in CSV Format and Uploading to AstraDB

### Python Script Overview:

- The Python script was designed to:
    - Connect to the Instagram Graph API using the access token.
    - Parse the JSON response from the API to extract relevant post metrics:
        - Post ID, Number of Likes, Number of Comments, Media Type, Permalink and Timestamp.
    - Store the parsed data into a **CSV file** for further use.
- Once the CSV file was created, the script:
    - Uploaded the data to **AstraDB**, using the **CSV file** upload.
    - Ensured data integrity by validating that the CSV columns matched the database schema in AstraDB.

### Data Fields:

- **Post ID**
- **Media Type - ( Static Image, Carousel , Reels)**
- **Likes**
- **Comments**
- **Permalink**
- **Timestamp - Time of Post Upload**

---

## 3. Creating Langflow Flow with AstraDB and Google Gemini API

### Google Gemini API Integration:

- Signed up for **Google Gemini API** to perform advanced data analysis on Instagram post metrics.
- Obtained the **Gemini API key** after configuring the API project in **Google Cloud Console**.
- The API key was securely integrated into the Langflow pipeline for connecting to Gemini.

### Langflow Flow:

- The Langflow flow was designed to take data from AstraDB and process it through the Gemini API:
    1. **Data Ingestion**: Fetched data directly from AstraDB via the AstraDB Tool
    2. **Parsing Data** - Used the Parse Data from the processing options to get text output of the data fields associated with each post. 
    3. **API Interaction**: Passed the data into the Google Generative AI from the models option for deeper insights.
    4. **Results Display**: The processed results were displayed in Langflow as engagement insights (e.g., trends, behavior analysis, post performance predictions).

---

## 4. Getting the Output in Langflow Playground

### Example Output

- The Langflow Playground displays the output based on the analysis done via Gemini API and data from AstraDB.

### Sample Output Format:

**Prompt** : Can you provide me based on the data on what format works best. Compare the average engagement of all three types of posts. Give a bit detailed with the information from the data. I want facts and figures.

**Output :** 

Based on the provided data, we can compare the average engagement of Reels, Images, and Carousel Albums.  Engagement will be measured as the sum of likes and comments.

**Reels:**

- **Total Engagement:** There are three reels. Reel 1 (Post ID 18252308083274439) had 27 engagements (17 likes + 10 comments). Reel 2 (Post ID 18352223557192810) had 28 engagements (16 likes + 12 comments). Reel 3 (Post ID 18113657428435442) had 25 engagements (14 likes + 11 comments). The total engagement for reels is 80.
- **Average Engagement per Reel:** 80 / 3 = 26.67.

**Images:**

- **Total Engagement:** There are four image posts. Post ID 17906123985009386 had 9 engagements (7 likes + 2 comments). Post ID 18121412002409588 had 8 engagements (7 likes + 1 comment). Post ID 18044329751240060 had 10 engagements (9 likes + 1 comment).
- **Average Engagement per Image:** 27 / 4 = 6.75.

**Carousel Albums:**

- **Total Engagement:** There are three carousel album posts. Post ID 18265371160268031 had 13 engagements (11 likes + 2 comments). Post ID 18102325633469516 had 13 engagements (10 likes + 3 comments). Post ID 18450562792070129 had 13 engagements (10 likes + 3 comments). The total engagement for carousel albums is 39.
- **Average Engagement per Carousel Album:** 39 / 3 = 13.

**Conclusion:**

Based purely on this limited dataset, Reels show significantly higher average engagement (26.67) compared to Images (6.75) and Carousel Albums (13).

**Links**
Youtube:https://youtu.be/jIl7x931NRE?si=tMdpQPIiv5k8cG1x


