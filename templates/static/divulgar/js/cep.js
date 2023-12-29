function buscaCep() {
        let cep = document.getElementById('txtCep').value;
        if(cep !== ""){
            let url = "https://brasilapi.com.br/api/cep/v2/" + cep;

            let req = new XMLHttpRequest();
            req.open("GET", url);
            req.send();

            req.onload = function () {
                if(req.status === 200){
                    let endereco = JSON.parse(req.response);
                    document.getElementById("txtRua").value = endereco.street;
                    document.getElementById("txtBairro").value = endereco.neighborhood;
                    document.getElementById("txtCidade").value = endereco.city;
                    document.getElementById("txtEstado").value = endereco.state;
                }
                else if(req.status === 404){
                    alert("Cep inválido");
                }
                else{
                    alert("erro ao fazer requisição");
                }
            }

        }

    }

    window.onload = function(){
        let txtCep = document.getElementById("txtCep");
        txtCep.addEventListener("blur", buscaCep);
    }
