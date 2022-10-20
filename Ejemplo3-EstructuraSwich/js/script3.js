function ejecutar() {
    //.value coje el valor
    var opcion = document.getElementById('opciones').value;
    var respuesta = document.getElementById('resultado');

    switch (opcion) {
        case "1":
            respuesta.innerText = "FORMATEANDO EL DISCO, espere por favor...";
            break;
        case "2":
            respuesta.innerText = "RECOPILANDO DATOS PARA SU ELIMINACIÓN, espere por favor...";
            break;
        case "3":
            respuesta.innerText = "CAMBIO DE UBICACIÓN IP, espere por favor...";
            break;
        case "4":
            respuesta.innerText = "NAVEGADOR MONITORIZADO, espere por favor..."
            +navigator.userAgent
            break;
        case "5":
            respuesta.innerText = "SALIR";
            break;
        default:
            respuesta.innerText = "Es necesario elegir una de la opciones del 1 al 5";
            break; 
            
    }
}