# Historias de Usuario

---

# ÉPICA 1: Reporte de Animales Perdidos y Alertas

---

## Identificación

| Campo | Valor |
|-------|-------|
| **ID** | HU-101 |
| **Épica / Módulo** | Reporte de Animales Perdidos y Alertas |
| **Sprint** | Sprint 1 |
| **Prioridad** | Alta |
| **Story Points** | 5 |
| **Estado** | Backlog |

---

## Enunciado

> **Como** dueño de una mascota,
> **quiero** registrar a mi mascota como perdida ingresando su nombre, especie, raza, foto y descripción,
> **para** poder alertar a la comunidad y aumentar las posibilidades de encontrarla.

---

## Criterios de Aceptación

**Escenario 1 — Registro exitoso de mascota perdida**
- **Dado** que soy un dueño autenticado en la plataforma,
- **Cuando** completo el formulario de reporte con nombre, especie, raza, foto y descripción, y lo envío,
- **Entonces** el sistema crea el reporte, lo marca como "activo" y confirma el registro al usuario.

**Escenario 2 — Campos obligatorios incompletos**
- **Dado** que estoy completando el formulario de reporte de mascota perdida,
- **Cuando** intento enviar el formulario sin ingresar un campo obligatorio (nombre, especie, raza o foto),
- **Entonces** el sistema muestra un mensaje de error indicando el campo faltante y no permite guardar el reporte.

**Escenario 3 — Foto en formato no soportado**
- **Dado** que estoy adjuntando una foto de la mascota,
- **Cuando** el archivo no es JPEG o PNG,
- **Entonces** el sistema rechaza el archivo y solicita un formato válido.

---

## Notas / Observaciones

- Relacionado con RF 1.1.
- Este reporte es la base de datos que utilizará RF 2.5 (Verificar Pérdida) para contrastar metadatos.
- Considerar límite de tamaño de archivo para la foto.

---

## Definition of Done (DoD)

- [ ] Código implementado y revisado (code review)
- [ ] Pruebas unitarias escritas y pasando
- [ ] Criterios de aceptación verificados
- [ ] Documentación actualizada (si aplica)
- [ ] Aprobado por el Product Owner

---
---

## Identificación

| Campo | Valor |
|-------|-------|
| **ID** | HU-102 |
| **Épica / Módulo** | Reporte de Animales Perdidos y Alertas |
| **Sprint** | Sprint 1 |
| **Prioridad** | Alta |
| **Story Points** | 5 |
| **Estado** | Backlog |

---

## Enunciado

> **Como** dueño de una mascota,
> **quiero** que el sistema capture la ubicación geográfica exacta de donde se perdió mi mascota (vía GPS del móvil o selección en un mapa web),
> **para** que los usuarios cercanos puedan ser notificados con precisión sobre la zona de búsqueda.

---

## Criterios de Aceptación

**Escenario 1 — Captura automática vía GPS (móvil)**
- **Dado** que estoy registrando un reporte desde la aplicación móvil y he otorgado permisos de ubicación,
- **Cuando** lleno el formulario de reporte,
- **Entonces** el sistema captura automáticamente mis coordenadas GPS actuales y las asocia al reporte.

**Escenario 2 — Selección manual en mapa web**
- **Dado** que estoy registrando un reporte desde la versión web,
- **Cuando** selecciono un punto en el mapa interactivo,
- **Entonces** el sistema guarda las coordenadas correspondientes a ese punto como ubicación del reporte.

**Escenario 3 — Permiso de ubicación denegado**
- **Dado** que estoy en la aplicación móvil,
- **Cuando** deniego el permiso de acceso al GPS,
- **Entonces** el sistema me solicita seleccionar manualmente la ubicación en un mapa.

---

## Notas / Observaciones

- Relacionado con RF 1.2.
- Dependencia con HU-101 (el reporte debe existir antes de asociar coordenadas, o crearse en el mismo flujo).
- Evaluar uso de un proveedor de mapas (Google Maps / OpenStreetMap).

