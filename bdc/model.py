########################
# 
# La boîte du chercheur
# @DemangeJeremy
# 
########################
import gradio as gr

import uuid
import os
class BaseBoite:
    """
    Classe de base pour le catalogue.
    """

    title = "... >> ..."
    categories = []
    link = "/app/dot_to_dot"
    shortDescription = "Your short description."
    bigDescription = """..."""
    inputs = []
    outputs = []
    examples=[]
    css="footer {visibility: hidden} h1 {text-align: left!important} .gr-button-primary {background-color: #004AAD!important; color: white!important; --tw-gradient-stops: inherit, rgb(255 255 255 / 0) !important; border: none!important}"

    def info(self):
        return {
            "title": self.title,
            "description": self.shortDescription,
            "link": self.link,
            "categories": self.categories
        }

    def execute(self):
        pass

    def echo(text, request: gr.Request):
        if request:
            print("Request headers dictionary:", request.headers)
            print("IP address:", request.client.host)
            print("Query parameters:", dict(request.query_params))
        return text

    def executeSecure(self, *args, request: gr.Request):
        if request:
            print("Request headers dictionary:", request.headers)
            print("IP address:", request.client.host)
            print("Query parameters:", dict(request.query_params))
        try:
            return self.execute(*args)
        except Exception as e:
            print(e)
            return "Une erreur est survenue. Vérifier vos paramètres et votre fichier."

    def app(self):
        return gr.Interface(
            title=self.title,
            description=self.shortDescription,
            article=self.bigDescription,
            fn=self.execute,
            inputs=self.inputs,
            outputs=self.outputs,
            css=self.css,
            allow_flagging="never",
            examples=self.examples,
            theme=gr.themes.Default(primary_hue=gr.themes.colors.blue, secondary_hue=gr.themes.colors.blue)
        )

def getUniqueFilename(extension: str=".txt"):
    """
    Fonction pour récuperer un lieu sûr d'enregistrement de fichiers.
    """

    tempPath = os.environ["TMPDIR"]
    filename = tempPath + str(uuid.uuid4()) + extension
    return filename

def saveByTxt(txt: str, extension: str=".txt"):
    """
    Fonction pour enregistrer un fichier avec une base texte.
    """

    filename = getUniqueFilename(extension)
    with open(filename, "w") as w:
        w.write(txt)
    return filename