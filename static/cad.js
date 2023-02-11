window.addEventListener('load',function load(){
    const senha = prompt('Senha De Acesso')

    if(senha != 'adm'){
       
        window.location.replace("/");
    }
    else{
        alert('Seja Bem Vindo')
    }
})