---

## Definition of Done (DoD)

- [ ] Código implementado y revisado (code review)
- [ ] Pruebas unitarias escritas y pasando
- [ ] Criterios de aceptación verificados
- [ ] Documentación actualizada (si aplica)
- [ ] Aprobado por el Product Owner

---
---

## Identificación

| Campo | Valor |
|-------|-------|
| **ID** | HU-103 |
| **Épica / Módulo** | Reporte de Animales Perdidos y Alertas |
| **Sprint** | Sprint 1 |
| **Prioridad** | Alta |
| **Story Points** | 5 |
| **Estado** | Backlog |

---

## Enunciado

> **Como** ciudadano anónimo,
> **quiero** registrar un "avistamiento" de una mascota subiendo una foto y su ubicación exacta,
> **para** ayudar a que el dueño la encuentre sin necesidad de crear una cuenta.

---

## Criterios de Aceptación

**Escenario 1 — Registro de avistamiento sin autenticación**
- **Dado** que soy un usuario no autenticado,
- **Cuando** subo una foto y proporciono la ubicación exacta del avistamiento,
- **Entonces** el sistema registra el avistamiento y lo asocia a las coordenadas indicadas sin requerir datos personales.

**Escenario 2 — Avistamiento sin foto**
- **Dado** que estoy registrando un avistamiento,
- **Cuando** intento enviarlo sin adjuntar una foto,
- **Entonces** el sistema muestra un error indicando que la foto es obligatoria.

**Escenario 3 — Ubicación no proporcionada**
- **Dado** que estoy registrando un avistamiento,
- **Cuando** no otorgo ubicación ni la selecciono manualmente,
- **Entonces** el sistema no permite completar el registro hasta contar con una ubicación válida.

---

## Notas / Observaciones

- Relacionado con RF 1.3 y RNF 1.2 (anonimato de datos personales del dueño frente a quien reporta el avistamiento).
- No se debe solicitar registro/login al ciudadano que reporta.
- Verificar posibles medidas anti-spam/anti-abuso (captcha, límite de envíos).

---

## Definition of Done (DoD)

- [ ] Código implementado y revisado (code review)
- [ ] Pruebas unitarias escritas y pasando
- [ ] Criterios de aceptación verificados
- [ ] Documentación actualizada (si aplica)
- [ ] Aprobado por el Product Owner

---
---

## Identificación

| Campo | Valor |
|-------|-------|
| **ID** | HU-104 |
| **Épica / Módulo** | Reporte de Animales Perdidos y Alertas |
| **Sprint** | Sprint 2 |
| **Prioridad** | Alta |
| **Story Points** | 8 |
| **Estado** | Backlog |

---

## Enunciado

> **Como** usuario registrado en la plataforma,
> **quiero** recibir notificaciones automáticas cuando se reporte una mascota perdida dentro de un radio configurable (ej. 1 km) de mi ubicación,
> **para** poder colaborar rápidamente en la búsqueda.

---

## Criterios de Aceptación

**Escenario 1 — Notificación dentro del radio configurado**
- **Dado** que soy un usuario registrado con notificaciones activadas y un radio de 1 km configurado,
- **Cuando** se crea un nuevo reporte de mascota perdida a menos de 1 km de mi ubicación registrada,
- **Entonces** el sistema me envía una notificación automática en un tiempo menor a 5 segundos.

**Escenario 2 — Reporte fuera del radio configurado**
- **Dado** que soy un usuario registrado con un radio de 1 km configurado,
- **Cuando** se crea un reporte de mascota perdida a una distancia mayor al radio configurado,
- **Entonces** el sistema no me envía notificación alguna.

**Escenario 3 — Usuario modifica su radio de alerta**
- **Dado** que soy un usuario registrado,
- **Cuando** cambio el radio configurable de notificaciones,
- **Entonces** el sistema aplica el nuevo radio a partir de ese momento para futuras alertas.

---

## Notas / Observaciones

