# Diferencia entre las unidades de medida PX, EM y REM en CSS

La principal diferencia entre las unidades de medida PX, EM y REM en CSS es la siguiente:

- **PX (píxeles)**: Es una unidad de medida absoluta, que no depende de ningún otro elemento. 1 px siempre será igual a 1 píxel en la pantalla, independientemente del tamaño de fuente o dispositivo.[1][2][3]

- **EM**: Es una unidad de medida relativa al tamaño de fuente del elemento padre. Si un elemento tiene un tamaño de fuente de 16px y se le aplica un padding de 2em, el padding será de 32px (2 x 16px).[1][2][3][5]

- **REM**: Es una unidad de medida relativa al tamaño de fuente del elemento raíz (HTML). Si el elemento raíz tiene un tamaño de fuente de 16px y un elemento tiene un padding de 2rem, el padding será de 32px (2 x 16px), independientemente del tamaño de fuente de elementos padres.[1][2][3][5]

En resumen:
- PX es una unidad absoluta, EM es relativa al padre, y REM es relativa al elemento raíz.
- REM es más fácil de calcular y mantener que EM, ya que no depende del tamaño de fuente de elementos padres.[5]
- REM es más recomendable que EM cuando se quiere que el diseño se escale de manera consistente con los cambios de tamaño de fuente del usuario.[5]

Citations:
[1] https://lacolmenatecnologica.com/elementor-academy-temas/cual-es-la-diferencia-entre-px-em-rem-vw-y-vh/
[2] https://www.inabaweb.com/em-rem-y-px-en-css-cual-es-la-diferencia-y-cuando-utilizar-cada-unidad-de-medida/
[3] https://franciscoamk.com/unidades-de-medida-en-css/
[4] https://www.youtube.com/watch?v=HVPxR2RMQ18
[5] https://desarrolloweb.com/faq/cual-es-la-diferencia-entre-las-unidades-css-em-y-rem

##  Ejemplos de uso de la unidad de medida REM en CSS:

### Tamaño de fuente
```css
html { font-size: 16px; }
body { font-size: 1.2rem; } /* 19.2px */
h1 { font-size: 2.5rem; } /* 40px */
p { font-size: 1rem; } /* 16px */
```

### Márgenes y rellenos

```css
body {
  margin: 2rem; /* 32px */
  padding: 1.5rem; /* 24px */
}

h1 {
  margin-bottom: 1rem; /* 16px */
}

p {
  padding: 0.5rem 1rem; /* 8px 16px */
}
```

### Dimensiones
```css
.container {
  width: 80rem; /* 1280px */
  height: 40rem; /* 640px */
}

.item {
  width: 10rem; /* 160px */
  height: 10rem; /* 160px */
}
```

### Responsive design
```css
@media (max-width: 768px) {
  body { font-size: 1rem; } /* 16px */
  h1 { font-size: 2rem; } /* 32px */
  .container { width: 90vw; }
}
```

En estos ejemplos, el uso de REM permite que los tamaños de fuente, márgenes, rellenos y dimensiones se escalen de manera proporcional al tamaño de fuente del elemento raíz (HTML). Esto facilita el diseño responsive y la accesibilidad, ya que los usuarios pueden cambiar el tamaño de fuente del navegador y el diseño se ajustará automáticamente.