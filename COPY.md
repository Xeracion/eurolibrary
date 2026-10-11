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

## Quinta ronda: URLs limpias

Las páginas se sirven sin `.html` (`/about`, `/spain`...). Lo hace `vercel.json` con `cleanUrls`, y `tools/build.py` genera los enlaces internos ya sin extensión. Las direcciones antiguas con `.html` redirigen a las nuevas. La copia de vista previa en Claude mantiene `.html`, porque ese entorno no admite URLs limpias.

## Sexta ronda: sin antetítulos

Se eliminan las etiquetas pequeñas que iban sobre los títulos en todas las páginas. La mención a Erasmus+ que llevaba la del hero de la home pasa a la primera frase del texto de apertura. Se mantiene la etiqueta "Chapter N of 5" de las páginas de capítulo, porque es un dato de navegación y no un antetítulo.

## Séptima ronda: fotos reales de Spain

Se añade una galería "Photos from the road" con 8 fotos del álbum compartido de Eurolibrary Spain, y la parada de Santiago pasa a usar una foto real de la llegada a la plaza del Obradoiro en lugar de una imagen de archivo.

Criterio de selección: paisaje y caminantes de espaldas, el montaje de una mesa de Human Library en una plaza y fotos de grupo en las que nadie queda en primer plano. Se dejaron fuera los primeros planos de participantes y de personas del público de las Human Library, porque en la web no consta su consentimiento para aparecer. Conviene que el equipo confirme los consentimientos de imagen antes de publicar las fotos de grupo.

## Octava ronda: fotos del álbum en las paradas, carrusel y sin "Who"

* Las fotos de archivo de las paradas de Spain se sustituyen por fotos del álbum. Se asignan por la fecha de captura que guarda el álbum, que coincide con el itinerario: el 28 de julio sale en Pontedeume y llega a Betanzos, el 29 es Ordes, el 30 Sigüeiro y el 31 Santiago.
* La imagen de portada de Spain pasa a ser una foto del álbum de caminantes por la carretera.
* La galería pasa a ser un carrusel con lightbox: flechas, teclado, Escape, gesto de deslizar en móvil y pie de foto con la fecha.
* Se elimina de los cinco capítulos la sección "Who we were looking for" (perfil y requisitos de participación). Los datos siguen en `tools/build.py` por si se quieren recuperar.

## Novena ronda: fotos con personas y botón al álbum

La persona responsable confirma que cuenta con el consentimiento de todas las personas de las fotos, así que se incorporan fotos con caras: conversaciones de la Human Library, un selfie en la carretera, caminantes de frente, el grupo descansando en el albergue y los abrazos en el Obradoiro. El carrusel pasa a 15 fotos, y las paradas de Betanzos, Sigüeiro y Santiago usan fotos con personas.

Se eliminan las descripciones visibles de las fotos, tanto bajo el carrusel como en el lightbox, que solo muestra el contador. El texto alternativo se mantiene para accesibilidad. Se añade el botón "View the full album", que abre el álbum compartido en una pestaña nueva.

## Décima ronda: texto de la Human Library, flechas y pie

* El bloque oscuro "Everything on the road" de los cinco capítulos pasa a ser "A library where the books are people", con un texto de apertura adaptado a cada destino y un párrafo común que explica cómo funciona. Los detalles salen de los informes y la web: la Human Library en el tren de Bulgaria, el catálogo de historias de Spain, la lluvia y el viento de Países Bajos, las escuelas y el ferry de Grecia y las cuatro paradas de Portugal.
* El anterior y el siguiente capítulo llevan flechas.
* El pie ya no dice "Project completed in 2025".

## Undécima ronda: fotos en Países Bajos

El álbum compartido como "Eurolibrary Greece" contiene en realidad fotos del capítulo de Países Bajos (pancartas de "The Dutch Way", bicicletas por Frisia, ferris y veleros), y se usa en esa página. La persona responsable indicó que se use en Países Bajos.

