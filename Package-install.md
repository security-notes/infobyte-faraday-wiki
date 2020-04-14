
<!--
<!--Guía de migración a la nueva estructura de Faraday
-->
Migration Guide for the New Version of Faraday

After many months of work we have reorganized and changed the internal estructure of Faraday turning the whole project into giving it a Package organized structure. This is not something we came up with though, here is a blog with some more information of what this type of structure looks like: https://docs.python-guide.org/writing/structure/ (This is just ilustrative not exactly what we have)

<!--Cuando se mergeen !312 (o !318 o !324 para pink y black), la estructura del repo va a cambiar considerablemente, junto a muchos <!--ficheros de Python. La forma de instalación y de correr el server también van a ser diferentes.

<!--
<!--Haciendo correr (white|pink|black)/dev
<!--Se recomienda borrar el virtualenv y armar uno desde cero. Para evitar los problemas con gobject-introspection, lo mejor es crearlo <!--usando la opción --system-site-packages:
<!--
<!--$ virtualenv -p python3 --system-site-packages .venv
<!--$ source .venv/bin/activate


-->
##VirtualEnv
The Firts Step is to create the VirtualEnv.
If you already had a virtual env for faraday, we recomend deleting it and creating a new one.
And if hadn't: We can't stress enough just how important it is to use VirtualEnvs on Python projects.

### How to create a VirtualEnv
To install VirtualEnv do:
```
pip install virtualenv
```
And to create a new one:
```
virtualenv  --system-site-packages MYVIRTUALENV
```
And to activate it:
```
source MYVIRTUALENV/bin/activate
```

For more information on click here(https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/)


<!--Borrar todos los .pyc corriendo find . -name '*.pyc' -exec rm -f '{}' \;. Si no lo hacen, al correr el server va a tirar un error <!--diciendo que no puede importar CONST_LICENSE.
<!--
<!--Ahora no es necesario pip installear requirements_server.txt, ya que el setup.py lo hace solo. Para instalar el paquete tenemos dos <!--opciones:
-->
## Re-Installing faraday 
Delete all .pyc files:
```
find . -name '*.pyc' -exec rm -f '{}' \;
```
If you get an error saying: can't import CONST_LICENSE, it means you the pyc delition didn't work. Try again.

Now we are gonna install all the python dependencies on our new virtual env by doing:

```
python setup.py install
```

If you are on a OSX first install coreutils.


### Faraday Client

If you are using GTK.

now you need to do:
```
pip install -r requirements.txt -U
```

## New aliases

