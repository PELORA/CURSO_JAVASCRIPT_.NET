function calcular(){
    /*
    1ª Fase 
    Defino las variables y la entrada de variables tipo y valor
    */
    //Asigno el valor String
    //var peso=document.getElementById('CalculoPeso').value;
    var peso=parseFloat(calculoPeso.value);//Coje el valor del id por defecto.
    //Siempre recoje valores como string.Hay que parsearlo
    //Hay variables directas y variables respusta
    //Asigno el valor Int
    var altura=parseFloat(calculoAltura.value);
    var imc=0;
    imc=peso/(Math.pow(altura,2));
    console.log(imc);
    var respuesta=document.getElementById('resultado');
     /*
    2ª Fase
    Gestion de las variables, osea ¿Que quiero hacer con las variables?
    */
    if(imc<=18.5){
        respuesta.innerHTML=" Índice de extrema delgadez, estas por debajo de 18.5 "
    }else if(imc<=24.9){
        respuesta.innerHTML=" Índice de masa corporal optimo, estas en el intervalo standart "
    }else if(imc<=29.9){
        respuesta.innerHTML=" Índice de masa corporal critico, estas por encima de la media "
    }else{
        respuesta.innerHTML=" Rasgos de obesidad claros"
    }
    /*
    3ª Fase 
    Soltar los resultados de manerta directa y con los valores de la variable definidos

    */


}