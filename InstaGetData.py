import requests
import csv
import os

# Instagram Graph API setup
access_token = 'IGAA1y2H5SISNBZAE4wcEZALcUZAtRVkwUUduUzMyaUZAsRmxvaTNwbWhRdGZAJNTgyd3lXLVlXWXZAjQzZAJcWRUS3VqQVRGSnY4Y1hDVGcyM1ZAiZAHdyUjc4NmRfaG9XWXNBeGFZAb09kbG5sRFRSWlhCXzlucEhJa1FnWEt2Ym9qSk4yWQZDZD'  # Replace with your long-lived access token
instagram_business_account_id = '17841472046381403'  # Replace with your Instagram business account ID

# Base URL for the Instagram Graph API
base_url = f'https://graph.instagram.com/{instagram_business_account_id}'

# Function to fetch posts data
def fetch_instagram_posts():
    url = f'{base_url}/media?fields=id,media_type,permalink,timestamp,like_count,comments_count&access_token={access_token}'

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        return data.get('data', [])
    else:
        print(f"Error fetching data: {data.get('error', {}).get('message')}")
        return []

# Function to read existing post IDs from the CSV
def read_existing_post_ids(csv_file):
    post_ids = set()
    if os.path.exists(csv_file):
        with open(csv_file, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                post_ids.add(row[0])  # Add the post ID to the set
    return post_ids

# Function to store or update post data in CSV
def store_or_update_in_csv(posts, csv_file):
    existing_post_ids = read_existing_post_ids(csv_file)
    
    # Create CSV file with headers if it doesn't exist
    if not os.path.exists(csv_file):
        with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Post_ID', 'Media_Type', 'Permalink', 'Timestamp', 'Likes', 'Comments'])

    # Append new posts or update existing ones
    with open(csv_file, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for post in posts:
            post_id = post.get('id')
            media_type = post.get('media_type')
            permalink = post.get('permalink', '')
            timestamp = post.get('timestamp', '')
            likes = post.get('like_count', 0)
            comments = post.get('comments_count', 0)

            # Check if post ID exists, if not, add it as a new post
            if post_id not in existing_post_ids:
                writer.writerow([post_id, media_type, permalink, timestamp, likes, comments])
                print(f"Adding new post: {post_id}")
            else:
                # Update existing post's likes and comments
                print(f"Updating post: {post_id}")
                update_existing_post(csv_file, post_id, likes, comments)

# Function to update existing post data
def update_existing_post(csv_file, post_id, likes, comments):
    lines = []
    with open(csv_file, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == post_id:
                row[4] = likes  # Update likes (column 4)
                row[5] = comments  # Update comments (column 5)
            lines.append(row)

    # Write updated data back to the CSV
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(lines)

# Main function to fetch, store, or update Instagram data
def main():
    posts = fetch_instagram_posts()
    if posts:
        store_or_update_in_csv(posts, 'instagram_data.csv')
        print("Data fetched and stored/updated successfully!")
    else:
        print("No data to store.")

# Run the script
if __name__ == '__main__':
    main()
