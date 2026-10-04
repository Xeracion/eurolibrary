# Análisis del copy y propuesta de rediseño de eurolibrary.eu

Fecha del análisis: 4 de octubre de 2026. Fuente: https://eurolibrary.eu/ (home).

## Qué hay hoy

Estructura de la home, que la propuesta mantiene tal cual:

1. Navegación: Home, About, Mobilities (5 capítulos), Human Library, Get Involved.
2. Hero: "An erasmus+ adventure", "5 countries, 5 topics, 5 ways to move", botón de registro.
3. Concepto: "A journey beyond borders".
4. Destinos: cinco mobilities con fechas, descripción y estado.
5. Llamada a la comunidad: "Listen, share, inspire".
6. Leitmotiv, contadores (5, +120, +150) y tres puntos.
7. Pie con el aviso legal de la UE.

## Diagnóstico del copy

| Problema | Dónde | Efecto |
|---|---|---|
| Erratas y gramática | "who has a lot to say" (young people), "more that 3 cities", "most tacking challenges", "Discovering Europe", "an erasmus+" | Resta credibilidad ante una institución financiadora y ante jóvenes |
| Todos los destinos dicen "Applications are closed" | Los cinco bloques | La web parece muerta; no explica qué hacer ahora |
| El tema de cada capítulo queda escondido dentro de la frase | Destinos | Cuesta escanear qué trata cada viaje |
| Verbos de instrucción mezclados ("Join", "Share", "Hop on") sin ritmo común | Destinos | Tono desigual |
| El botón "Register your interest" aparece sin explicar qué se recibe ni cuándo | Hero | Fricción |
| Titulares en mayúsculas sueltas ("AN erasmus+ adventure") | Hero | Aspecto de error |
| Los contadores no dicen qué son los "+" | Leitmotiv | Cifras sin contexto |
| Se pierde el vínculo entre medio de transporte y tema | Destinos | Es el gancho más fuerte del proyecto y no se destaca |

## Cambios de copy

| Antes | Después | Motivo |
|---|---|---|
| AN erasmus+ adventure | An Erasmus+ adventure | Corrige mayúsculas |
| One unforgettable experience | One journey that changes how you see Europe. | Promete un cambio concreto en vez de un adjetivo |
| Press the button below to register your interest. You will receive all the information and news regarding the 5 chapters of #eurolibrary | Register your interest and we will send you news and details on all five chapters of #eurolibrary. | Más corto y en voz activa |
| (sin microcopy) | Free to join the community. No spam, only stories. | Reduce fricción en el CTA |
| Hop on a train that crisscross Balkanic landscapes. We will gather young entrepreneurs and changemakers who are building futures with their own hands. | Ride trains across the Balkans with young entrepreneurs and changemakers who are building their futures with their own hands. | Corrige "crisscross" y "Balkanic" |
| Share your experience and knowledge about mental health while walking The English way of the Camino de Santiago. | Walk the English Way of the Camino de Santiago and share what you know about mental health, one step at a time. | Primero la acción, después el tema |
| Join an exciting journey in the Netherlands. Cycle across Friesland and motivate young people through your personal story associated to healthy lifestyle. | Cycle across Friesland and inspire young people with your personal story about living a healthy lifestyle. | Elimina el relleno "exciting journey" |
| Join the ultimate island hopping experience. Visit 3 Greek Cycladic islands, share and listen personal stories about migration. | Island hop across three Cycladic islands, sharing and listening to personal stories about migration. | Corrige "listen personal stories" |
| A roadtrip with RVs at South Portugal. Travel in more that 3 cities, organise events, share and listen to stories about sustainability and eco-living. | Road trip in RVs through southern Portugal: visit more than three cities, organise events and swap stories about sustainability and eco living. | Corrige preposiciones y "that" |
| APPLICATIONS ARE CLOSED | Applications closed + enlace "Read the story" | Cada tarjeta ofrece una salida útil |
| Discovering Europe: the wild way | Discover Europe the wild way | Imperativo, como el resto |
| The most international group: ...who has a lot to say about the most tacking European challenges | ...who have a lot to say about the most pressing challenges Europe faces today | Concordancia y errata |
| Cool content: ...catchy clips available on our socials. You will have the chance also to listen the stories... | ...catchy clips on our socials, and you can hear our participants' stories in our podcast. | Corrige "listen the" y orden |
| This is not just a project. It's an adventure. A celebration of... | This is not just a project. It is an adventure, a celebration of empathy, sustainability and European identity. | Una sola idea en una frase |