- Relacionado con RF 1.4 y RNF 1.1 (latencia menor a 5 segundos en procesamiento y distribución de alertas).
- Depende de HU-101 y HU-102 (el reporte y su ubicación deben existir previamente).
- Considerar arquitectura basada en eventos/colas para cumplir el requisito de latencia.
- Este flujo de suscripción a alertas se relaciona también con RF 3.3 (toggle de cuidadores para recibir alertas).

---

## Definition of Done (DoD)

- [ ] Código implementado y revisado (code review)
- [ ] Pruebas unitarias escritas y pasando
- [ ] Criterios de aceptación verificados
- [ ] Documentación actualizada (si aplica)
- [ ] Aprobado por el Product Owner

---
---

# ÉPICA 2: Buscador Multipropósito por Imagen

---

## Identificación

| Campo | Valor |
|-------|-------|
| **ID** | HU-201 |
| **Épica / Módulo** | Buscador Multipropósito por Imagen |
| **Sprint** | Sprint 2 |
| **Prioridad** | Alta |
| **Story Points** | 5 |
| **Estado** | Backlog |

---

## Enunciado

> **Como** usuario de la plataforma,
> **quiero** contar con una interfaz única para cargar una imagen (JPEG/PNG) de una mascota,
> **para** iniciar una búsqueda según mi necesidad (adopción, venta o verificación de pérdida).

---

## Criterios de Aceptación

**Escenario 1 — Carga exitosa de imagen**
- **Dado** que estoy en la pantalla del buscador por imagen,
- **Cuando** selecciono y subo un archivo en formato JPEG o PNG,
- **Entonces** el sistema acepta el archivo y lo muestra en una vista previa.

**Escenario 2 — Formato de archivo no soportado**
- **Dado** que estoy subiendo una imagen,
- **Cuando** el archivo no está en formato JPEG o PNG,
- **Entonces** el sistema rechaza la carga y muestra un mensaje indicando los formatos permitidos.

**Escenario 3 — Archivo demasiado pesado**
- **Dado** que estoy subiendo una imagen,
- **Cuando** el archivo excede el tamaño máximo permitido,
- **Entonces** el sistema muestra un mensaje de error y no procesa la imagen.

---

## Notas / Observaciones

- Relacionado con RF 2.1.
- Es el punto de entrada común para HU-202, HU-203, HU-204 y HU-205.

---

## Definition of Done (DoD)

- [ ] Código implementado y revisado (code review)
- [ ] Pruebas unitarias escritas y pasando
- [ ] Criterios de aceptación verificados
- [ ] Documentación actualizada (si aplica)
- [ ] Aprobado por el Product Owner

---
---

## Identificación

| Campo | Valor |
|-------|-------|
| **ID** | HU-202 |
| **Épica / Módulo** | Buscador Multipropósito por Imagen |
| **Sprint** | Sprint 2 |
| **Prioridad** | Alta |
| **Story Points** | 3 |
| **Estado** | Backlog |

---

## Enunciado

> **Como** usuario de la plataforma,
> **quiero** seleccionar obligatoriamente una intención de búsqueda (Adopción, Venta o Verificar Pérdida) antes de procesar mi imagen,
> **para** obtener resultados específicos y relevantes a mi necesidad.

---

## Criterios de Aceptación

**Escenario 1 — Selección de intención obligatoria**
- **Dado** que he cargado una imagen en el buscador,
- **Cuando** intento continuar sin seleccionar una intención,
- **Entonces** el sistema bloquea el avance y solicita seleccionar una de las tres opciones.

**Escenario 2 — Selección válida de intención**
- **Dado** que he cargado una imagen,
- **Cuando** selecciono una de las tres intenciones disponibles (Adopción, Venta o Verificar Pérdida),
- **Entonces** el sistema habilita el botón de búsqueda y enruta la solicitud al flujo correspondiente.

---

## Notas / Observaciones

- Relacionado con RF 2.2.
- Depende de HU-201.
- Esta selección determina cuál de las HU-203, HU-204 o HU-205 se ejecuta.

