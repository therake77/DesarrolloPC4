# Software Requirements Specification (SRS)
**Proyecto:** Plataforma de Reporte, Búsqueda y Cuidado de Mascotas (PetFinder)
**Fecha:** 01/07/2026
**Autor:** Jarem Villalobos Palomino

---

## 1. Introducción

### 1.1 Propósito
Este documento describe los requisitos funcionales y no funcionales del sistema (auto-denominado) **PetFinder**, como plataforma web destinada a dueños de mascotas, ciudadanos en general, protectoras/ONGs, criaderos comerciales certificados y personas que ofrecen servicios de cuidado de mascotas. El propósito del sistema es facilitar el reporte y búsqueda de mascotas perdidas, la identificación de mascotas mediante imágenes con distintos propósitos (adopción, venta o verificación de pérdida), y la conexión entre dueños y una red confiable de cuidadores.

### 1.2 Alcance
El sistema permitirá:
- Registrar mascotas perdidas y avistamientos, geolocalizarlos y notificar automáticamente a usuarios cercanos.
- Buscar mascotas a partir de una imagen, según tres intenciones distintas: adopción, venta o verificación de pérdida.
- Registrar, filtrar y calificar cuidadores de mascotas organizados en distintos roles de servicio.

**No incluye** (fuera de alcance de esta versión):
- Procesamiento de pagos.
- Chat en tiempo real entre usuarios.
- Gestión veterinaria o historial clínico de las mascotas.
- Certificación legal de criaderos (se asume que dicha certificación es otorgada por un ente externo y solo es validada/consumida por el sistema).

### 1.3 Definiciones y Acrónimos

| Término | Definición |
|---------|------------|
| **RF** | Requisito Funcional |
| **RNF** | Requisito No Funcional |
| **Dueño** | Usuario registrado propietario de una mascota |
| **Avistamiento** | Registro realizado por un ciudadano indicando que vio a una posible mascota perdida |
| **Cuidador** | Usuario que ofrece servicios de cuidado de mascotas (Solidario, Profesional o Especializado) |
| **ONG/Protectora** | Organización sin fines de lucro dedicada al rescate y adopción de animales |
| **Criadero comercial certificado** | Entidad legalmente certificada dedicada a la venta de mascotas |
| **Radio configurable** | Distancia geográfica (ej. 1 km) definida por el usuario para recibir alertas |
| **Metadatos** | Información estructurada (JSON) extraída de una imagen para su procesamiento por el motor de búsqueda |
| **Toggle** | Interruptor de activación/desactivación de una opción dentro del sistema |
| **Reseña verificada** | Calificación asociada a un servicio de cuidado confirmado dentro de la plataforma |

---

## 2. Descripción General

### 2.1 Perspectiva del producto
PetFinder es un sistema nuevo, compuesto por tres módulos funcionales interrelacionados: (1) Reporte de Animales Perdidos y Alertas, (2) Buscador Multipropósito por Imagen, y (3) Red de Cuidadores de Mascotas. Los tres módulos comparten una base de datos común de mascotas y usuarios, pero deben poder escalar y operar de forma independiente, especialmente el módulo de cuidadores, para no afectar el rendimiento del módulo de alertas en momentos de alta demanda. El sistema se ofrecerá como aplicación web y aplicación móvil.

### 2.2 Funciones principales
- Registro de reportes de mascotas perdidas con foto, descripción y ubicación geográfica.
- Registro anónimo de avistamientos por parte de ciudadanos.
- Envío de notificaciones automáticas geolocalizadas ante nuevos reportes.
- Búsqueda de mascotas por imagen, con resultados diferenciados según la intención del usuario (adopción, venta o verificación de pérdida).
- Registro y gestión de perfiles de cuidadores con roles, restricciones de servicio y calificaciones.
- Validación de identidad de cuidadores antes de su publicación pública.

### 2.3 Usuarios y características

| Tipo de usuario | Descripción |
|----------------|-------------|
| **Dueño de mascota** | Usuario registrado que reporta mascotas perdidas, busca cuidadores y puede calificar sus servicios. |
| **Ciudadano anónimo** | Usuario no registrado que reporta avistamientos de mascotas sin necesidad de crear una cuenta. |
| **Usuario registrado (comunidad)** | Usuario que recibe notificaciones de mascotas perdidas dentro de un radio configurable. |
| **Cuidador Solidario** | Usuario que ofrece cuidado de mascotas de forma no profesional/voluntaria. |
| **Cuidador Profesional** | Usuario que ofrece servicios de cuidado de forma remunerada y con mayor formalidad. |
| **Cuidador Especializado** | Usuario capacitado para atender necesidades específicas (ej. administración de medicamentos, mascotas de tamaño o tipo particular). |
| **Protectora / ONG** | Entidad que gestiona un catálogo de mascotas disponibles para adopción. |
| **Criadero comercial certificado** | Entidad legalmente certificada que ofrece mascotas en venta. |
| **Administrador de la plataforma** | Usuario interno encargado de validar documentos de identidad de cuidadores y certificaciones de criaderos. |