Lo que se conserva a propósito: "a story can change a life, a journey can unite a continent", "living library made not of books, but of people" y el triplete "Real voices. Real experiences. Real connections.". Son lo mejor del texto.

Añadidos nuevos, todos derivados de información que ya está en la web:

* Etiqueta de tema en cada capítulo (Entrepreneurship, Mental health, Healthy lifestyle, Migration, Sustainability).
* Medio de transporte en cada capítulo (tren, a pie, bici, barco, autocaravana).
* Una tira de cinco capítulos en el hero para ver el proyecto de un vistazo.

Pendiente de confirmar con el equipo: que los viajes de 2025 ya han pasado y todas las tarjetas dicen "closed". Conviene decidir si se mantiene el registro como lista de espera para una nueva edición y decirlo explícitamente.

## Rediseño

Archivo: `index.html` (autocontenido, sin dependencias salvo Google Fonts).

**Sistema visual**

* Lienzo crema `#faf2ec`, tarjetas blancas que flotan encima, tinta cálida `#1b1917`.
* Tipografía de titulares: DM Serif Display como sustituta de Nineties, a 80, 48 y 28 px con interlineado 1.08. Cuerpo en Inter con las características cv02, cv03, cv04, cv06 y cv11.
* Acento naranja quemado `#c4521a`, tomado del Instagram de Eurolibrary, para la única acción principal. Toques de azul agua y melocotón solo como lavado de fondo en el hero.
* Radios de 12 px en tarjetas y etiquetas, 16 px en botones. Sombras de un píxel más una caída suave.
* Bordes y etiquetas en lavanda `#9894a8`.

**Decisión a revisar**: pampam.city reserva un azul periwinkle para el CTA. Aquí lo sustituyo por el naranja de la marca porque el azul no aparece en la identidad de Eurolibrary. Si prefieres el azul exacto, es cambiar `--orange`.

**Estructura mantenida**: navegación con desplegable de Mobilities, hero, concepto, cinco destinos, comunidad, leitmotiv con contadores animados, pie con aviso de la UE. Los enlaces apuntan a las páginas reales y el botón de registro al mismo formulario de Typeform.

**Imágenes**: son las de la web actual (`assets/`). El logo original es blanco, así que hay una versión en tinta (`logo-ink.svg`) para fondo crema. El pie usa la insignia de la UE sobre un bloque oscuro para respetar su versión blanca.

## Segunda ronda: todo el sitio, proyecto cerrado, lector evaluador

Cambia el enfoque. Los cinco viajes de 2025 ya han terminado, así que la web deja de captar participantes y pasa a ser el registro del proyecto. El lector principal es quien evalúa el proyecto para la Comisión Europea, con un tono joven pero claro y verificable.

**Reglas de copy que se han aplicado**

* Pasado para lo que ocurrió, presente solo para descripciones de lugares y de método.
* Sin llamadas a postular. "Apply now" desaparece y cada capítulo muestra "Completed".
* Cada capítulo dice lo mismo en el mismo orden: idea, perfil buscado, criterios, ruta y qué cubría el proyecto. Eso permite comparar capítulos de un vistazo.
* Cifras solo las que ya publicaba la web: 5 movilidades, más de 120 participantes, más de 150 vídeos, podcasts y reels, más de 500 km en tren, más de 150 km en bici, más de 20 km diarios a pie, cuatro Human Libraries por capítulo.
* Se quita el "thousands of young individuals" de About, porque contradice la cifra de 50 participantes de ediciones anteriores.
* El botón "Get involved" pasa a "Contact" y el registro desaparece.

**Páginas nuevas o reformuladas**

| Página | Qué cambia |
|---|---|
| Home | Hero de proyecto completado, tarjetas con estado "Completed", banda "Want to know more?" en lugar del registro |
| About | Cifras de ediciones anteriores con su fuente, historia, línea de tiempo 2021 a 2025 y bloque sobre cómo conecta con las prioridades de Erasmus+ |
| Cinco capítulos | Plantilla común con datos clave, perfil, criterios, ruta con fotos y qué cubría el proyecto |
| Human Library | Método, resultados esperables, cinco motivos y formato de sesión |
| Contact | Formulario que abre el correo y la dirección copiable |