To run the server instead of doing python3 faraday-server.pyc  do:
```
faraday-server 
```
This will work even without being inside the faraday directory (as long as you don't deactivate your virtualenv).

To run the client instead of doing python3 faraday.pyc do:
```
faraday-client
```
To run the manage intead of doing python3 manage.pyc do:
```
faraday-manage
```



<!--
<!--Después hay que instalar los requirements del cliente y de desarrollo, que todavía no se instalan automáticamente:
<!--
<!--$ pip install -r requirements.txt
<!--$ pip install -r requirements_dev.txt
<!--Con esto ya debería estar todo instalado. Para correr el server, ahora hay que ejecutar el comando faraday-server, y se puede hacer <!--desde cualquier directorio! (siempre y cuando esté el virtualenv activado). También están el faraday-manage y faraday-client que <!--corren el manage.py y el cliente GTK respectivamente.
<!--
<!--Mergeando tu branch
<!--Todos estos cambios pueden hacer que si estás laburando en otro branch medio viejo, al momento de mergear produzca muchos <!--conflictos o directamente las nuevas funcionalidades dejen de funcionar.
<!--
<!--A continuación hay una pequeña guía de cosas a hacer para no frustrarse al momento de mergear.
<!--
<!--Qué cambios se hicieron al código
<!--Con esta migración se hicieron principalmente dos cambios: una mejora a la estructura de ficheros y directorios, y el cambio de <!--imports relativos a absolutos.
<!--
<!--El cambio de estructura fue simplemente mover los ficheros de lugar. Las cosas del cliente están un directorio client en el root <!--del proyecto (o en faraday/ una vez que se mergee lo de Eric). Por ejemplo, el código del plugin de sqlmap ahora va a estar ubicado <!--en client/plugins/repo/sqlmap/plugin.py.
<!--
<!--Con los cambios de Eric, casi todos los ficheros de python y JS van a cambiar de lugar y se van a mover al directorio faraday/. Por <!--ejemplo, código del API de vulns va a estar en faraday/server/api/modules/vulns.py. El controller del status report, en faraday/<!--server/www/scripts/statusReport/controllers/statusReport.js.
<!--
<!--Tanto en el branch de Eric como en !312 y sus derivados, hay que usar imports absolutos en el código de Python. Un código que <!--implemente un endpoint del API que antes importaba así:
<!--
<!--from server.api.base import ReadWriteAPITests
<!--tiene que pasar a ser:
<!--
<!--from faraday.server.api.base import ReadWriteAPITests
<!--Y algo que use la persistence server que hacía esto:
<!--
<!--from persistence.server.server import server
<!--ahora quedaría así
<!--
<!--from faraday.client.persistence.server import server
<!--Lo bueno es que se desarrollaron scripts que hacen estos cambios automáticamente, para evitar tener que perder el tiempo en estas <!--trivialidades.
<!--
<!--Resolviendo conflictos de imports
<!--Lo primero que hay que hacer para arreglar es traerse los últimos cambos del branch /dev correspondiente haciendo un git merge. <!--Esto puede traer varios conflictos con el código Python, pero la mayoría solamente afectan a los imports. Este es un ejemplo de un <!--conflicto que podría haber:
<!--
<!--<<<<<<< white/dev:start_server.py
<!--    import faraday.server.config
<!--    import faraday.server.utils.logger
<!--    from faraday.server.models import db, Workspace
<!--    from faraday.server.utils import daemonize
<!--    from faraday.server.web import app
<!--    from faraday.utils import dependencies
<!--    from faraday.utils.user_input import query_yes_no
<!--    from faraday.server.config import FARADAY_BASE
<!--    from faraday.utils.logs import setUpLogger
<!--=======
<!--    import server.config
<!--    import server.utils.logger
<!--    from server.models import db, Workspace
<!--    from server.utils import daemonize
<!--    from server.web import app
<!--    from server.config import otra_cosa
<!--    from utils import dependencies
<!--    from utils.user_input import query_yes_no
<!--    from faraday import FARADAY_BASE
<!--    from utils.logs import setUpLogger
<!-->>>>>>> mibranch:faraday-server.py
<!--En este caso, en nuestro branch tocamos los imports del start_server.py al mismo tiempo que lo hizo el cambio a imports absolutos. <!--Como todas las líneas en el código conflictivo son imports, hay una forma fácil de resolverlos (sólo es válida durante el cambio a <!--imports absolutos, no para siempre): dejar los cambios hechos en tu branch e ignorar los que están hechos en .../dev. Un script <!--después se va a encargar de arreglar los imports que estén mal.
<!--
<!--Los conflictos que no tengan que ver con imports hay que resolverlos a mano, pero no debería haber más que de costumbre.
<!--
<!--Una vez resueltos, commitear el merge sin probar que todo funcione bien (de nuevo, hacer esto solo para esta migración, no en el <!--resto de los casos). Después hay que hacer una pasada por los absolutize scripts como se describe a continuación.
<!--
<!--Cambiar estructura de nuevos ficheros
<!--Si modificaste un fichero que cambió de lugar, git automáticamente se va a dar cuenta y va a modificar el fichero renombrado sin <!--problemas. Sin embargo, si creaste un fichero nuevo que use la estructura vieja, este no se va a mover automáticamente. En muchos <!--casos esto hace que el fichero no se detecte. Por ejemplo, recientemente se creó un fplugin en bin/autoclose_vulns.py. Este path ya <!--no sirve, por lo que ese fplugin no funcionaría con los nuevos cambios.
<!--
<!--Para evitar esto, existe el script ./absolutize/fix_files_structure.sh. Este detecta ficheros que usen la vieja estructura y los <!--marca para mover en git. Para usarlo solamente hay que ejecutarlo desde la terminal, tirar un git status para ver que esté todo <!--bien, y en caso de haya cambios, commitear con git commit -m "[Absolutize] Run fix_files_structure.sh". Esto debería arreglar todos <!--los problemas relacionados a la estructura de directorios.
<!--
<!--Arreglar imports "triviales"
<!--Cuando hay código que hace un from ... import ... o import ... as ... es muy fácil convertir de imports relativos a absolutos. Solo <!--es necesario cambiar la línea del import para que le agregué el from faraday.....
<!--
<!--También hay un script de Bash para eso: ./absolutize/fix_trivial_imports.sh. Se recomienda leerlo si quieren aprender un poco de <!--bash.
<!--
<!--Para arreglar estos imports, hay que ejecutar el script (asegurarse antes que no haya código sin commitear). Después de unos <!--segundos va a terminar, y hay que correr un git add -p para ver que esté todo bien y agregar esos cambios. Después (si se cambió <!--algo), commitear con git commit -m "[Absolutize] Run fix_trivial_imports.sh" y pushear.
<!--
<!--Arreglar imports "no triviales"
<!--Si hay un código que por ejemplo hace un import server.config, entonces no solo hay que cambiar esa línea por import <!--faraday.server.config, sino todas las que usen el módulo importado. Ejemplo:
<!--
<!--# Check dependencies
<!--installed_deps, missing_deps, conflict_deps = dependencies.check_dependencies(
<!--    requirements_file=server.config.REQUIREMENTS_FILE)
<!--se tendría que convertir a:
<!--
<!--# Check dependencies
<!--installed_deps, missing_deps, conflict_deps = dependencies.check_dependencies(
<!--    requirements_file=faraday.server.config.REQUIREMENTS_FILE)
<!--Esto es un proceso bastante más complicado de resolver que con los imports triviales. Pueden adivinar qué herramienta se usa <!--arreglarlos? Sí! otro shell script! Bash es una herramienta súper poderosa para automatizar este tipo de cosas.
<!--
<!--Al igual que en los demás casos, el script se corre ejecutando ./absolutize/fix_nontrivial_imports.sh desde un worktree limpio. <!--Después hacer un git add -p, esta vez con más cautela que arreglando los imports triviales, ya que hay más posibilidades de que <!--algo salga mal.  git commit -m "[Absolutize] Run fix_nontrivial_imports", push y ya estaría todo.
<!--
<!--Después correr los tests como siempre, probar un poco el server y la web para ver que funcione todo bien.
<!--
<!--
