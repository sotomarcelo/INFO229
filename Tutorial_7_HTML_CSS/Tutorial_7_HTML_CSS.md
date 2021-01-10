# Tutorial 7 HTML y CSS

## ¿Qué es el desarrollo Web?
El desarrollo web significa construir y mantener un sitio web; este trabajo se realiza en segundo plano, puede hacer que el sitio web tenga una apariencia perfecta, un funcionamiento rápido y un buen rendimiento para brindar la mejor experiencia de usuario.

## Frontend, Backend y Full Stack
En simples palabras para un desarrollador web existen distintas areas globalmente reconocidas y establecidas las cuales son las siguientes: 

- **Frontend**: se encarga de la composición, diseño e interactividad usando HTML, CSS y JavaScript.

- **Backend**: se encarga de lo que no se ve, es decir, dónde se almacenan los datos. Sin datos no hay Frontend. El Backend consiste en el servidor que acoge la web, una aplicación para ejecutarlo y una base de datos.

- **Full-stack**: está a cargo tanto del Frontend como del Backend, y necesita saber cómo funciona la web a todos los niveles para determinar cómo se van a coordinar la parte cliente y la parte servidor.

En esta serie de tres tutoriales se explicará de forma concisa, en lo que inicialmente se encarga un desarrollador **Frontend** para ello comenzaremos con lo mas basico que es HTML5.

## ¿Qué es HTML?

- HTML significa Hyper Text Markup Language (Lenguaje de marcado de hipertexto).
- El HTML es el lenguaje de marcado estándar para crear páginas web.
- El HTML describe la estructura de una página web.
- El HTML consiste en una serie de elementos.
- Los elementos HTML le dicen al navegador cómo mostrar el contenido.
- Los elementos HTML etiquetan piezas de contenido como "esto es un encabezado", "esto es un párrafo", "esto es un enlace", etc.
> **Nota:** Actualmente nos encontramos con la version 5 de HTML.

## Escribiendo HTML Básico.
A continuación se muestra un ejemplo con distintos elementos, etiquetados. Hay que entender que HTML es el esqueleto de una pagina y por ello su importancia en como esta se escriba. 

HTML es muy intuitivo ya que de la forma en que se escriba es como finalmente esta se mostrará.

> **Importante:** El formato en como este se guardará es archivo.html, pueden utilizar el editor que mas les acomode. Al hacer hacer doble click en el archivo, este se abrirá en su navegador predeterminado, mostrando lo que ya han realizado.

A cualquier sitio web es posible descargar su esqueleto y ver como esta desarrollado.

```html
<!DOCTYPE  html>
<html  lang="es">
<head>
   <meta  charset="UTF-8">
   <meta  name="viewport"  content="width=device-width, initial-scale=1.0">
   <title>Este es el titulo que se mostrara en la pestaña</title>
</head>

<body>
   <!--Encabezado-->
   <h1>Etiqueta que se utiliza para titulos.</h1>

   <!--Contenido de index.html-->
   <h2>Esta es una etiqueta de texto menor</h2>
   <p> Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolorem atque odit dolores deleniti officiis iure, porro vel laboriosam maxime rem perferendis nam quasi esse a tenetur dolor ad! Minima.
</body>
</html>
```

La declaración `<!DOCTYPE  html>` <!DOCTYPE html> define que este documento es un documento HTML5.
El elemento `<html>` es el elemento raíz de una página HTML.
El elemento `<head>` contiene meta información sobre la página HTML.
El elemento `<title>` especifica un título para la página HTML (que se muestra en la barra de título del navegador o en la pestaña de la página).
El elemento `<body>` define el cuerpo del documento, y es un contenedor para todos los contenidos visibles, como los encabezados, párrafos, imágenes, hipervínculos, tablas, listas, etc.
El elemento `<h1>` define un gran encabezado.
El elemento `<p>` define un párrafo.

## Listas, Tablas y Formularios.


