/*
Ventajas metodos asociados querySelector() y querySelectAll()
    querySelector() similar a getelmentById()--> varios elementos con un mismo id
    querySelectAll() actua como un getElementByTagName--> tiene acceso a todos los elementos de una consulta
*/
var botones=document.querySelectorAll('button');
//esta a la escucha de todos los botones
var s=true;
for (const i of botones) {
    i.addEventListener('click',function(){

        //Llama al puntero del raton y devuelve nuestro primer objeto
        
        if(s==false){
            document.querySelector('.mensaje').innerHTML="Ahora Has seleccionado: "+"<br>"+this.innerHTML;
            s=true;
        }else if(s==true){
            document.querySelector('.mensaje').innerHTML="Has seleccionado: "+"<br>"+this.innerHTML;
            s=false;
        }
    
    });
}
