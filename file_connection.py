import json


def get_articles():
    with open("articles.json","r",encoding="utf-8") as f:
        data = json.load(f)
        return data
def save_article(name, text):
    data = get_articles()
    data[name] = text
    with open("articles.json","w",encoding="utf-8") as f:
        json.dump(data,f,ensure_ascii=False)
def delete_article(name):
    data = get_articles()
    del data [name]
    with open("articles.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)


