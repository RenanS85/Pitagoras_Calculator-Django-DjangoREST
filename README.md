<div>
<a href="#descrição">Descrição</a>
<a href="#ferramentas">Ferramentas</a>
</div>
    <div id="titulo e apresentação">
        <h1>Pitagoras_Calculator-Django-DjangoREST</h1>
        <p>Calculadora destinada a realizar cálculos e validações de um triângulo retângulo. Back-end: Django e Django rest framework, Front-end: HTML, CSS e JS.</p> 
    </div>
    <div id="descrição">
        <p>O projeto <a href="https://pitagoras-calculator.herokuapp.com/" target="_blank"> Pitagoras Calculator</a>(Calculadora de Pitágoras) é uma aplicação web que realiza funcionalidades referentes a relação matemática entre os comprimentos dos lados de um triângulo retângulo.</p>
        <p>"Em qualquer triângulo retângulo, o quadrado do comprimento da hipotenusa é igual à soma dos quadrados dos comprimentos dos catetos."</p>
    <div id="imagem">
        <img src="./triângulo retângulo.png">
    </div>
        <h4>
            hipotenusa<sup>2</sup> = cateto oposto<sup>2</sup> + cateto adjacente<sup>2</sup>
        </h4>
        <p>A relação entre os lados do triângulo retângulo permite, em se sabendo dois lados, calcular o terceiro</p>
        <h4>cateto oposto =  &radic;(hipotenusa<sup>2</sup> - cateto adjacente<sup>2</sup>) </h4>
        <h4>cateto adjacente =  &radic;(hipotenusa<sup>2</sup> - cateto oposto<sup>2</sup>) </h4>
        <p>O projeto <a href="https://pitagoras-calculator.herokuapp.com/" target="_blank"> Pitagoras Calculator</a> automatiza os cálculos para o usuário, de maneira que, ao se indicar dois lados para a aplicação, se obtém o valor do terceiro, <strong>se matemáticamente possível.</strong> Por exemplo, se após fornecer a hipotenusa e o cateto oposto, cateto adjacente for<strong>ZERO</strong>, o mesmo é um lado inválido.<a href="https://pitagoras-calculator.herokuapp.com/" target="_blank">Explore as possibilidades!</a></p>  
    <div>
        <a href="https://pitagoras-calculator.herokuapp.com/" target="_blank"><img src="./calculadora pitágoras.png"></a>
    </div>
        <p>Outra funcionaidade disponível para o úsuário é a escolha de indicar os três lados do triângulo e então deixar a <a href="https://pitagoras-calculator.herokuapp.com/" target="_blank"> Pitagoras Calculator</a> lhe responder se a condição de existência é verdadeira.</p>
        <p>O projeto conta com uma API - Pitagoras Calculator que pode ser requisitada com a URL: <a href="https://api-pitagoras.herokuapp.com/">https://api-pitagoras.herokuapp.com/ </a></p>
        <p>A API recebe os três lados enviados pelo usuário e realiza a verificação de existência do triângulo, seguindo o Teorema de Pitágoras.</p>
</div>
<div id="ferramentas">
    <h2>Ferramentas utilizadas: </h2>
    <div>
        <img src="./ferramentas.png">
    </div>
</div>
