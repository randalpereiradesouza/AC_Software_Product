document.addEventListener('DOMContentLoaded', function () {
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
});
