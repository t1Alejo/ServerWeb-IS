# ServerWeb-IS
Servidor web basico con verbos GET, POST, PATCH, DELETE creado con WSGI Python.

Actividad: Haz una breve explicación con tus palabras de la diferencia entre `GET`, `POST`, `PATCH` y `DELETE`, y por qué `POST` no es idempotente

El "GET" sirve para obtener los recursos del servidor y leerlos, estos no deberian poder modificar ningun dato/estado del servidor ya que su funcion principal es de servir de consulta por ende es seguro e idempotente porque siempre genera el mismo resultado
El "POST" es para crear y mandar datos al servidor. 
El "PATCH" actualiza o reemplaza unicamente partes de los atributos que le de lugar para cambiar de un recurso ya existente. Siempre tendria que tirar error cuando no encuentra el recurso solicitado
El "DELETE" vendria ser lo casi lo contrario de "POST", ya que en vez de crear, elimina datos del servidor. Al igual que "PATCH", tendria que tirar error en caso que el recurso a borrar no exista.

¿Por que "POST" no es idempotente?
Ser idempotente significaria que hacer una misma accion genera un mismo resultado pero en el caso de "POST" este no puede ser idempotente ya que genera siempre recursos nuevos aunque tengan todos los mismos datos, por ejemplo siempre se modificara el ID aunque borre los recursos con "DELETE" y trate de generar algo igual. 
