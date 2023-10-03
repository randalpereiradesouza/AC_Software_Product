document.addEventListener('DOMContentLoaded', function () {
   
   try{
    const form = document.getElementById('cadastro-form');
    const mensagem = document.getElementById('mensagem');
   
    form.addEventListener('submit', function (e) {
        e.preventDefault();

        const data = {
            nome: form.nome.value,
            cpf: form.cpf.value,
            email: form.email.value,
            endereco: form.endereco.value,
            contrato: form.contrato.value
        };

        fetch('/cadastrar_cliente', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(result => {
            mensagem.innerHTML = result.mensagem;
            form.reset();
        })
        .catch(error => {
            mensagem.innerHTML = 'Erro ao cadastrar/atualizar cliente.';
            console.error('Erro:', error);
        });
    });

   }
   catch{
    const formchamado = document.getElementById('chamado-form');
    const mensagemchamado = document.getElementById('mensagemchamado');
    
    formchamado.addEventListener('submit', function (e) {
        e.preventDefault();

        const data = {
            modelo: formchamado.modelo.value,
            defeito: formchamado.defeito.value,
            cpf: formchamado.cpf.value
        };

        fetch('/cadastrar_chamado', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(result => {
            mensagemchamado.innerHTML = result.mensagemchamado;
            formchamado.reset();
        })
        .catch(error => {
            mensagemchamado.innerHTML = 'Erro ao cadastrar chamado.';
            console.error('Erro:', error);
        });
    });
   }

});


