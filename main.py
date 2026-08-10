# This code imports our Semantic Scholar search function, searches for papers about federated learning, and prints the number and basic details of the returned papers.
from src.retrieval.semantic_scholar import search_papers

results = search_papers("federated learning", limit=5)

print("Total matching papers:", results["total"])

for paper in results["data"]:
    print("\nTitle:", paper["title"])
    print("Year:", paper["year"])
    print("Abstract:", paper["abstract"])