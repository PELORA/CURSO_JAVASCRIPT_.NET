function ejecutar(){

   var respuesta=document.getElementById("resultado");
   
   /*
         1 creamos el objeto
            sintaxis:
            var nombre = new Nombre(); Representada la variable objeto

   */
   var fecha = new Date();
   var dia=fecha.getDay();
   var menu="";
   switch(dia){
      case 0:
         menu="Hoy es Domingo y servimos arroz con vino";
            break;
      case 1:
         menu="Hoy es Lunes y servimos Cerrado por descanso";
            break;
      case 2:
         menu="Hoy es Martes y servimos Pote gallego";
            break;
      case 3:
         menu="Hoy es Miercoles y servimos Ensaladilla rusa";
            break;
      case 4:
         menu="Hoy es Jueves y servimos Torrijas con chorizo";
            break;
      case 5:
         menu="Hoy es Viernes y servimos Cocido Madrileño";
            break;      
      case 6:
         menu="Hoy es Sabado y servimos Atun con tomate";
            break;          
      default:   
         menu="#Error de conexion"      
   }

   document.getElementById('resultado').innerText=" "+menu;
}
/*
   
   */