**Listas**
Son utilizadas para maquetar un menú, aunque visualmente se vea mal esto será arreglado con estilos en cascada (**CSS**)-

```html
<!--Menú-->
<ul>
   <li><a href="index.html" title="Inicio"> Inicio</a></li>
   <li><a href="contenidos.html" title="Contenidos">Contenidos</a></li>
   <li><a href="contacto.html" title="Contacto">Contacto</a></li>
</ul>
```
- La etiqueta `<li>` define un elemento de la lista.
- La etiqueta `<ul>` define una lista no ordenada (con viñetas).
- La etiqueta `<a>` define un hipervínculo, que se utiliza para enlazar de una página a otra.

**Tablas**
```html
<table style="width:100%">
  <tr>
    <th>Nombre</th>
    <th>Apellido</th> 
    <th>Edad</th>
  </tr>
  <tr>
    <td>Jill</td>
    <td>Smith</td>
    <td>50</td>
  </tr>
  <tr>
    <td>Eve</td>
    <td>Jackson</td>
    <td>94</td>
  </tr>
  <tr>
    <td>John</td>
    <td>Doe</td>
    <td>80</td>
  </tr>
</table>
```

- La etiqueta `<table>` define una tabla HTML.
- Cada fila de la tabla se define con una etiqueta `<tr>`. Cada encabezado de la tabla se define con una etiqueta `<th>`. Cada dato/célula de la tabla se define con una etiqueta <td>.

> **Nota:** Por defecto, el texto en los elementos `<th>` están en negrita y centrados.
Por defecto, el texto en los elementos `<td>` son regulares y alineados a la izquierda.

**Formularios**
```html
<form>
   <p>
      <label  for="nombre">Nombre</label> <br/>
      <input  type="text"  name="nombre"/>
   </p>

   <p>
      <label  for="biografia">Biografia</label> <br/>
      <textarea  name="biografia"></textarea>
   </p>

   <p>
      <label  for="edad">Edad</label> <br/>
      <select  name="edad">
          <option  value="mayor">Mayor de edad</option>
          <option  value="adulto">Adulto</option>
          <option  value="65">Mayor de 65 años</option>
      </select>
   </p>
   
   <imput  type="submit"  value="Enviar email"/>
</form>
```

- El elemento HTML `<form>` se utiliza para crear un formulario HTML para la entrada del usuario.
- La etiqueta `<li>` se usa dentro de las listas ordenadas(`<ol>`), las listas no ordenadas (`<ul>`), y en las listas de menú (`<menu>`).
- La etiqueta `<label>` define una etiqueta para muchos elementos del **form**.
- La etiqueta `<option>` define una opción en una lista de selección.
- El elemento `<select>` se utiliza más a menudo en un formulario, para recoger las entradas del usuario.
- La etiqueta `<textarea>` define un control de entrada de texto de varias líneas.

## ¿Ahora que sigue?
Luego de entender lo básico respecto al esqueleto de una pagina web nos iremos a la parte estetica y visual de la pagina lo que seria como la piel. Esto mayormente conocido como **CSS**.

## ¿Qué es CSS?
**CSS** (**C**ascading **S**tyle **S**heets) o en español Hojas de Estilo en Cascada es un tipo de lenguaje encargado en la forma en como se presentara un **HTML** agregando estilos y disposicion en una pagina web. Para ello en la siguiente parte del tutorial veremos como se implementa **CSS** a un **HTML**.

## Implementación CSS a HTML
Para la implementación de estilos existen diversas formas de hacerlo y a continuación veremos algunas de ellas:
1. **Utilizando styles en las etiquetas de HTML.**

```html
<h1 style="color: brown; font-size: 35px;">Un ejemplo de texto </h1>
```
En este ejemplo estamos agregando estilos a un `<h1>` el cual tendra un color cafe y ademas un tamaño de letra de 35px. Como podemos ver, son muy intuitivas las propiedades de **CSS** aún asi esta es la peor practica que se puede realizar ya que crea un codigo desordenado y poco practico a futuro.

