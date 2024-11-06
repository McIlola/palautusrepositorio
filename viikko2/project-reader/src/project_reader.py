from urllib import request
from project import Project
import tomllib


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        print(content)
        sisalto = tomllib.loads(content)
        print(sisalto)
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(sisalto["tool"]["poetry"]["name"],
                       sisalto["tool"]["poetry"]["description"],
                       sisalto["tool"]["poetry"]["license"],
                       sisalto["tool"]["poetry"]["authors"],
                       sisalto["tool"]["poetry"]["dependencies"], 
                       sisalto["tool"]["poetry"]["group"]["dev"]["dependencies"]
                       )