* Portada: la foto de grupo.
* Paradas: Leeuwarden con el grupo en la calle, Sint Annaparochie con el grupo en el dique, Terschelling con el ferry y Goingarijp con la vela. La imagen lateral de la idea pasa a una foto de tres ciclistas sonrientes.
* Carrusel de 15 fotos con lightbox, sin descripciones y con botón al álbum. Como las fotos son verticales, las diapositivas también lo son.
* Las fotos del álbum tienen una resolución máxima de 1440 por 1800 píxeles, menor que las de Spain.
* La página de Grecia sigue con sus imágenes de archivo hasta recibir el álbum correcto.

## Duodécima ronda: valoraciones y frases de participantes

Se usa el feedback de participantes españoles en los cinco proyectos para completar los resultados de cada capítulo. Solo se publican datos agregados y frases firmadas con el nombre de pila. No se usa ningún dato personal ni económico del archivo.

* Valoración media sobre 5 (columna de valoración global): Países Bajos 5.0 (4 respuestas), Portugal 5.0 (3), Grecia 5.0 (5), Spain 4.7 (3) y Bulgaria 4.2 (9 respuestas de dos formularios, con 4 de 5 que eligen la Human Library como actividad favorita).
* Cada capítulo añade "What worked" y "What we learned" y entre dos y tres frases positivas.
* Las valoraciones proceden solo de participantes españoles, y la nota bajo las cifras lo indica. Conviene confirmar con las personas citadas que aceptan aparecer con su nombre.

## Decimotercera ronda: favicon

Se usa el símbolo del logo (el libro con globo de diálogo), sin el nombre, como favicon. Se genera `assets/favicon.svg` con fondo crema redondeado para que se vea también en pestañas oscuras, además de `favicon-32.png` y `apple-touch-icon.png` para navegadores y dispositivos que no admiten SVG.

## Decimocuarta ronda: vista previa al compartir en redes

Cada página lleva etiquetas Open Graph y Twitter Card (título, resumen, dirección canónica e imagen), de modo que al compartir el enlace en redes o mensajería aparece un resumen con la imagen de cabecera.

* Las imágenes son de 1200 por 630 píxeles, recortadas de la foto de cabecera de cada página y guardadas en `assets/social/`. La portada usa una foto del aula, distinta de la de Países Bajos, para que no se repitan.
* Las direcciones son absolutas sobre `https://eurolibrary.eu`, como exigen los rastreadores de redes sociales. Si el dominio cambia, se ajusta `SITE` en `tools/build.py`.
* Las redes guardan en caché las vistas previas: para ver el cambio en un enlace ya compartido hay que refrescarlo con el depurador de cada red.

## Decimoquinta ronda: página del podcast People of EU

Se añade la página `podcast.html` (enlace "Podcast" en el menú y el pie) y un bloque en la portada que lleva a ella. Los datos salen del programa "PEOPLE OF EU | EUROLIBRARY" de Spotify (publicado por AltVenturers).

* Reproductor del programa completo de Spotify, que solo se carga cuando la persona pulsa el botón, porque Spotify puede instalar cookies.
* Explorador de episodios: filtros por tema, búsqueda por palabra, botón "Surprise me" y reproductor incrustado por episodio (solo uno abierto a la vez).
* Los temas (identidad, viajes y fronteras, salud y mente, deporte, naturaleza, trabajo e ideas) son una clasificación propia a partir de la descripción de cada episodio. Las portadas se alojan en `assets/podcast/`.
* Se muestran los 12 episodios más recientes que Spotify lista en la página del programa (números 89 a 100). La portada del programa habla de 100 historias, así que el reproductor completo cubre el resto. Para listar más episodios hace falta añadirlos a `EPISODES` en `tools/build.py`.
* Se han sustituido las rayas de las descripciones originales por comas.

## Decimosexta ronda: fotos de Grecia

Las fotos de archivo de la página de Grecia se sustituyen por fotos reales de la carpeta de Drive "Photos Natasa" (días 2 a 6, unas 1.000 fotos, de las que se revisó una de cada tres).