2. **Utilizando la etiqueta styles.**
```html
<head>
   <title>Ejemplo de titulo </title>
   <style>
      h1{
         color: red;
         font-size: 50px;
      }
   </style>
</head>
```
A diferencia del anterior, este formato intenta ser mas ordenado pero llegamos a la misma situación cuando el HTML tiende a ser mas grande. Es por ello que tampoco es una muy buena practica.

3. **Creando un archivo css aparte**.
Ahora llegamos a la forma mas utilizada, la cual consiste en crear un archivo css (idealmete con el nombre de styles.css) la cual se unirá directamente con el HTML haciendo asi que el codigo sea mas limpio y estructurado.

Ejemplo de styles.css
```css
body{
   background: gray;
}

h1{
   color: red;
   font-size: 50px;
   text-decoration: underline;
}
```
 **Importante:** Ahora para unir ambos archivos utlizaremos `<link>` siendo **href** lo mas importante de rellenar ya que este es nuestra direccion en donde se encunetra el archivo CSS. 
```html
<link rel="stylesheet> type="text/css" href="styles.css">
```

Con esto en mente, ye tenemos una idea básica del uso de CSS. Utilizamos algunas de sus propiedades y ademas del uso de selectores. Ahora bien, **¿Qué son los selectores?**.

## 1. **Selectores**
Los selectores, como bien dice su nombre, son los encargados de definir a que atributos de HTML se les agregar estilos CSS, existen varias maneras de implementarse y estas son:
1. **Selector universal.**
Este tipo de selector lo que hace es aplicar un estilos a todas las etiquetas que se encuentran. Esto se utiliza normalmente para dar un estilo general a la pagina para luego ir generando nuevos estilos.  Por ejemplo:

	HTML:
	```html
	<h2>Ejemplo de titulo</h2> 
	<p>Esto es un parrafo</p> 
	<h2>Ejmplo de titulo</h2>
	<p>Esto es un parrafo</p>
	```
	CSS:
	```css
	*{
	   font-family: Verdana, Geneva, Tahoma, sans-serif;
	   margin: 0px;
	   padding: 0px;
	}
	```
	Con esto, tanto al `<h2>` como el `<p>` se les cambiará el tipo de letra, tambien su margin y padding (margin interno). Todos estos atributos se iran entendiendo mas adelante.

2. **Selector de etiqueta**
El selector de etiquetas lo que hace es aplicar estilos a todas las etiquetas del mismo nombre. Utilizando el mismo ejemplo anterior.
CSS:
	```css
	p{
	   font-family: Verdana, Geneva, Tahoma, sans-serif;
	   font-size: 50px;
	}
	```
	Con esto aplicariamos a todos los `<p>`(parrafos) que existan los estilos de font-family y font-size.

3. **Selector de id**

	HTML:
	```html
	<div id="caja">
	   <h3>Ejemplo de titulo</h3> 
	   <p>Esto es un parrafo</p> 
	   <h4>Ejmplo de titulo</h4>
	   <p>Esto es un parrafo</p>
	</div>
	```
	CSS:
	```css
	#caja{
	   font-family: Verdana, Geneva, Tahoma, sans-serif;
	   color: red;
	   border: 1px solid black;
	}
	```
	A diferencia del selector universal y de etiquetas, este tipo de selector se encarga de aplicar estilos a etiquetas unicas y no tiende a repetirse varias veceses a diferencia de otros selectores.
	> **Importante:** La forma en que se leen una hoja de estilo es de arriba hacia abajo dando siempre prioridad a lo que se encuentre al final por ello es importante definir bien los estilos.

Otro punto importante a destacar al utilizar selectores es que los estilos se pueden compartir, por ejemplo (utilizando el css anterior) si quiero compartir los estilos de **#caja** a otro selector debemos hacer lo siguiente:

CSS:
```css
#caja,
#otroselector{
   font-family: Verdana, Geneva, Tahoma, sans-serif;
   color: red;
   border: 1px solid black;
}
```