### 2.4 Restricciones generales
- El sistema debe funcionar tanto en aplicación web (con mapa interactivo) como en aplicación móvil (con acceso a GPS nativo).
- Las imágenes cargadas deben limitarse a los formatos JPEG y PNG.
- El motor de búsqueda por imagen debe comunicarse mediante un contrato de metadatos en formato JSON, de manera que sea intercambiable en el futuro.
- El módulo de cuidadores debe poder desplegarse/escalar de forma independiente al módulo de alertas.
- Los datos personales del dueño deben mantenerse anónimos frente a los ciudadanos que reportan avistamientos.
- Los perfiles de cuidadores no pueden hacerse públicos sin validación previa de un documento de identidad oficial.

---

## 3. Requisitos Específicos

### 3.1 Requisitos Funcionales

**RF-01: Registro de mascota perdida**
- **Descripción:** El sistema debe permitir a un dueño registrar una mascota como perdida ingresando nombre, especie, raza, foto y descripción.
- **Prioridad:** Alta

**RF-02: Captura de ubicación del reporte**
- **Descripción:** El sistema debe capturar las coordenadas geográficas del reporte, ya sea vía GPS del dispositivo móvil o mediante selección manual en un mapa web.
- **Prioridad:** Alta

**RF-03: Registro de avistamiento anónimo**
- **Descripción:** El sistema debe permitir a ciudadanos anónimos (sin necesidad de autenticarse) registrar un "avistamiento" subiendo una foto y la ubicación exacta donde fue observada la mascota.
- **Prioridad:** Alta

**RF-04: Notificaciones automáticas por proximidad**
- **Descripción:** El sistema debe disparar notificaciones automáticas a los usuarios registrados que se encuentren dentro de un radio configurable (ej. 1 km) del reporte de mascota perdida.
- **Prioridad:** Alta

**RF-05: Carga de imagen para búsqueda**
- **Descripción:** El sistema debe ofrecer una interfaz única donde el usuario pueda cargar un archivo de imagen (JPEG/PNG) de una mascota para iniciar una búsqueda.
- **Prioridad:** Alta

**RF-06: Selección obligatoria de intención de búsqueda**
- **Descripción:** El sistema debe obligar al usuario a seleccionar una de tres intenciones antes de procesar la búsqueda: Adopción, Venta o Verificar Pérdida.
- **Prioridad:** Alta

**RF-07: Resultados exclusivos de protectoras/ONGs (Adopción)**
- **Descripción:** Si la intención seleccionada es "Adopción", el sistema debe devolver exclusivamente resultados provenientes del catálogo de protectoras/ONGs.
- **Prioridad:** Media

**RF-08: Resultados exclusivos de criaderos certificados (Venta)**
- **Descripción:** Si la intención seleccionada es "Venta", el sistema debe filtrar y mostrar solo criaderos comerciales legalmente certificados.
- **Prioridad:** Media

**RF-09: Contraste con alertas activas (Verificar Pérdida)**
- **Descripción:** Si la intención seleccionada es "Verificar Pérdida", el sistema debe contrastar los metadatos de la imagen con la base de datos de alertas activas de mascotas perdidas.
- **Prioridad:** Alta

**RF-10: Registro de cuidadores por rol**
- **Descripción:** El sistema debe permitir a los usuarios registrarse como cuidadores bajo uno de tres roles: Cuidador Solidario, Profesional o Especializado.
- **Prioridad:** Alta

**RF-11: Restricciones de servicio del cuidador**
- **Descripción:** El sistema debe permitir a los cuidadores definir sus restricciones de servicio, tales como especies aceptadas, tamaños de mascota y disposición para administrar medicamentos.
- **Prioridad:** Media

**RF-12: Suscripción a alertas del cuidador**
- **Descripción:** El sistema debe permitir a los cuidadores activar o desactivar, mediante un interruptor (toggle), la recepción de alertas de mascotas perdidas (funcionalidad de RF-04).
- **Prioridad:** Media

**RF-13: Calificación promedio del cuidador**
- **Descripción:** El sistema debe calcular y mostrar en el perfil del cuidador una calificación promedio basada en reseñas verificadas realizadas por dueños.
- **Prioridad:** Media

---

### 3.2 Requisitos No Funcionales

**RNF-01 — Rendimiento (Latencia de alertas):** Las alertas de mascotas perdidas deben procesarse y distribuirse a los usuarios dentro de un radio configurado en un tiempo menor a 5 segundos desde su creación.

**RNF-02 — Seguridad (Anonimato del dueño):** Los datos personales del dueño de una mascota deben permanecer anónimos frente a los ciudadanos que registran avistamientos; solo se debe exponer la información estrictamente necesaria para la coordinación del reencuentro.

