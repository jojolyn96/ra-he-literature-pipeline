import requests

def search_semantic_scholar(query, limit=20):
    url = "https://api.semanticscholar.org/graph/v1/paper/search"
    
    params = {
        "query": query,
        "limit": limit,
        "fields": "title,abstract,year,authors,venue,externalIds"
    }

    response = requests.get(url, params=params)
    data = response.json()

    papers = []
    for item in data.get("data", []):
        papers.append({
            "title": item.get("title"),
            "abstract": item.get("abstract"),
            "year": item.get("year"),
            "authors": [a["name"] for a in item.get("authors", [])],
            "venue": item.get("venue"),
            "doi": item.get("externalIds", {}).get("DOI")
        })
    return papers
