import requests

def search(query):
    url = "https://www.googleapis.com/customsearch/v1"  # Google Custom Search API URL
    api_key = "AIzaSyArmR0VWxfyy5urqsX0nI-Ngb8L3iLGVe8"  # Replace with your own API key
    cx = "7647ac75be2b045ea"  # Replace with your own search engine ID
    params = {
        "key": api_key,
        "cx": cx,
        "q": query
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data

def get_answer(query):
    data = search(query)
    if "items" in data and len(data["items"]) > 0:
        top_result = data["items"][0]
        if "title" in top_result and "snippet" in top_result:
            title = top_result["title"]
            snippet = top_result["snippet"]
            return f"{title}\n\n{snippet}"
    return "Sorry, I couldn't find an answer to your question."

# Main loop
while True:
    user_input = input("User: ")
    if user_input.lower() == "exit":
        break
    answer = get_answer(user_input)
    print("Chatbot:", answer)
