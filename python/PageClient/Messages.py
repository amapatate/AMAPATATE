template=Import('../template.py')

def Mes():
    Mes='''
    <div class="col-md-12">
        <p> Créer un protocole d'envoie automatique d'Email</p>
    </div>'''
    return Mes

def Messages():
    result= template.head()
    result+= template.navClient()
    result+= template.headerClient()
    result+= Mes()
    result+= template.footer()

    return result
