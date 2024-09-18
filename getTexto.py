'''Este scrip va a obter el texto para pasarselo al scrip getTrack_**'''
#imports
import lxml_html_clean
import lxml
import newspaper
from newspaper import Article

def getText(url):
    article = Article(url)

    ##Puede fallar al descargar el articulo por proteccion del articulo a las descargas.
    try:
        article.download()
        article.parse()
    except newspaper.article.ArticleException:
        print("No se puedo descargar el artículo solicitado, sorry")
        return "No se pudo descargar el texto"
    
    # Extract and print the desired data
    # print("**Headline:**", article.title)
    # print("**Authors:**", article.authors)
    # print("**Publication Date:**", article.publish_date)
    # print("**Main Text:**", article.text)
    return 'Título. ' + article.title + '. '+ article.text
