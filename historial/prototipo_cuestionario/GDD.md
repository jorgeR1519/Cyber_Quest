# Game Design Document

## Identidad y propósito

**CyberQuest: Defensa Digital** es una aventura de decisiones para estudiantes y jóvenes usuarios de internet. Busca practicar el reconocimiento de mensajes fraudulentos, la protección de cuentas y la respuesta básica ante alertas. No mide competencia profesional ni sustituye asesoría técnica.

La problemática inicial es la posible dificultad de algunos usuarios para reconocer engaños y proteger su información. Su frecuencia y presencia en el contexto local están pendientes de investigación. La propuesta se relaciona principalmente con ODS 4 mediante el aprendizaje interactivo; la relación secundaria propuesta con ODS 9 se basa en el desarrollo de una herramienta tecnológica educativa.

## Narrativa y personajes

Una ciudad tecnológica necesita activar su escudo digital. El jugador asume el rol de guardián y ayuda a Ada, usuaria del centro de comunicaciones, y Leo, responsable de una cuenta de la torre. Un sistema de alertas presenta las situaciones de los sectores.

## Escenarios y niveles

| Nivel | Escenario | Reto educativo | Escenas |
|---|---|---|---|
| La alerta sospechosa | Centro de comunicaciones | Verificar un mensaje y reportar phishing | 2 |
| El acceso protegido | Torre de identidad | Clave única y autenticación multifactor | 2 |
| La red comprometida | Estación de trabajo | Evitar descargas y seguir el protocolo | 2 |
| Operación Escudo Digital | Núcleo de la ciudad | Integrar verificación, protección y reporte | 3 |

## Mecánicas y consecuencias

### Ambientación visual por misión

El escenario ocupa toda la pantalla: fondo y márgenes decorados, barra superior, paneles, botones y desplazamiento adoptan el tema de cada misión. El contenido se coloca sobre una tarjeta clara central para mantener el contraste. Las nubes, árboles, lianas, torres y lava se distribuyen alrededor del área de lectura; el paisaje superior es un complemento. Los SVG muestran esta composición completa.

Actualización del 3 de noviembre de 2026: el primer nivel tiene islas de nubes en un cielo claro; el segundo, una selva con árboles y lianas; el tercero, un cielo al atardecer; y el cuarto, un infierno fantástico con fortaleza y lava. Los paisajes decoran la narrativa digital sin modificar sus objetivos educativos ni sus reglas.

Se mantiene el guardián pixel art, la tipografía legible y los paneles claros. Cada misión tiene su propia paleta de fondo, paneles y botones. Las nubes, lianas y brasas tienen movimientos suaves, junto con las animaciones existentes de respuesta. El mapa conserva la ciudad cálida. Los dibujos y colores se comparten con los SVG mediante temas.py.

Cada escena presenta un incidente con una evidencia examinable y cuatro acciones (una segura y tres riesgosas). El orden de los botones cambia para evitar memorizar posiciones. Las decisiones modifican recursos y reciben una explicación ligada al incidente. Los distractores incorporan medidas incompletas, confianza en señales superficiales y respuestas que trasladan el riesgo. Los últimos niveles combinan verificación, credenciales y reporte. Se conservan nueve situaciones contextualizadas.

### Ayudas estratégicas

Examinar evidencia es gratuito y no consume recursos. Para toda la partida hay 3 pistas tácticas, 2 comodines 50/50 y 1 consulta a la mentora Ada. Cada tipo puede usarse una vez por situación y los tipos se pueden combinar. La pista orienta el análisis; 50/50 elimina al azar dos acciones riesgosas y conserva la segura; Ada explica el principio de seguridad aplicable.

Usar pista, 50/50 o mentora reduce el premio de esa situación en 15, 25 o 40 XP respectivamente. No se descuentan puntos al pedir la ayuda ni se pierde energía. Un acierto sin ayudas otorga 100 XP; con todas las ayudas otorga 20 XP. Un error conserva la penalización normal, sin un coste adicional por las ayudas utilizadas. Los usos se consumen aunque la respuesta final sea incorrecta. Las ayudas se bloquean tras responder. Reiniciar misión restaura sus usos al estado inicial de esa misión, junto con puntos, energía e historial.

Se comienza con 3 de energía y 0 XP. Acción segura: +100 XP. Acción riesgosa: −50 XP y −1 energía. Los puntos nunca bajan de 0. Una misión completa recupera 1 energía, con máximo 3. No hay tiempo límite.

Para avanzar se resuelven todas las escenas y se pulsa Continuar tras cada explicación. No es obligatorio acertar todo: los errores tienen consecuencias, y se puede completar con energía restante. La misión siguiente se desbloquea al completar la actual. Las completadas no se repiten. Reiniciar la misión revierte todos sus cambios para evitar acumular puntos.

Victoria: cuatro misiones completas con energía positiva. Derrota: energía igual a 0. El final muestra puntos, cantidad de decisiones seguras y temas que conviene repasar. Máximo: 900 XP en nueve decisiones. El porcentaje de aciertos describe la partida; no prueba aprendizaje real.

## Navegación y prototipo de pantallas

Inicio (nombre y reglas) → Centro de mando (cuatro sectores y ayuda) → Misión (objetivo, incidente, evidencia, acciones, explicación) → Centro de mando o resultado final. El final permite volver a jugar o salir. No se guarda progreso al cerrar.

```text
CYBERQUEST                  XP | Energía | Progreso
Título de la misión
Objetivo y número de situación
Incidente narrativo
[Examinar evidencia]
[Acción A]
[Acción B]
Explicación de la consecuencia
[Continuar] [Reiniciar esta misión]
```

El mínimo técnico de la guía exige cuatro niveles, aunque otra sección mencione tres. Esta versión adopta cuatro.