4. **Selector de clase**
	HTML:
	```html
	<div id="caja">
	   <h2>Ejemplo de titulo</h2> 
	   <h3>Ejemplo de titulo</h3> 
	   <p class="parrafo">Esto es un parrafo</p> 
	   <h4>Ejmplo de titulo</h4>
	   <p class="parrafo">Esto es un parrafo</p>
	</div>
	```
     Este selector tiende a repetirse en varias etiquetas haciendo su difrencia al selector id.
     
     La forma de utlizarse en **CSS** sería asi:

	CSS:
	```css
	.parrafo{
	   font-family: Verdana, Geneva, Tahoma, sans-serif;
	   color: red;
	   border: 1px solid black;
	}
	```
     Este selector tiende a repetirse en varias etiquetas y ademas en su forma de utlizarse ya que para su mension en HTML debe definirse por class y en tanto al CSS este se invoca con un punto seguido de su nombre.
     
5. **Selector de atributo**
	```html
	<div  id="usuario">
	   <form>
	      <label  for="nombre">Nombre</label>
	      <input  type="text"  name="nombre">
	      <label  for="apellidos">Apellidos</label>
	      <input  type="text"  name="apellidos">
	      <input  type="submit"  value="Enviar">
	   </form>
	</div>
	```
	Utilizaremos el selector de atributos para como dice su nombre, dar estilos a atributos especificos de HTML. Por ejemplo aqui tenemos un formulario y aplicaremos CSS.

	```css
	input[type="text"]{
	   margin-bottom: 15px;
	   padding: 10px;
	   width: 300px;
	}
	```
	Aquí se le estaría aplicando estilos a los tipo `type="text"`, dejando un margen abajo de 15px y un margen interior de 10px y un largo de 300px.

6. **Selector hijo**
	HTML
	```html
	<ul  id="menu">
	   <li>
	      <a  href="#">Inicio</a>
	      <ul>
	         <li><a  href="#">HTML</a></li>
	         <li><a  href="#">CSS</a></li>
	         <li><a  href="#">LESS</a></li>
	      </ul>
	   </li>
	   <li><a  href="#">Temario</a></li>
	   <li><a  href="#">Reseña</a></li>
	   <li><a  href="#">Contacto</a></li>
	</ul>
	```
    CSS
    ```css
    #menu > li > a{
       font-size: 18px;
       color: red;
       text-decoration: none;
    }
    ```
    Con el selector hijo solo aplicariamos estilos a los primeras etiquetas marcadas. Por ejemplo en este caso a todos las etiques que vienen despues del `<ul>` que son `<li>` a sus `<a>` se les aplicara los estilos dichos.
    
   **Pueden revisar la carpeta selectores y ver un ejemplo de maquetación aplicando los distintos selectores vistos.**
  
## 2. Fuentes

1. **Propiedades basicas:**
- font-family: es un estilo de css en el cual existe una familia de fuentes, la razón de esta es porque puede existir algun navegador que no tenga una y seguira con la siguiente, es mas bien para asegurarse en que exista una fuente (como minimo).
- font-size: como lo dice su nombre, font-size es para definir un tamaño de letra para las fuentes, tienden a medirse con pixeles (px).
- font-weight: es para aplicar un grosor de letra, existen varias propiedades para esta (bold, bolder, inherit) o simplemente con pixeles.

	2.**Fuentes personalizadas:**
	 Se busca utilizar fuentes externas a css para crear una imagen distinta a las otras pagians webs. Idealmente se deben utilizar fuentes personalizadas compatibles con las mayorias de navegadores webs es por ello que existen distintas sitios en donde entregan un sin fin de fuentes, como por ejemplo Google Fonts : <a> https://fonts.google.com/.
	 
	Se puede implementar las fuentes ya sea descargando el archivo o implementandolo de forma online utilizando su direccion url. 
	- Forma directa:  Utilizando la etiqueta `<link>` en HTML.

	```html
	<link href="https://fonts.googleapis.com/css2?family=East+Sea+Dokdo family=Roboto:wght@100&display=swap" rel="stylesheet">
	```

	Luego la utilizamos en el styles.css de la siguiente manera, con ello poderemos aplicar tamaños, tipos de bordes, etc.
	```css
	font-family: 'Roboto';
	font-size: 18px;
	```

	- Descargando el archivo de fuentes: En este caso deberíamos guardar las fuentes en una carpeta en donde se encuentre nuestra pagina. Para asi tener un mejor control de estas.
	Su forma de implementación es la siguiente:

	```css
	@font-face{
	   font-family: definimosNombre
	   src: url(ubicacion/tifodefuente.ttf);
	}
	```
	Luego de implementarla podemos usarla en las distintas etiquetas con los selectores.
	Por ejemplo:
	```css
	h1{
	   font-family: 'definimosNombre';
	   font-size: 18px;
	}
	```
