template= Import('template.py')

def formulaire():
    formulaire='''
<div class="container form">
    <h2 class="col-md-12">Formulaire</h2>
    <form id="form1" name="inscription " method="post" action="fonction.py/insert" enctype="multipart/form-data">
       <div class="col-md-12">
        <label class="col-md-6"> Type de compte:</label>
        <section class="col-md-6">
          <select name="select">
            <optgroup label= "Acteur">
                <option value="1">Agriculteur</option>
                <option value="2">Client</option>
            </optgroup>
          </select>
        </section>
      </div>
      <div class="col-md-12">
        <label class="col-md-6">Nom:</label>
        <section class="col-md-6">
          <input type="text" name="Nom" />
        </section>
      </div>
      <div class="col-md-12">
        <label class="col-md-6">Prénom:</label>
        <section class="col-md-6">
          <input type="text" name="Prénom"/>
        </section>
      </div>
      <div class="col-md-12">
        <label class="col-md-6">Adresse mail:</label>
        <section class="col-md-6">
          <input type="text" name="Email"/>
        </section>
      </div>
      <div class="col-md-12">
        <label class="col-md-6">Adresse:</label>
        <section class="col-md-6">
          <input type="text" name="Adresse"/>
        </section>
      </div>
      <div class="col-md-12">
        <label class="col-md-6">Mot de passe:</label>
        <section class="col-md-6">
          <input type="password" name="mdp"/>
        </section>
      </div>
      <div class="col-md-12">
        <label class="col-md-6">Confirmation mot de passe:</label>
        <section class="col-md-6">
          <input type="password" name="mdp"/>
        </section>
      </div>
      <div class="col-md-12">
          <button type="submit">Envoyer</button>       
      </div>
  </div>'''
    return formulaire


def NewAcount():
    result= template.head()
    result+= template.nav()
    result+= template.header()
    result+= formulaire()
    result+= template.footer()
    return result
