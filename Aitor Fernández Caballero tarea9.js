
document.addEventListener("DOMContentLoaded", () => {

    const botonClick = document.getElementById("botonClick");
    botonClick.addEventListener("click", () => {
        alert("¡Hiciste clic en el botón!");
    });


    const botonCambiar = document.getElementById("botonCambiar");
    const imagen = document.getElementById("imagen");

    const categorias = ["nature", "city", "technology", "animals", "mountains", "sea"];

    botonCambiar.addEventListener("click", () => {
        const categoriaAleatoria = categorias[Math.floor(Math.random() * categorias.length)];
        imagen.src = `https://source.unsplash.com/400x250/?${categoriaAleatoria}&${new Date().getTime()}`;
        imagen.alt = `Imagen de ${categoriaAleatoria}`;
    });

});


function comprobarEdad() {
    const inputFecha = document.getElementById("fecha").value;

    if (!inputFecha) {
        alert("Introduce tu fecha de nacimiento.");
        return;
    }

    const fechaNacimiento = new Date(inputFecha);
    const hoy = new Date();

    let edad = hoy.getFullYear() - fechaNacimiento.getFullYear();
    const mes = hoy.getMonth() - fechaNacimiento.getMonth();

    if (mes < 0 || (mes === 0 && hoy.getDate() < fechaNacimiento.getDate())) {
        edad--;
    }

    if (edad >= 18) {
        alert(`Tienes ${edad} años. ✅ Eres mayor de edad.`);
    } else {
        alert(`Tienes ${edad} años. ❌ Eres menor de edad.`);
    }
}