3. **Colores**
- Colores del sistema: <a> https://www.w3schools.com/cssref/css_colors.asp 
 Ejemplo:
    ```css
    h1{
	   font-family: 'definimosNombre';
	   font-size: 18px;
	   color: Olive;
	}
	```
- Colores hexadecimales: colores que se antepone un #.
  ```css
  h1{
     font-family: 'definimosNombre';
     font-size: 18px;
     color: #000000; /*Negro*/
  }
  ```
- Colores RGB: colores que se generan por el rojo, verde y azul (colores primarios). <a> https://www.css3maker.com/css-3-rgba.html
Ejemplo:

  	```css
	h1{
	   font-family: 'definimosNombre';
	   font-size: 18px;
	   color: rgb(255,255,107)
	}
    ```
- Colores RGBA: colores que ademas de ser creado por rojo, verde y azul tienen tambien opacidad (en su cuarto argumento).
Ejemplo: 
  	```css
	h1{
	   font-family: 'definimosNombre';
	   font-size: 18px;
	   color: rgba(255,255,107,0.8)
	}
	```

## 3. Fondos
- background-color: se utiliza, como dice su nombre, para unicamente el color de fondo.
- background-image: agregar una imagen al sitio web utilizando una direccion ya ubicada en el equipo.
- background: idealmente se utiliza para pintar una etiqueta por completo de un color ademas de poder colocar una imagen como su posicón.
- border: se utiliza idealmente para aplicar borde a una etiqueta, tienendo idealmente 3 parametros, el primero con el ancho del border, el tipo de borde (si es en linea, interlineado, etc) y por ultimo su color.

	```css
	body{
	   background-color: #ccc;
	   background-image: url("img/imagen.jpg");
	}

	#caja{
	   border: 5px solid black;
	   background-color: rgb(94,131,212);
	   color: white;
	}
	```
## 4. Textos
- color: para especificar un color a nuestro texto.
- font-family: definir tipos de fuentes disponibles en un orden para disponibilidad en el navegador.
- text-aling: se usa para alinear el text, ya sea centrado, justificado, izquierda o derecha.
- line-height: es para definir que tan separada estaran las alturas de lineas.
- text-transform: su función es transformar el tipo de letra como por ejemplo **uppercase** que significa dejar todo en mayusculas.
- text-decoration: aplicar un efecto en la letra como por ejemplo underline (colocar un linea por dejabajo del texto).
- text-indent: identar el texto por cada salto de pagina.
- word-spacing: cantidad de espacio que habrá por cada palabra en el texto.
- letter-spacing: la cantidad de espacios que habra dentro de una palabra.
## 5. Cajas
En este punto trabajaremos sobre las distintas cajas que se pueden crear sobre una pagina, su margenes, anchos, altos y su posicionamiento.

Utilizando el siguiente html:
```html
<body>
   <h1>Cajas en CSS</h1>
   <div class="caja">
      <p>Contenido de la caja 1</p>
   </div>

   <section class="caja">
      <p>Contenido de la caja 2</p>
   </section>
```
Ahora en el css comenzaremos aplicar algunas propiedades a los selectores:

