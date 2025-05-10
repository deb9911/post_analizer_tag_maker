import requests

ACCESS_TOKEN = 'YOUR_PAGE_ACCESS_TOKEN'
PAGE_ID = 'your_page_id'  # or 'page_username'
GRAPH_URL = f'https://graph.facebook.com/v18.0'

# Get latest posts from the page
posts_url = f'{GRAPH_URL}/{PAGE_ID}/posts?access_token={ACCESS_TOKEN}'
posts_resp = requests.get(posts_url).json()

for post in posts_resp.get('data', []):
    post_id = post['id']
    print(f"\nPost ID: {post_id}")

    # Fetch comments for each post
    comments_url = f'{GRAPH_URL}/{post_id}/comments?access_token={ACCESS_TOKEN}'
    comments_resp = requests.get(comments_url).json()

    print("Comments:")
    for comment in comments_resp.get('data', []):
        user = comment['from']['name']
        message = comment['message']
        print(f"- {user}: {message}")

  
