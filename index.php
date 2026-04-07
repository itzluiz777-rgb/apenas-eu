<?php
//Luiz  Hottavio Costa Silva aura+ego
extract($_POST);
if (isset($a) && isset($b) && isset($c)) {
    

  $soma = $a+$b+$c;
  $sub = $a-$b-$c;
 
} else {
    $soma = null;
    $sub = null;
}



?>
<!DOCTYPE html>
<html  lang="pt-BR">
    <head>
       <meta charset="utf-8">
        <title>atividade</title>
        <style>
            .conteiner{
                position: absolute;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                width: 350px;
                height: 340px;
                border-style: solid;
                border-radius: 15px;
                border-color: black;
                padding:4%;
            }
           .conteiner button {
               position: absolute;
               top : 110px;
               left : 80px;
               top : 150px;
               border-radius: 10px;  
               border: none;         
               color: white;         
               background-color: black; 
               padding: 10px 20px;   
               cursor: pointer;      
            }
            .conteiner button:hover {
                 outline: none;           
                 background-color: darkred; 
                 color: black;            
                 box-shadow: 0 0 10px black; 
}
            .conteiner p {
                  position: absolute;
                  top : 180px;
                  left : 80px;
                  
            }
           
        </style>
    </head>
        <body>
            <div class='conteiner'>
                <form action= 'index.php' method='post' required>
                    <label for='A'>A:</label>
                    <input type='number' name='a'> 
                    </br>
                    <label for='B'>B:</label>
                    <input type='number' name='b'>
                    </br> 
                    <label for='C'>C:</label>
                    <input type='number' name='c'>
                    </br> 
                    <button type="submit">Enviar</button></br>
                </form>
                <p>
                <?php            
                    echo 'a soma dos 3 numeros: ',$soma;
                    echo '<br> a subtração do 3 numeros: ',$sub;
                    echo '<br> maior valor dos 3 numeros: ',max($a,$b,$c);
                    echo '<br> menor valor dos 3 numeros: ',min($a,$b,$c);
                    echo '<br> 1° número elevado pelo 2° numero: ',pow($a,$b);
                    echo '<br> Raiz quadrada do 3°: ',sqrt($c);
                ?>
                </p>         
            </div>   
       </body>
    </html>

   