---

## Definition of Done (DoD)

- [ ] Código implementado y revisado (code review)
- [ ] Pruebas unitarias escritas y pasando
- [ ] Criterios de aceptación verificados
- [ ] Documentación actualizada (si aplica)
- [ ] Aprobado por el Product Owner

---
---

## Identificación

| Campo | Valor |
|-------|-------|
| **ID** | HU-203 |
| **Épica / Módulo** | Buscador Multipropósito por Imagen |
| **Sprint** | Sprint 3 |
| **Prioridad** | Media |
| **Story Points** | 5 |
| **Estado** | Backlog |

---

## Enunciado

> **Como** usuario interesado en adoptar una mascota,
> **quiero** que, al seleccionar la intención "Adopción", el sistema me muestre exclusivamente resultados del catálogo de protectoras/ONGs,
> **para** encontrar mascotas similares disponibles para adopción de fuentes confiables.

---

## Criterios de Aceptación

**Escenario 1 — Resultados exclusivos de protectoras/ONGs**
- **Dado** que subí una imagen y seleccioné la intención "Adopción",
- **Cuando** el sistema procesa la búsqueda,
- **Entonces** devuelve únicamente resultados provenientes del catálogo de protectoras/ONGs registradas.

**Escenario 2 — Sin coincidencias en el catálogo**
- **Dado** que seleccioné la intención "Adopción",
- **Cuando** no existen coincidencias en el catálogo de protectoras/ONGs,
- **Entonces** el sistema muestra un mensaje indicando que no se encontraron resultados.

---

## Notas / Observaciones

- Relacionado con RF 2.3.
- Depende de HU-201 y HU-202.
- Requiere integración con el catálogo/base de datos de protectoras y ONGs.

---

## Definition of Done (DoD)

- [ ] Código implementado y revisado (code review)
- [ ] Pruebas unitarias escritas y pasando
- [ ] Criterios de aceptación verificados
- [ ] Documentación actualizada (si aplica)
- [ ] Aprobado por el Product Owner

---
---

## Identificación

| Campo | Valor |
|-------|-------|
| **ID** | HU-204 |
| **Épica / Módulo** | Buscador Multipropósito por Imagen |
| **Sprint** | Sprint 3 |
| **Prioridad** | Media |
| **Story Points** | 5 |
| **Estado** | Backlog |

---

## Enunciado

> **Como** usuario interesado en comprar una mascota,
> **quiero** que, al seleccionar la intención "Venta", el sistema filtre y muestre solo criaderos comerciales legalmente certificados,
> **para** asegurarme de que la compra provenga de fuentes formales y responsables.

---

## Criterios de Aceptación

**Escenario 1 — Resultados exclusivos de criaderos certificados**
- **Dado** que subí una imagen y seleccioné la intención "Venta",
- **Cuando** el sistema procesa la búsqueda,
- **Entonces** devuelve únicamente resultados de criaderos comerciales con certificación legal vigente.

**Escenario 2 — Criadero con certificación vencida**
- **Dado** que existe un criadero comercial cuya certificación ha vencido,
- **Cuando** se ejecuta una búsqueda con intención "Venta",
- **Entonces** el sistema excluye a dicho criadero de los resultados.

---

## Notas / Observaciones

- Relacionado con RF 2.4.
- Depende de HU-201 y HU-202.
- Requiere un proceso previo de validación/certificación legal de criaderos (posible módulo administrativo adicional).

---

## Definition of Done (DoD)

- [ ] Código implementado y revisado (code review)
- [ ] Pruebas unitarias escritas y pasando
- [ ] Criterios de aceptación verificados
- [ ] Documentación actualizada (si aplica)
- [ ] Aprobado por el Product Owner

---
---

## Identificación

| Campo | Valor |
|-------|-------|
| **ID** | HU-205 |
| **Épica / Módulo** | Buscador Multipropósito por Imagen |
| **Sprint** | Sprint 3 |
| **Prioridad** | Alta |
| **Story Points** | 8 |
| **Estado** | Backlog |

