@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Rowdies:wght@300&display=swap');
:root{
    --cor1: #2746D6;
    --cor2: #2879F0;
}
*{
    margin: 0;
    padding: 0;
    border: none !important;
    
}
@keyframes title {
    from{font-size: 0px}
    to{font-size: 40px;}
}
body{
    color: white;
    font-family: 'Rowdies', Helvetica, sans-serif;
    background-color: #007e97;
}

.header{
    width: 100%;
    height: 100px;
    display: flex;
    align-items: center;
    background-color: #074F57;
}
.header h1{
    margin-left: 10px;
    color: yellow;
    text-shadow: 1px 1px 2px  rgba(0, 0, 0, 0.658);
}

.fl-1{
    display: flex;
    justify-content: space-around;
    margin-top: 40px;
    color: #BFEDEF;

}
.fl-1 input{
    width: 300px;
    height: 40px;
    border-radius: 15px;
    border: none;
    outline: none;
}
.c-barras{
    box-shadow: 2px 2px 2px 3px rgba(0, 0, 0, 0.253);
}
.c-qt{
    box-shadow: 2px 2px 2px 3px rgba(0, 0, 0, 0.253);
}
.fl-1 section{
    display: flex;
    width: 300px;
    height: 100px;
    font-size: 1px;;
    justify-content: space-around;
    color: white;
    
}
.fl-1 label{
    font-size: 25px;

}
.fl-2{
    display: flex;
    align-items: center;
    justify-content: space-around;
    width: 100%;
    height: 50%;
}
.historico{
    width: 500px;
    height: 400px;
    
    background: white;
}
.info{
    width: 500px;
    height: 400px;
    border: 1px solid white;
    text-align: end;
}
.info label{
    font-size: 15pt;
}
.info div{
   
    width: 100%;
    height: 40px;
    background: white;
}
.produto{
    width: 200px;
    height: 400px;
    border: 1px solid white;
    display: flex;
    flex-direction: column;
    align-items: center;
}
.produto img{
    width: 100px;
    height: 100px;
    border: 1px solid white;
}
.vt{
    width: 90%;
    height: 40px;
    background: white;
    color: black;
    display: flex;
    align-items: center;
}
.fl-3{
    display: flex;
    align-items: center;
    justify-content: space-around;
    width: 100%;
    height: 20%;
    text-align: center;
}
.fl-3 div{
    display: flex;
    flex-direction: column;
}
.fl-3 div div{
    background: #0D4781;
    width: 500px;
    height: 100px;
    font-size: 20pt;
    display: flex;
    justify-content: center;
    padding-left: 20px;
    border-radius: 15px;
}