**RNF-03 — Arquitectura / Abstracción (Motor de búsqueda intercambiable):** El backend del buscador por imagen debe aceptar y producir un formato estándar de metadatos en JSON, de modo que el motor de búsqueda (algoritmo o proveedor de reconocimiento de imágenes) pueda ser reemplazado en el futuro sin afectar al resto del sistema.

**RNF-04 — Usabilidad (Tiempo de respuesta del buscador):** El tiempo de respuesta entre la carga de la imagen y la visualización de la pantalla de resultados no debe superar el umbral máximo definido por el equipo del producto *(valor pendiente de confirmación con el Product Owner; se recomienda no exceder pocos segundos para no afectar la experiencia de usuario)*.

**RNF-05 — Confiabilidad (Validación de identidad de cuidadores):** El sistema debe requerir y validar un documento de identidad oficial de cada cuidador antes de habilitar públicamente su perfil en la plataforma.

**RNF-06 — Escalabilidad (Independencia del servicio de cuidadores):** El servicio de cuidadores debe estar desacoplado del resto del sistema y ser capaz de escalar de forma independiente para soportar picos de alta demanda (ej. temporada vacacional) sin afectar el rendimiento ni la latencia del sistema de alertas de mascotas perdidas (RNF-01).

**RNF-07 — Disponibilidad:** El sistema debe estar disponible de forma continua (24/7), dado que los reportes de mascotas perdidas y avistamientos pueden ocurrir en cualquier momento del día.

**RNF-08 — Portabilidad:** El sistema debe ser accesible desde una aplicación web (compatible con los navegadores más recientes) y desde aplicaciones móviles (Android/iOS), garantizando consistencia funcional entre ambas plataformas.

---

### 3.3 Requisitos de Interfaz

- **Interfaz de usuario:**
  - **Web:** portal para dueños, protectoras/ONGs, criaderos y administradores, con mapa interactivo para selección manual de ubicación.
  - **Móvil (Android/iOS):** aplicación con acceso a GPS nativo, cámara para captura/carga de fotos, y notificaciones push para alertas geolocalizadas.

- **Interfaz de hardware:**
  - Acceso al GPS del dispositivo móvil del usuario para la captura automática de coordenadas.
  - Acceso a la cámara del dispositivo para la captura de fotografías de mascotas y avistamientos.

- **Interfaz de software / APIs externas:**
  - **API de mapas** (ej. Google Maps / OpenStreetMap) para geolocalización y selección de puntos en el mapa web.
  - **API/servicio de reconocimiento de imágenes** (motor de búsqueda por imagen), consumido mediante un contrato JSON estandarizado (ver RNF-03), para las funcionalidades de adopción, venta y verificación de pérdida.
  - **Servicio de notificaciones push / mensajería** para el envío de alertas geolocalizadas en tiempo casi real.
  - **Servicio de verificación de identidad** (interno o de terceros) para la validación de documentos de identidad de los cuidadores.
  - **Interfaz de integración con catálogos externos** de protectoras/ONGs y de criaderos comerciales certificados.

---

## 4. Modelos y Diagramas

*(Incluir aquí, cuando corresponda: diagrama de casos de uso general con los actores Dueño, Ciudadano anónimo, Usuario registrado, Cuidador, Protectora/ONG, Criadero certificado y Administrador; diagrama de flujo de datos del proceso de alerta geolocalizada (RF-01 a RF-04); diagrama de flujo del buscador por imagen mostrando la bifurcación según intención (RF-05 a RF-09); y diagrama entidad-relación preliminar cubriendo las entidades Mascota, Reporte, Avistamiento, Usuario, Cuidador, Reseña y Certificación.)*

---

## 5. Apéndices

**Supuestos:**
- Se asume que las protectoras/ONGs y los criaderos comerciales certificados ya cuentan con un catálogo o registro previo integrable al sistema.
- Se asume que la certificación legal de los criaderos es otorgada y mantenida por una entidad externa, y que el sistema solo consume/valida dicho estado.
- Se asume que el usuario final cuenta con conexión a internet estable para el envío/recepción de alertas en tiempo casi real.

**Pendientes a definir con el Product Owner:**
- Valor numérico exacto del umbral de tiempo de respuesta indicado en RNF-04.
- Mecanismo específico de validación de documentos de identidad (manual vs. automatizado/tercerizado) referido en RNF-05.
- Criterio formal de "reseña verificada" utilizado para el cálculo de la calificación promedio (RF-13).

**Referencias:**
- Historias de Usuario asociadas: HU-101 a HU-104 (Épica 1 — Reporte de Animales Perdidos y Alertas), HU-201 a HU-207 (Épica 2 — Buscador Multipropósito por Imagen), HU-301 a HU-306 (Épica 3 — Red de Cuidadores de Mascotas).