---

## Enunciado

> **Como** usuario que encontró una mascota,
> **quiero** que, al seleccionar la intención "Verificar Pérdida", el sistema contraste los metadatos de mi imagen con la base de datos de alertas activas,
> **para** saber si la mascota corresponde a un reporte de pérdida vigente.

---

## Criterios de Aceptación

**Escenario 1 — Coincidencia con alerta activa**
- **Dado** que subí una imagen y seleccioné la intención "Verificar Pérdida",
- **Cuando** los metadatos de la imagen coinciden con un reporte activo en la base de datos de mascotas perdidas,
- **Entonces** el sistema muestra el/los reporte(s) coincidentes y una opción para contactar o notificar al dueño.

**Escenario 2 — Sin coincidencias**
- **Dado** que seleccioné la intención "Verificar Pérdida",
- **Cuando** no existen coincidencias con ningún reporte activo,
- **Entonces** el sistema informa que no se encontraron alertas activas relacionadas y sugiere registrar un avistamiento.

---

## Notas / Observaciones

- Relacionado con RF 2.5.
- Depende de HU-201, HU-202 y de la base de datos de alertas generada en HU-101/HU-102 (Épica 1).
- Requiere un formato estándar de metadatos para la interoperabilidad del motor de búsqueda (ver RNF 2.1).

---

## Definition of Done (DoD)

- [ ] Código implementado y revisado (code review)
- [ ] Pruebas unitarias escritas y pasando
- [ ] Criterios de aceptación verificados
- [ ] Documentación actualizada (si aplica)
- [ ] Aprobado por el Product Owner

---
---

## Identificación

| Campo | Valor |
|-------|-------|
| **ID** | HU-206 |
| **Épica / Módulo** | Buscador Multipropósito por Imagen |
| **Sprint** | Sprint 3 |
| **Prioridad** | Media |
| **Story Points** | 5 |
| **Estado** | Backlog |

---

## Enunciado

> **Como** equipo de desarrollo/arquitectura,
> **quiero** que el backend acepte un formato estándar de metadatos (JSON) para las búsquedas por imagen,
> **para** que el motor de búsqueda pueda ser reemplazado o mejorado en el futuro sin afectar el resto del sistema.

---

## Criterios de Aceptación

**Escenario 1 — Metadatos en formato JSON estándar**
- **Dado** que el motor de búsqueda procesa una imagen,
- **Cuando** genera los metadatos resultantes,
- **Entonces** los entrega en un formato JSON estandarizado y documentado (esquema definido).

**Escenario 2 — Motor de búsqueda intercambiable**
- **Dado** que existe un nuevo motor de búsqueda que cumple con el esquema JSON definido,
- **Cuando** se reemplaza el motor actual por el nuevo,
- **Entonces** el resto del sistema (HU-203, HU-204, HU-205) sigue funcionando sin cambios adicionales.

---

## Notas / Observaciones

- Relacionado con RNF 2.1 (Abstracción).
- Es una historia técnica/arquitectónica que soporta a toda la Épica 2.
- Recomendable definir el esquema JSON como contrato (ej. JSON Schema) antes de la implementación.

---

## Definition of Done (DoD)

- [ ] Código implementado y revisado (code review)
- [ ] Pruebas unitarias escritas y pasando
- [ ] Criterios de aceptación verificados
- [ ] Documentación actualizada (si aplica)
- [ ] Aprobado por el Product Owner

---
---

## Identificación

| Campo | Valor |
|-------|-------|
| **ID** | HU-207 |
| **Épica / Módulo** | Buscador Multipropósito por Imagen |
| **Sprint** | Sprint 3 |
| **Prioridad** | Media |
| **Story Points** | 3 |
| **Estado** | Backlog |

---

## Enunciado

> **Como** usuario del buscador por imagen,
> **quiero** que la pantalla de resultados responda en un tiempo razonable tras subir la imagen,
> **para** tener una experiencia de uso fluida y no abandonar la búsqueda.