## Puntos que debe validar el equipo

1. **Cifras de About.** Las he rotulado como "Spain edition in 2022 and Greece edition in 2023" porque coinciden con las ediciones anteriores. Hay que confirmar que es lo que significan.
2. **Cuatro prioridades de Erasmus+.** Inclusión y diversidad, movilidad verde, participación cívica y narrativa digital son una lectura mía de lo que dice la web. Conviene alinearlas con las del formulario de candidatura.
3. **Ruta en pasado.** Los textos dan por hecho que cada chapter se hizo como estaba publicado. Si hubo cambios de ciudad, fechas o actividades, hay que corregirlo.
4. **Resultados por capítulo.** Un evaluador agradecerá número de participantes, eventos realizados y público alcanzado por capítulo. La web actual no los da y no los he inventado.
5. **Fotos de las islas griegas.** Asigné las imágenes de stock a cada isla por orden, sin poder confirmar cuál es cuál.
6. **Formulario de contacto.** En esta propuesta abre el correo del visitante. En producción debería conectarse al formulario de WordPress.

## Cómo regenerar las páginas

Todas las páginas salen de `tools/build.py` y de `css/site.css`.

```
python3 tools/build.py
```

## Tercera ronda: resultados por capítulo

Cifras agregadas, sin datos personales, publicadas con confirmación de la persona responsable del proyecto. Las frases de participantes van firmadas solo con el nombre de pila.

**Fuentes**

* Informe técnico interno de noviembre de 2025: 125 participantes, 25 por movilidad, 4 Human Library por país, y los problemas de clima en Bulgaria y Países Bajos.
* Informe de diseminación de octubre de 2025: más de 600.000 visualizaciones, más de 20.000 cuentas alcanzadas, más de 1.000 seguidores orgánicos, más de 3.000 interacciones y más de 75 publicaciones.
* Hoja de valoración de Bulgaria: 5 respuestas, valoración media de 4,0 sobre 5, y 4 de 5 eligen una Human Library como actividad favorita.
* Catálogo de Human Books: 125 libros, según indicó la persona responsable.

**Dónde aparece**

| Página | Qué se añade |
|---|---|
| About | Cuadrícula de nueve cifras del proyecto y ficha con programa, número de proyecto, coordinador y socios |
| Cada capítulo | Cifras del capítulo, qué funcionó y qué se aprendió |
| Bulgaria | Valoración de la encuesta y tres frases de participantes |
| Spain | Catálogo de 125 Human Books |
| Human Library | Cifras del método en la práctica |
| Home | Enlace a los resultados |

**Pendiente de completar por el equipo**

* Valoraciones de los capítulos de Spain, Netherlands, Greece y Portugal. Solo existe la encuesta de Bulgaria.
* Lectores por evento: dos informes dan 30 y 20 de media. La web dice "20 to 30" hasta que se aclare.
* Las hojas de candidaturas incluyen filas vacías y pestañas duplicadas, así que no se usan sus recuentos.

## Cuarta ronda: ajustes

* El catálogo pasa a 125 Human Books, según la corrección de la persona responsable. Aparece en Spain y en la página de Human Library.
* Las fichas de capítulo de la home ya no dicen "Completed" y llevan un botón "Check the details". La etiqueta de cada capítulo pasa a "Chapter N of 5".
* Icono de Instagram en la cabecera, enlazado a https://www.instagram.com/eurolibrary.
* Nueva sección de socios en About y línea de coordinación en el pie. Coordina Asociación Xeración, con AltVenturers, De Kracht van Sport, The Future Now Association y GAIA Alentejo. El país de cada socio es una deducción a partir de los documentos del proyecto y conviene confirmarlo.
* El pie usa una versión azul del logo de la UE, que es el archivo blanco oficial recoloreado al azul de la UE. Si se dispone del archivo oficial en color, conviene sustituirlo en `assets/eu-funded-blue.png`.

**Valoraciones de los otros capítulos.** No se han añadido, porque en el Drive solo existe la hoja de valoración de Bulgaria. Hace falta el enlace a las de Spain, Netherlands, Greece y Portugal.
