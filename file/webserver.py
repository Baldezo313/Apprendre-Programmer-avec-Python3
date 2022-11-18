import cherrypy

#  =========================================================


# class MonSiteWeb(object):               # Classe maître de l'application
#     def index(self):                    # Méthode invoquée comme URL racine (/)
#         # Renvoie d'une page HTML contenant un lien vers une autre page
#         # (laquelle sera produite par une autre méthode du même objet)
#         return '''
#             <h2>Veuillez <a href="unMessage">cliquer ici</a>
#             pour accéder à une information d'importance cruciale.</h2>
#             '''
#     index.exposed = True                # La méthode doit être 'publiée'
#
#     def unMessage(self):
#         return "<h1>La programmation, c'est géniale !</h1>"
#     unMessage.exposed = True
#
# # ==== Programme Principale =====
# cherrypy.quickstart(MonSiteWeb(), config="tutoriel.conf")
# =============================================================================


# class Bienvenue(object):
#     def index(self):
#         # Formulaire demandant son nom à l'utilisateur :
#         return '''
#         <form action="salutations" method="GET">
#         Bonjour. Quel est votre nom ?
#         <input type="text" name="nom" />
#         <input type="submit" value="OK" />
#         </form>
#         '''
#     index.exposed = True
#
#     def salutations(self, nom=None):
#         if nom:                     # Accueil de l'utilisateur :
#             return "Bonjour, {0}, comment allez-vous ?".format(nom)
#         else:                       # Aucun nom n'a été fourni :
#             return 'Veuillez svp fournir votre nom <a href="/">ici</a>.'
#     salutations.exposed = True
#
# cherrypy.quickstart(Bienvenue(), config="tutoriel.conf")

# =====================================================


# class HomePage(object):
#     def __init__(self):
#         # Les objets gestionnaires de requêtes peuvent instancier eux-mêmes
#         # d'autres gestionnaires "esclaves", et ainsi de suite :
#         self.maxime = MaximeDuJour()
#         self.liens = PageDeLiens()
#         # L'instanciation d'objets gestionnaires de requêtes peut bien entendu
#         # être effectuée à n'importe que niveau du programme.
#
#     def index(self):
#         return '''
#             <h3>Site des adorateurs du Python royal - Page d'accueil.</h3>
#             <p>Veuillez visiter nos rubriques géniales :</p>
#             <ul>
#                 <li><a href="/entreNous">Restons entre nous</a></li>
#                 <li><a href="/maxime/">Une maxime subtile</a></li>
#                 <li><a href="/liens/utiles">Des liens utiles</a></li>
#             </ul>
#         '''
#     index.exposed = True
#
#     def entreNous(self):
#         return '''
#             Cette page est produite à la racine du site.<br />
#             [<a href="/">Retour</a>]
#         '''
#     entreNous.exposed = True
#
#
# class MaximeDuJour(object):
#     def index(self):
#         return '''
#             <h3>Il existe 10 sortes de gens : ceux qui comprennent le binaire, et les autres !</h3>
#             <p>[<a href="../">Retour</a>]</p>
#         '''
#     index.exposed = True
#
#
# class PageDeLiens(object):
#     def __init__(self):
#         self.extra = LiensSupplementaires()
#
#     def index(self):
#         return '''
#             <p>Page racine des liens (sans utilité réelle).</p>
#             <p>En fait, les liens <a href="utiles">sont plutôt ici</a></p>
#         '''
#     index.exposed = True
#
#     def utiles(self):
#         # Veuillez noter comment le lien vers les pages est défini :
#         # on peut procéder de manière ABSOLUE ou RELATIVE.
#         return '''
#             <p>Quelques liens utiles :</p>
#             <ul>
#                 <li><a href="http://www.cherrypy.org">Site de CherryPy</a></li>
#                 <li><a href="http://www.python.org">Site de Python</a></li>
#             </ul>
#             <p>D'autres liens utiles vous sont proposés
#             <a href="./extra/" ici </a>.</p>
#             <p>[<a href="../">Retour</a>]</p>
#         '''
#     utiles.exposed = True
#
#
# class LiensSupplementaires(object):
#     def index(self):
#         # Notez le lien relatif pour retourner à la page maîtresse :
#         return '''
#             <p>Encore quelques autres liens utiles :</p>
#             <ul>
#                 <li><a href="http://pythomium.net">Le site de l'auteur</a></li>
#                 <li><a heref="http://ubuntu-fr.org">Ubuntu : le must</a></li>
#             </ul>
#             <p>[<a href="../">Retour à la racine des liens</a>]</p>
#         '''
#     index.exposed = True
#
# racine = HomePage()
# cherrypy.quickstart(racine, config="tutoriel.conf")


# ===================================================================================
class CompteurAcces(object):
    def index(self):
        # Exemple simplissime : incrémentation d'un compteur d'accés.
        # on commence par récupérer le total actuel du comptage :
        count = cherrypy.session.get('count', 0)
        # ... on l'incrémente :
        count += 1
        # ... on mémorise sa nouvelle valeur dans le dictionnaire de session :
        cherrypy.session['count'] = count
        # ... et on affiche le compte actuel :
        return '''
            Durant le présente session, vous avez déjà visité cette page {0} fois ! Votre vie
            est bien excitante !'''.format(count)
    index.exposed = True

cherrypy.quickstart(CompteurAcces(), config='tutoriel.conf')