---

## Criterios de Aceptación

**Escenario 1 — Tiempo de respuesta dentro del umbral**
- **Dado** que subí una imagen y seleccioné una intención de búsqueda,
- **Cuando** el sistema procesa la solicitud,
- **Entonces** la pantalla de resultados se muestra dentro del tiempo máximo definido por el equipo (a especificar en segundos, según RNF 2.2).

**Escenario 2 — Procesamiento demorado**
- **Dado** que el procesamiento de la imagen excede el tiempo máximo definido,
- **Cuando** esto ocurre,
- **Entonces** el sistema muestra un indicador de carga y/o un mensaje informando la demora, evitando que la interfaz parezca congelada.

---

## Notas / Observaciones

- Relacionado con RNF 2.2 (Usabilidad).
- **Pendiente de definición:** el requerimiento original no especifica el valor numérico del umbral de segundos; se recomienda validar con el Product Owner antes de la estimación final.

---

## Definition of Done (DoD)

- [ ] Código implementado y revisado (code review)
- [ ] Pruebas unitarias escritas y pasando
- [ ] Criterios de aceptación verificados
- [ ] Documentación actualizada (si aplica)
- [ ] Aprobado por el Product Owner

---
---

# ÉPICA 3: Red de Cuidadores de Mascotas

---

## Identificación

| Campo | Valor |
|-------|-------|
| **ID** | HU-301 |
| **Épica / Módulo** | Red de Cuidadores de Mascotas |
| **Sprint** | Sprint 4 |
| **Prioridad** | Alta |
| **Story Points** | 5 |
| **Estado** | Backlog |

---

## Enunciado

> **Como** usuario que desea ofrecer servicios de cuidado de mascotas,
> **quiero** registrarme bajo uno de tres roles (Cuidador Solidario, Profesional o Especializado),
> **para** que mi perfil refleje el tipo de servicio que ofrezco.

---

## Criterios de Aceptación

**Escenario 1 — Registro exitoso con rol seleccionado**
- **Dado** que estoy en el formulario de registro de cuidador,
- **Cuando** completo mis datos y selecciono uno de los tres roles disponibles,
- **Entonces** el sistema crea mi perfil de cuidador asociado al rol elegido.

**Escenario 2 — Registro sin seleccionar rol**
- **Dado** que estoy completando el registro de cuidador,
- **Cuando** intento enviar el formulario sin seleccionar un rol,
- **Entonces** el sistema muestra un error y no permite finalizar el registro.

---

## Notas / Observaciones

- Relacionado con RF 3.1.
- El perfil de cuidador queda inicialmente no habilitado públicamente hasta cumplir con RNF 3.1 (validación de identidad) — ver HU-304.

---

## Definition of Done (DoD)

- [ ] Código implementado y revisado (code review)
- [ ] Pruebas unitarias escritas y pasando
- [ ] Criterios de aceptación verificados
- [ ] Documentación actualizada (si aplica)
- [ ] Aprobado por el Product Owner

---
---

## Identificación

| Campo | Valor |
|-------|-------|
| **ID** | HU-302 |
| **Épica / Módulo** | Red de Cuidadores de Mascotas |
| **Sprint** | Sprint 4 |
| **Prioridad** | Media |
| **Story Points** | 5 |
| **Estado** | Backlog |

---

## Enunciado

> **Como** cuidador registrado,
> **quiero** definir mis restricciones de servicio (especies aceptadas, tamaños de mascota, administración de medicamentos),
> **para** que los dueños encuentren cuidadores compatibles con las necesidades específicas de su mascota.

---

## Criterios de Aceptación

**Escenario 1 — Configuración de restricciones**
- **Dado** que soy un cuidador con perfil creado,
- **Cuando** selecciono las especies que acepto, los tamaños de mascota permitidos y si administro medicamentos,
- **Entonces** el sistema guarda estas preferencias en mi perfil.

