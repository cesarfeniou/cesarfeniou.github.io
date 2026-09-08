"""
sync_scholar.py
Fetches publications from Google Scholar and merges them into _bibliography/papers.bib.
Run via GitHub Actions (see .github/workflows/sync-scholar.yml).

Setup:
  Set SCHOLAR_ID to override the default profile when running locally.
"""

import os
import re
import time
import bibtexparser
from scholarly import scholarly, ProxyGenerator

SCHOLAR_ID = os.environ.get("SCHOLAR_ID", "atHK9rYAAAAJ")
BIB_PATH   = "_bibliography/papers.bib"

# ── Optional: use a free proxy to avoid rate-limiting ──────────────────────
# pg = ProxyGenerator()
# pg.FreeProxies()
# scholarly.use_proxy(pg)
# ───────────────────────────────────────────────────────────────────────────

def slugify(title: str) -> str:
    """Turn a title into a safe BibTeX key."""
    title = title.lower()
    title = re.sub(r"[^a-z0-9\s]", "", title)
    words = title.split()[:4]
    return "".join(words)

def fetch_publications(author_id: str) -> list[dict]:
    author = scholarly.search_author_id(author_id)
    author = scholarly.fill(author, sections=["publications"])
    pubs = []
    for pub in author["publications"]:
        # The author record already contains the metadata needed for the
        # bibliography. Avoid filling every publication separately: doing so
        # creates dozens of requests and is frequently blocked on CI runners.
        bib = pub.get("bib", {})
        pubs.append({
            "title":   bib.get("title", ""),
            "author":  bib.get("author", ""),
            "year":    str(bib.get("pub_year", "")),
            "journal": bib.get("citation", ""),
            "volume":  "",
            "pages":   "",
            "url":     pub.get("pub_url", ""),
            "abstract":"",
        })
    return pubs

def load_existing_bib(path: str) -> bibtexparser.bibdatabase.BibDatabase:
    if not os.path.exists(path):
        return bibtexparser.bibdatabase.BibDatabase()
    with open(path, encoding="utf-8") as f:
        return bibtexparser.load(f)

def merge(db: bibtexparser.bibdatabase.BibDatabase, pubs: list[dict]):
    existing_titles = {
        e.get("title", "").lower().strip()
        for e in db.entries
    }
    added = 0
    for pub in pubs:
        title = pub["title"].strip()
        if title.lower() in existing_titles:
            continue
        key = slugify(title) + pub["year"]
        entry = {
            "ENTRYTYPE": "article",
            "ID":        key,
            "title":     title,
            "author":    pub["author"],
            "year":      pub["year"],
            "journal":   pub["journal"],
            "volume":    pub["volume"],
            "pages":     pub["pages"],
            "url":       pub["url"],
            "abstract":  pub["abstract"],
        }
        # Remove empty fields
        entry = {k: v for k, v in entry.items() if v}
        db.entries.append(entry)
        existing_titles.add(title.lower())
        added += 1
        print(f"  + Added: {title[:70]}")
    print(f"Sync complete — {added} new publication(s) added.")

def write_bib(db: bibtexparser.bibdatabase.BibDatabase, path: str):
    writer = bibtexparser.bwriter.BibTexWriter()
    writer.indent = "  "
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(writer.write(db))

if __name__ == "__main__":
    if not SCHOLAR_ID:
        raise ValueError("SCHOLAR_ID environment variable is not set.")
    print(f"Fetching publications for Scholar ID: {SCHOLAR_ID}")
    pubs = fetch_publications(SCHOLAR_ID)
    print(f"Found {len(pubs)} publication(s) on Scholar.")
    db = load_existing_bib(BIB_PATH)
    merge(db, pubs)
    write_bib(db, BIB_PATH)
