// Cadastro de Clientes
const formCliente = document.getElementById('formCliente');
if(formCliente){
    formCliente.addEventListener('submit', function(e){
        e.preventDefault();
        const nome = document.getElementById('nome').value;
        const email = document.getElementById('email').value;
        const telefone = document.getElementById('telefone').value;
        const endereco = document.getElementById('endereco').value;

        const tabela = document.getElementById('tabelaClientes').querySelector('tbody');
        const row = tabela.insertRow();
        row.insertCell(0).innerText = nome;
        row.insertCell(1).innerText = email;
        row.insertCell(2).innerText = telefone;
        row.insertCell(3).innerText = endereco;

        formCliente.reset();
    });
}

// Cadastro de Animais
const formAnimal = document.getElementById('formAnimal');
if(formAnimal){
    formAnimal.addEventListener('submit', function(e){
        e.preventDefault();
        const nome = document.getElementById('nomeAnimal').value;
        const tipo = document.getElementById('tipoAnimal').value;
        const raca = document.getElementById('raca').value;
        const idCliente = document.getElementById('idCliente').value;

        const tabela = document.getElementById('tabelaAnimais').querySelector('tbody');
        const row = tabela.insertRow();
        row.insertCell(0).innerText = nome;
        row.insertCell(1).innerText = tipo;
        row.insertCell(2).innerText = raca;
        row.insertCell(3).innerText = idCliente;

        formAnimal.reset();
    });
}

// Agendamento de Serviços
const formAgendamento = document.getElementById('formAgendamento');
if(formAgendamento){
    formAgendamento.addEventListener('submit', function(e){
        e.preventDefault();
        const idAnimal = document.getElementById('idAnimalAg').value;
        const servico = document.getElementById('servico').value;
        const data = document.getElementById('dataAg').value;

        const tabela = document.getElementById('tabelaAgendamentos').querySelector('tbody');
        const row = tabela.insertRow();
        row.insertCell(0).innerText = idAnimal;
        row.insertCell(1).innerText = servico;
        row.insertCell(2).innerText = data;

        formAgendamento.reset();
    });
}
