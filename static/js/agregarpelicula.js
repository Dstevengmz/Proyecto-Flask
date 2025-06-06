document.getElementById("formPelicula").addEventListener("submit", function(event) {
    event.preventDefault(); 

    const codigo = document.getElementById("codigo").value;
    const titulo = document.getElementById("titulo").value;
    const protagonista = document.getElementById("protagonista").value;
    const duracion = document.getElementById("duracion").value;
    const resumen = document.getElementById("resumen").value;
    const foto = document.getElementById("foto").value;
    const genero = document.getElementById("genero").value;

    const data = {
        codigo: codigo,
        titulo: titulo,
        protagonista: protagonista,
        duracion: duracion,
        resumen: resumen,
        genero: genero,
        foto: foto
    };

    fetch('/agregarpelicula/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.text())
    .then(data => {
        const parser = new DOMParser();
        const doc = parser.parseFromString(data, "text/html");

const estado = doc.querySelector('#alert-container').getAttribute('data-estado');
const mensaje = doc.querySelector('#alert-container').getAttribute('data-mensaje');

if (estado === "True") {
    Swal.fire({
    icon: 'success',
    title: '¡Éxito!',
    text: mensaje,
    confirmButtonText: 'Aceptar'
}).then(() => {
    window.location.href = '/listapelicula/';
}
);
} else 
{
Swal.fire({
    icon: 'error',
    title: '¡Error!',
    text: mensaje,
    confirmButtonText: 'Aceptar'
});
}
}).catch(error => {
    Swal.fire("Error en la solicitud",error);
    Swal.fire({
    icon: 'error',
    title: '¡Algo salió mal!',
    text: "Hubo un problema al procesar la solicitud.",
    confirmButtonText: 'Aceptar'
        });
    });
});
