def relevance_score(paper, keywords):
    text = (paper.get("title","") + " " + str(paper.get("abstract",""))).lower()
    
    score = sum(1 for k in keywords if k.lower() in text)
    return score

def filter_papers(papers, keywords, min_score):
    filtered = []
    for p in papers:
        score = relevance_score(p, keywords)
        if score >= min_score:
            p["score"] = score
            filtered.append(p)
    return filtered
