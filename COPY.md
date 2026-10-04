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