**Escenario 2 — Actualización de restricciones**
- **Dado** que ya tengo restricciones configuradas,
- **Cuando** modifico alguna de ellas,
- **Entonces** el sistema actualiza mi perfil con los nuevos valores de forma inmediata.

---

## Notas / Observaciones

- Relacionado con RF 3.2.
- Depende de HU-301.
- Estas restricciones deberían usarse como filtros al momento de que un dueño busque cuidadores.

---

## Definition of Done (DoD)

- [ ] Código implementado y revisado (code review)
- [ ] Pruebas unitarias escritas y pasando
- [ ] Criterios de aceptación verificados
- [ ] Documentación actualizada (si aplica)
- [ ] Aprobado por el Product Owner

---
---

## Identificación

| Campo | Valor |
|-------|-------|
| **ID** | HU-303 |
| **Épica / Módulo** | Red de Cuidadores de Mascotas |
| **Sprint** | Sprint 4 |
| **Prioridad** | Media |
| **Story Points** | 3 |
| **Estado** | Backlog |

---

## Enunciado

> **Como** cuidador registrado,
> **quiero** activar o desactivar mediante un interruptor (toggle) la recepción de alertas de mascotas perdidas,
> **para** decidir si deseo participar activamente en la búsqueda de mascotas en mi zona.

---

## Criterios de Aceptación

**Escenario 1 — Activar recepción de alertas**
- **Dado** que soy un cuidador con el toggle de alertas desactivado,
- **Cuando** activo el interruptor,
- **Entonces** el sistema me suscribe a las notificaciones de mascotas perdidas dentro de mi radio configurado.

**Escenario 2 — Desactivar recepción de alertas**
- **Dado** que soy un cuidador con el toggle de alertas activado,
- **Cuando** desactivo el interruptor,
- **Entonces** el sistema deja de enviarme notificaciones de mascotas perdidas de inmediato.

---

## Notas / Observaciones

- Relacionado con RF 3.3.
- Depende de HU-301 y se integra con HU-104 (motor de notificaciones de la Épica 1).

---

## Definition of Done (DoD)

- [ ] Código implementado y revisado (code review)
- [ ] Pruebas unitarias escritas y pasando
- [ ] Criterios de aceptación verificados
- [ ] Documentación actualizada (si aplica)
- [ ] Aprobado por el Product Owner

---
---

## Identificación

| Campo | Valor |
|-------|-------|
| **ID** | HU-304 |
| **Épica / Módulo** | Red de Cuidadores de Mascotas |
| **Sprint** | Sprint 5 |
| **Prioridad** | Alta |
| **Story Points** | 8 |
| **Estado** | Backlog |

---

## Enunciado

> **Como** dueño de una mascota que busca un cuidador,
> **quiero** ver una calificación promedio en el perfil de cada cuidador basada en reseñas verificadas,
> **para** poder elegir con confianza a quién dejar el cuidado de mi mascota.

---

## Criterios de Aceptación

**Escenario 1 — Cálculo de calificación promedio**
- **Dado** que un cuidador tiene una o más reseñas verificadas,
- **Cuando** se visualiza su perfil,
- **Entonces** el sistema muestra la calificación promedio calculada a partir de dichas reseñas.

**Escenario 2 — Cuidador sin reseñas**
- **Dado** que un cuidador aún no tiene reseñas verificadas,
- **Cuando** se visualiza su perfil,
- **Entonces** el sistema muestra un estado de "sin calificaciones aún" en lugar de un promedio.

**Escenario 3 — Reseña no verificada**
- **Dado** que existe una reseña que no ha sido verificada como proveniente de un servicio real,
- **Cuando** se calcula el promedio del cuidador,
- **Entonces** dicha reseña no verificada se excluye del cálculo.

---

## Notas / Observaciones

- Relacionado con RF 3.4.
- Depende de HU-301.
- Se recomienda definir el criterio de "reseña verificada" (ej. asociada a un servicio confirmado en la plataforma).

---

## Definition of Done (DoD)