* Portada: la foto de grupo en la cubierta del ferry. Foto lateral: participantes sonriendo en el ferry.
* Paradas: el embarque en Pireo, el grupo sobre Ios, la Human Library en la Chora de Folegandros, el mar de Sifnos y la espera en el puerto de vuelta.
* Carrusel de 15 fotos con lightbox, sin descripciones visibles, y botón al álbum de Drive. Se eligieron fotos con buena luz y con composición clara: el ferry, las plazas blancas, los patios de las escuelas y los atardeceres.
* Las fotos se redimensionan a 1400 píxeles de ancho como máximo.
* Los créditos de las fotos no constan en la carpeta. Conviene que el equipo confirme el consentimiento de imagen, como en el resto de capítulos, y quién debe figurar como autoría.
* El botón del álbum apunta a la carpeta de Drive tal como se compartió. Si se quiere un álbum público más cuidado, basta cambiar `gallery_link` en `tools/build.py`.

Actualización: el botón "View the full album" de Grecia pasa a apuntar al álbum de Google Fotos del equipo (https://photos.app.goo.gl/DerMeM1c22HKJRPC6), en lugar de la carpeta de Drive.

Actualización del podcast: se añade el episodio 50, "I work on an educational game about circular economy" (6 de abril de 2026, 7 min), localizado con Firecrawl. La página pasa a 13 episodios y el texto aclara que es una selección y que el reproductor completo lista toda la serie.

Con Firecrawl y con el HTML de Spotify no se pueden listar más: Spotify solo sirve los primeros 12 episodios en la página del programa y el resto va tras un "Load more" que exige su API autenticada. Las búsquedas web solo indexan 13 episodios, y el programa no aparece en Apple Podcasts. Los números de portada no siguen el orden de publicación (el episodio 50 es de abril y el 89 de mayo), así que no se pueden deducir los demás.

## Decimoséptima ronda: la Human Library pasa a ser una guía metodológica

La página `/human-library` se amplía y pasa a ser "The Human Library guide": qué es una biblioteca humana y cómo organizar una. Se basa en los documentos del propio equipo en Drive ("Info Human Library", "Our amazing Human Library" y las pautas de movilidad de Eurolibrary) y en lo que se hizo en los cinco capítulos.

Contenido, con índice lateral que sigue el scroll (en móvil, una barra horizontal fija):
* Qué es: origen (Dinamarca, 2000; apoyo del Consejo de Europa en 2003), para qué sirve y las seis reglas de la biblioteca.
* Roles y espacios: libro, lector, bibliotecario, diccionario y promotor, con pestañas, y los tres espacios (recepción, estantería y espacio de lectura).
* Cómo funciona un préstamo: recorrido interactivo de ocho pasos y un temporizador de préstamo (15, 20 o 30 minutos).
* Organízala: lista de preparación en siete fases, de tres semanas antes a después del evento, con barra de progreso que se guarda en el navegador, botón de imprimir y lista de materiales. Las fases se basan en las pautas de movilidad.
* Escribe un libro: preguntas para encontrar la historia y un constructor de reseñas con contador de palabras (50 a 150, según la ficha del equipo).
* Mantenerla segura, medir el impacto, qué hicimos en Eurolibrary (cifras del proyecto) y preguntas frecuentes.

Notas para el equipo:
* No se han copiado los detalles del documento de 2012 que eran de un evento concreto en Polonia.
* La duración del préstamo se formula como "20 a 30 minutos, nunca más de 30", que concilia los dos documentos del equipo (máximo 30 en uno, 15 a 20 en el otro).
* Los datos del origen del método proceden de esos documentos y conviene contrastarlos con humanlibrary.org antes de citarlos en un informe.
* La cifra "20 a 30 lectores por evento" sigue pendiente de confirmar, como en rondas anteriores.

## Decimoctava ronda: PDF descargable de la lista de preparación

La guía ofrece el botón "Download PDF" junto a "Print" y "Reset" en la lista de preparación. El PDF (`assets/downloads/eurolibrary-human-library-checklist.pdf`) es una hoja A4 con las siete fases, la lista de materiales y las seis reglas, con el logo y el aviso de financiación de la UE. Se genera con `python3 tools/checklist_pdf.py` a partir de los mismos datos que la web (`HL_PLAN`, `HL_MATERIALS`, `HL_RULES` en `tools/build.py`), con las tipografías de `tools/fonts/`, así que si se cambia la lista basta con volver a ejecutarlo.

## Decimonovena ronda: manual metodológico descargable

La guía ofrece el manual "The Human Library handbook" en PDF (`assets/downloads/eurolibrary-human-library-handbook.pdf`, 50 páginas A4, unos 7 MB), con un botón en la cabecera y una tarjeta con la portada. Mantiene el diseño de la web (crema, naranja, DM Serif Display e Inter) y usa fotos ya publicadas en los capítulos.

Estructura:
* Portada, "About Eurolibrary and this handbook", índice con números de página y cuatro partes con 14 capítulos: entender (qué es, roles y espacios, el préstamo, seguridad y ética), preparar (planificar, sede, libros, equipo y lectores, el modelo Eurolibrary), llevar a cabo el día (guion y facilitación) y evaluar y compartir (evaluación, pódcast, lecciones y preguntas frecuentes).
* Anexos A1 a A17, listos para copiar: lista de planificación, hoja de guion del evento, convocatoria de libros, ficha del libro, hoja de reseña, agenda de formación, plantilla de catálogo, guion de bibliotecario, acuerdos de grupo, tarjeta de registro, hoja de préstamos, formularios de valoración de lectores y libros, consentimientos, matriz de riesgos, presupuesto y kit de promoción. Un último anexo reúne recursos y glosario.
* Cada capítulo cierra con ideas clave. Se incluyen citas de participantes ya publicadas en la web, solo con nombre de pila.

Cómo se genera: `python3 tools/handbook.py` (texto en `tools/handbook_content.py`, diseño en `tools/handbook.py`, tipografías en `tools/fonts/`). Necesita Chromium y poppler. El índice se numera solo en dos pasadas. Si se añade contenido hay que vigilar el máximo de 50 páginas, que el propio script informa al terminar.

Para el equipo, antes de difundirlo:
* El texto es nuevo. Se apoya en los documentos del equipo (ficha "Info Human Library", documento de organización de 2012 y pautas de movilidad) y en lo ocurrido en los cinco capítulos. Lo que es recomendación general (tamaños de equipo, estructura de la formación, guion de bibliotecario, consejos de datos y seguridad) está redactado por el asistente y conviene revisarlo.
* Los modelos de consentimiento y de protección de datos son generales y deben revisarse para cada país.
* La cita de la guía del Consejo de Europa figura sin enlace ni año exacto, y los orígenes del método proceden de los documentos del equipo. Contrastar con humanlibrary.org y el Consejo de Europa.
* La cifra de "120+ participantes" y "125 libros" es la que figura en la web, y "20 a 30 lectores por evento" no se usa.
* La licencia no está definida. El PDF pide "credit Eurolibrary" al reutilizar los anexos, pero no declara ninguna licencia.

## Vigésima ronda: efectos visuales ligeros

Se añaden efectos sutiles en todas las páginas, sin librerías (CSS más unas 30 líneas de JavaScript, en `FX` de `tools/build.py` y al final de `css/site.css`):
* Entrada suave de la cabecera al cargar la página.
* Aparición al hacer scroll (fundido y ligero ascenso, escalonado en las rejillas) de tarjetas, paradas, cifras, fotos, citas y bloques de las guías.
* Fundido de las imágenes con carga diferida.
* Barra de progreso de lectura fina en la parte superior.
* Microinteracciones: botones que se elevan, tarjetas con sombra al pasar el ratón, zoom suave en fotos, polaroids que se enderezan, subrayado animado en el menú y flecha del pie.

Accesibilidad y robustez: todo se aplica solo si la persona no ha pedido reducir el movimiento en su sistema. Sin JavaScript la web se ve completa, porque los elementos solo se ocultan cuando el script ya ha cargado, y al imprimir se muestra todo. Si algún efecto no gusta, se desactiva borrando su bloque en `css/site.css`.