```css
/*Definimos propiedades globales*/
*{
   margin: 0px;
   padding: 0px;
}

/*definimos propiedades a las cajas del html*/
.caja{
   width: 250px;
   height: 250px;
   background-color: lightblue;
}
```
> **Importante:** con width y height definimos el tamaño de la caja y para ver su cambio la hacemos utlizando background-color.

**Margin y padding**
1.  Con margin definiremos un borde invisible para nuestras cajas, este margin se puede trabajar de distintas maneras.
         -   margin con un argumento: **margin: 15px;**, será aplicado un margen hacia todos los lados de la caja de 15 pixeles.
         -  margin con mas argumentos: **margin: arriba derecha abajo izquierda;** con esto definimos distintos tamaños de margenes para sus lados.
         - margin por definicion de nombre: tambien en *css* existe margin-top, margin-bottom, para mayor facilidad al usuario.

A nuestro ejemplo le aplicaremos un margin total de 15 pixeles por cada lado  (como se ve a continuación).
```css
.caja{
   width: 250px;
   height: 250px;
   background-color: lightblue;
   margin: 15px;
}
```
2. padding: con esta propiedad podremos definir un borde invisible pero al interior de nuestras etiquetas.  Al igual que el margin estas se dividen en distintas formas de uso. Con un argumento, con varios o directamente por su nombre.

```css
.caja{
   width: 250px;
   height: 250px;
   background-color: lightblue;
   margin: 15px;
   padding: 20px;
}
```
**Posicionamientos de cajas**
En css existen varias formas de posicionar cajas, en este caso utilizaremos una que su función principal era para imagenes que se encontraban en un texto, nos referimos al float.

Por ejemplo si aplicamos float a nuestras cajas ya existen lo que sucedera es que estas se colocaran una al lado de la otra, como se ve en la imagen siguiente.
![enter image description here](https://uniwebsidad.com/static/libros/imagenes/css/f0509.gif)
Ahora aplicaremos esto a nuestro css.
```css
.caja{
   width: 250px;
   height: 250px;
   background-color: lightblue;
   margin: 15px;
   padding: 20px;
   float: left;
}
```

Un problema que podemos encontrar al utilizar float es que si luego de la cajas existen mas parrafos o textos estos se alinearan al lado de las cajas, esto por lo que se dijo an terior ya que los float se utilizan para eso.

Para ello agregaramos a nuestro html un div que arreglará esto.
```html
<div class="clearfix"></div>
```
 Y en los estilos css agregamos el selector class de clearfix, con lo cual arreglamos el problema del texto flotado a la derecha.
```css
.clearfix{
   float: none;
   clear: both;
}
```


## 6. Pseudoclases 
En este apartado veremos lo que son las pseudocales y como aplicarlas. Usaremos un html basico en donde aplicaremos esto.

HTML:
```html
<ul>
   <li>Palabra 1</li>
   <li>Palabra 2</li>
   <li>Palabra 3</li>
   <li>Palabra 4</li>
</ul>
```

Ahora en *styles.css* aplicaremos las pseudoclases.

```css
ul li:first-child{
   color: purple;
   font-weight: bold;  
}
```
Con esta primera pseudoclase aplicaremos caracteristicas al primer li (hijo) que se encuentra en el ul (lista).

```css
ul li:nth-child(1){
   color: red;
   font-weight: bold;  
}
```
Aqui estaríamos aplicando a un hijo en especifico de la lista, en este caso el segundo hijo.
```css
ul li:last-child{
   color: green;
   font-weight: bold;  
}
```
Y por ultimo, aplicaremos caracteristicas al ultimo hijo.

Existen varios tipos de pseudoclases pero esta es una de las mas utilizada para mas ejemplos entrar a <a> https://www.w3schools.com/css/css_pseudo_classes.asp