- [ ] Código implementado y revisado (code review)
- [ ] Pruebas unitarias escritas y pasando
- [ ] Criterios de aceptación verificados
- [ ] Documentación actualizada (si aplica)
- [ ] Aprobado por el Product Owner

---
---

## Identificación

| Campo | Valor |
|-------|-------|
| **ID** | HU-305 |
| **Épica / Módulo** | Red de Cuidadores de Mascotas |
| **Sprint** | Sprint 5 |
| **Prioridad** | Alta |
| **Story Points** | 8 |
| **Estado** | Backlog |

---

## Enunciado

> **Como** administrador de la plataforma,
> **quiero** requerir y validar un documento de identidad oficial antes de habilitar públicamente el perfil de un cuidador,
> **para** garantizar la confiabilidad y seguridad de la red de cuidadores.

---

## Criterios de Aceptación

**Escenario 1 — Perfil no habilitado sin validación**
- **Dado** que un cuidador se registró pero no ha subido su documento de identidad,
- **Cuando** se intenta visualizar su perfil públicamente,
- **Entonces** el sistema no lo muestra en los resultados de búsqueda públicos.

**Escenario 2 — Documento validado exitosamente**
- **Dado** que un cuidador subió su documento de identidad oficial,
- **Cuando** el documento es validado (manual o automáticamente) y aprobado,
- **Entonces** el sistema habilita públicamente su perfil.

**Escenario 3 — Documento rechazado**
- **Dado** que un cuidador subió un documento de identidad,
- **Cuando** el documento es rechazado por no ser válido o legible,
- **Entonces** el sistema notifica al cuidador y solicita subir un nuevo documento, manteniendo el perfil no habilitado.

---

## Notas / Observaciones

- Relacionado con RNF 3.1 (Confiabilidad).
- Depende de HU-301.
- Definir si la validación del documento será manual (equipo interno) o mediante un servicio externo de verificación de identidad.

---

## Definition of Done (DoD)

- [ ] Código implementado y revisado (code review)
- [ ] Pruebas unitarias escritas y pasando
- [ ] Criterios de aceptación verificados
- [ ] Documentación actualizada (si aplica)
- [ ] Aprobado por el Product Owner

---
---

## Identificación

| Campo | Valor |
|-------|-------|
| **ID** | HU-306 |
| **Épica / Módulo** | Red de Cuidadores de Mascotas |
| **Sprint** | Sprint 5 |
| **Prioridad** | Media |
| **Story Points** | 8 |
| **Estado** | Backlog |

---

## Enunciado

> **Como** equipo de arquitectura/infraestructura,
> **quiero** que el servicio de cuidadores sea independiente y escalable,
> **para** soportar picos de alta demanda en temporada vacacional sin afectar el sistema de alertas de mascotas perdidas.

---

## Criterios de Aceptación

**Escenario 1 — Aislamiento de servicios**
- **Dado** que el servicio de cuidadores experimenta un pico de tráfico (temporada vacacional),
- **Cuando** dicho pico ocurre,
- **Entonces** el sistema de alertas de mascotas perdidas (Épica 1) continúa funcionando con su nivel de latencia y disponibilidad normal (RNF 1.1).

**Escenario 2 — Escalado ante demanda**
- **Dado** que el servicio de cuidadores está desplegado de forma independiente,
- **Cuando** la demanda de solicitudes aumenta significativamente,
- **Entonces** el servicio escala sus recursos de manera automática u horizontal sin degradar el tiempo de respuesta.

---

## Notas / Observaciones

- Relacionado con RNF 3.2 (Escalabilidad).
- Historia técnica/arquitectónica; se recomienda evaluar un despliegue en microservicio separado con su propia base de datos o réplica.
- Coordinar con el equipo de DevOps/Infraestructura para definir estrategia de autoescalado.

---

## Definition of Done (DoD)

- [ ] Código implementado y revisado (code review)
- [ ] Pruebas unitarias escritas y pasando
- [ ] Criterios de aceptación verificados
- [ ] Documentación actualizada (si aplica)
- [ ] Aprobado por el Product Owner
