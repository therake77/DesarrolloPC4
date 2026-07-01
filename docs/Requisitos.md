1. Requerimientos: Reporte de Animales Perdidos y Alertas
Requerimientos Funcionales (RF)
RF 1.1: El sistema debe permitir a un dueño registrar una mascota como perdida ingresando nombre, especie, raza, foto y descripción.
RF 1.2: El sistema debe capturar las coordenadas geográficas del reporte (vía GPS del móvil o selección en mapa web).
RF 1.3: El sistema debe permitir a ciudadanos anónimos registrar un "avistamiento" subiendo una foto y la ubicación exacta.
RF 1.4: El sistema debe disparar notificaciones automáticas a los usuarios registrados en un radio configurable (ej. 1 km).
Requerimientos No Funcionales (RNF)
RNF 1.1 (Prioridad): Las alertas de mascotas perdidas deben procesarse y distribuirse en un tiempo menor a 5 segundos (Latencia).
RNF 1.2 (Seguridad): Los datos personales del dueño deben permanecer anónimos para los ciudadanos que reportan avistamientos.
2. Requerimientos: Buscador Multipropósito por Imagen
Requerimientos Funcionales (RF)
RF 2.1: El sistema debe ofrecer una interfaz única para cargar un archivo de imagen (JPEG/PNG) de una mascota.
RF 2.2: El sistema debe obligar al usuario a seleccionar una de tres intenciones: Adopción, Venta o Verificar Pérdida.
RF 2.3: Si la intención es "Adopción", el sistema debe devolver exclusivamente resultados del catálogo de protectoras/ONGs.
RF 2.4: Si la intención es "Venta", el sistema debe filtrar y mostrar solo criaderos comerciales legalmente certificados.
RF 2.5: Si la intención es "Verificar Pérdida", el sistema debe contrastar los metadatos con la base de datos de alertas activas.
Requerimientos No Funcionales (RNF)
RNF 2.1 (Abstracción): El backend debe aceptar un formato estándar de metadatos (JSON) para que el motor de búsqueda sea intercambiable en el futuro.
RNF 2.2 (Usabilidad): El tiempo de respuesta de la pantalla de resultados no debe superar los segundos tras subir la imagen.
3. Requerimientos: Red de Cuidadores de Mascotas
Requerimientos Funcionales (RF)
RF 3.1: El sistema debe permitir a los usuarios registrarse bajo tres roles: Cuidador Solidario, Profesional o Especializado.
RF 3.2: El sistema debe permitir a los cuidadores definir sus restricciones de servicio (especies aceptadas, tamaños, administración de medicamentos).
RF 3.3: El sistema debe permitir a los cuidadores activar o desactivar mediante un interruptor (toggle) la recepción de alertas de la funcionalidad 1.
RF 3.4: El sistema debe calcular y mostrar una calificación promedio en el perfil del cuidador basada en reseñas verificadas de dueños.
Requerimientos No Funcionales (RNF)
RNF 3.1 (Confiabilidad): El sistema debe requerir y validar un documento de identidad oficial antes de habilitar públicamente el perfil de un cuidador.
RNF 3.2 (Escalabilidad): El servicio de cuidadores debe ser independiente para soportar picos de alta demanda vacacional sin afectar el sistema de alertas