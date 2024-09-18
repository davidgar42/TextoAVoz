'''Este scrip va a obter el texto para pasarselo al scrip getTrack'''
#imports
import lxml_html_clean
import lxml
from newspaper import Article

def getText(url):
    article = Article(url)
    article.download()
    ##Puede fallar al descargar el articulo
    article.parse()
    # Extract and print the desired data
    # print("**Headline:**", article.title)
    # print("**Authors:**", article.authors)
    # print("**Publication Date:**", article.publish_date)
    # print("**Main Text:**", article.text)
    return article.text
