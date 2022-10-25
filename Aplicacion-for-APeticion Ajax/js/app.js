/**
    OBJECT XMLhttpRequest(xhr) xhr es acronimo de XMLhttpRequest
    ¿Como ha contribuido este objeto representado en la interface del cliente? :
    1. Ha permitido que dicho objeto(xhr) acceda a las peticiones de los servidores WEB
        -mediante la directiva open().
    2. Puede enviar peticiones concretas
        -mediante la directiva send().
    3. Recibe las respuestas de los servicios WEB
        -mediante la directiva responseText()

    */

//Forma de crear un objeto var x; --> x = new XMLHttpRequest();
var xhr;

function buscarPokemon() {
    //Obtengo el objeto XMLHttpRequest y sus propiedades
    xhr = new XMLHttpRequest();

    //recuperamos el nombre desde su ubicación en html(id)
    //var dato = document.getElementById('nombre').value;           
    var dato = nombre.value;//id directo referenciado en html

    //Preparación de la petición:
    xhr.open("GET", "https://pokeapi.co/api/v2/pokemon/" + dato, true);// true = asincrono(sin esperar)

    //indicamos como queremos respuesta , entendiendo la cabecera
    xhr.setRequestHeader("accept", "application/json");
    //xhr.setRequestHeader("accept", "application/text");

    //CREAMOS LA FUNCION SUBORDINADA PARA CONTROLAR LA ENTRADA DE DATOS a traves de onreadystatechange
    xhr.onreadystatechange = procesarRespuesta;//Asignado a un remitente

    //Enviamos la peticion
    xhr.send();

    //Gestionamos el posible error, que ofrece la propiedad de objeto (onerror)
    xhr.onerror = procesaError;

    //Siempre van estas 7 lineas

}
function procesarRespuesta() {
//Primeros pasos de conexion, aseguramos que hay enlace partiendo de un if
    if(xhr.readystate = 4){//readystate
        var respuesta=[];
        respuesta = JSON.parse(xhr.responseText);
        //JASOn.parse(cadena) => Transformamos la cadena del json a object(Visualiza string)
        console.log(respuesta);
        document.getElementById('resultado').innerText=
        "Nombre: "+ respuesta.name+"\n"+
        "Altura: "+respuesta.height+"\n"+
        "Peso: "+respuesta.weight+"\n"+
        "Habilidades: "+"\n"
        var habilidades=respuesta.abilities;
        for(var i in habilidades){
            document.getElementById('resultado').innerText +=
            "\t"+habilidades[i].ability.name+"\n";
        
        }
       
    }
}
function procesaError() {
    document.getElementById('resultado').innerText="Error#";

}