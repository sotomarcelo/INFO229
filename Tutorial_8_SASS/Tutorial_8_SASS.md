# Tutorial 8 SASS

## ¿Qué es un preprocesador?
Un preprocesador CSS es un programa que te permite generar CSS, es un lenguaje declarativo que controla el aspecto de las páginas web en el navegador de una forma mas practica y legible, esto nos ahorra tiempo y facilidad de uso.

## ¿Que preprocesadores existen?
Hoy en dia existen varios preprocesdores para facilitar la vida de un programador, entre ellos hay dos que sobresalen sobre los demas y que ha tomado fuerza ultimamente y estos son SASS Y LESS. En este tutorial trabajaremos con SASS.

## Instalación de SASS
Existen dos maneras de instalar *SASS* mediante aplicaciones o por lineas de comando. En este caso lo haremos por lineas de comando, especificamente por node.js.

Para ello instalaremos node.js https://nodejs.org/es/ descargando la versión mas estable que este disponible.

Luego de haber instalado node.js, verificaremos si se encuentra en nuestro sistema, esto lo haremos escribiendo en nuestro cmd `node -v` si muestra la version de node significa que se instaló correctamente si no, significa que hubo un error de instalación.

Tambien verificaremos si el gestor de paquetes de node se encuentra disponible con `npm -v`.

Ahora instalaremos SASS con el siguiente comando:

    npm install -g sass
Ya estaria completa la instalación de SASS.

## Creación de archivos SASS.
Para poder trabajar con SASS crearemos un archivo styles.scss (el **scss** es el tipo de archivo sass).

## 1. Variables y compilación

```html
<!DOCTYPE html>
<html>
   <head>
      <meta charset="utf-8"/>
      <title> Aprendiendo SASS </title>
      <link rel="stylesheet" type="text/css" href="styles.css"/>
   <body>
      <h1> Aprendiendo SASS </h1>
      <p> SASS es un preprocesador CSS muy popular y potente.<p>
   </body>
</html>
```

Sass puede generar variables las cuales pueden ser utilizadas invocandolas en los distintos selectores de css.

Por ejemplo:
```scss
/*Variables ya creadas*/
$fuente-tipica: sans-serif, Helvetica, Arial;
$color-fondo: #ccc;

/*Aplicaremos las variables*/
body{
   background-color: $color-fondo;
}

h1{
   font-family: $fuente-tipica;

}
```

Ya que tenemos creadas nuestro primer codigo de sass ahora lo debemos compilar, para ello nos ubicaremos con cmd en la carpeta en donde se encuentra nuestros archivos y compilaremos de la siguiente manera:

    sass --watch styles.scss styles.css

Luego de compilar nos daremos cuenta que se creo un archivo en nuestro directorio el cual es un styles.css que contiene lo siguiente:

```css
body {
   background-color: #ccc
}

h1{
   font-family: sans-serif, Helvetica, Arial;
}
```

Con ello sabemos que con SASS trabajaremos mas limpio pero esto luego se transformara en el CSS tipico, lo interesante de SASS es que siempre se estará compilando cada vez que este se actualice.

## 2. Anidación
La anidación consiste en facilitar el uso de estilos para etiquetas que se encunetran dentro de otras para entenderlo mejor usaremos lo siguiente:

En nuestro HTML agregaremos...

```html
<div class="caja">
   <h1>Soy una caja</h1>
   <p>Soy un parrafo<p>
   <div class="info">
      08-01-2021
   </div>
</div>
```

Ahora en SASS 

```scss
.caja{
   border: 1px solid black;
   width: 500px;
   margin: 0px auto;
   text-align: center;
   background-color: white;
   
   h1{
      color: blue;
   }
   p{
      color: green;
   }
   .info{
      font-size: 10px;
   }
}
```
Esto es imposible hacerlo con css tipico y además es muy intuitivo a lo que estamos modificando.

## 3. Módulos
Los modulos es una forma de organizarse entre los estilos que manejamos para asi ser mas útil en su verificación y uso.

Para ello dividiremos lo ya realizado en tres archivos scss.

_encabezado.scss
```scss
/*Variables ya creadas*/
$fuente-tipica: sans-serif, Helvetica, Arial;
$color-fondo: #ccc;

/*Aplicaremos las variables*/
body{
   background-color: $color-fondo;
}

h1{
   font-family: $fuente-tipica;

}
```

_base.scss
```scss
.caja{
   border: 1px solid black;
   width: 500px;
   margin: 0px auto;
   text-align: center;
   background-color: white;
   
   h1{
      color: blue;
   }
   p{
      color: green;
   }
   .info{
      font-size: 10px;
   }
}
```

Ahora utilizaremos los modulos en nuestro archivo original styles.scss

```scss
@use 'base';
@use 'encabezado';
```

Con esto simplemente dividimos nuestros estilos en diferentes archivos pero en compilazión y creación de codigo es el mismo.

## 4. Mixins con SASS
Los mixins son las tipicas funciones que se pueden crear en un lenguaje de programación.

Un ejemplo:
```scss
@mixin crearBordes(){
   border: 5px solid red;
   border-radius: 10px;
   box-shadow: 0px 0px 5px black;
}
```

Esto lo podemos aplicar a nuestro html ya creado como por ejemplo al selector caja y se hace de la siguiente manera.

```scss
.caja{
   @include crearBordes():
}
```

Ahora si queremos utilizar la misma función pero cambiando ciertos valores lo podemos hacer de la siguiente manera.

```scss
@mixin crearBordes($color,$size,$shadow){
   border: $size solid $color;
   border-radius: $size;
   box-shadow: 0px 0px $size $shadow;
}
```
```scss
.caja{
   @include crearBordes(red, 10px, black);
}

.caja2{
   @include crearBordes(green, 20px, #ccc);
}
```
## 5. Herencia
La herencia es muy semejante a los mixins pero tienen menos caracteristicas, a continuación un ejemplo.

Crearemos en nuestro HTML lo siguiente:

```html
<div class="alert">
   Hola soy una alerta normal
</div>

<div class="alert alert-danger">
   Hola soy una alerta normal
</div>

<div class="alert alert-success">
   Hola soy una alerta normal
</div>
```

Con la herencia lo que aremos es generar unas caracteristicas fijas para caja hijo y luego modificaremos algunas de ellas dentro de caja selector.
```scss
/*Creamos nuestra herencia*/
%alert-normal{
   border: 1px solid gray;
   background: #eee;
   color: gray;
   padding: 10px;
   width: 80%;
   margin: 20px auto;
}

/*Aplicamos la herencia a los distintos selectores*/
,alert{
   @extend %alert-normal;
}

.alert-danger{
   @extend %alert-normal;
   color: red;
   border-color: red;
}

.alert-danger{
   @extend %alert-normal;
   color: green;
   border-color: green;
}
```
## 6. Operadores
Sass tambien nos posiblita el uso de operadores (al igual que un lenguaje de programación).

```scss
h1{
   font-size: 20px + 5px - 1px;
}

.caja{
   width: 500px / 1920px * 100%;
}
```
