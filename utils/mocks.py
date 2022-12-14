conta_cliente_mockada = {
    "username": "erick",
    "password": "1234",
    "email": "user1@email.com",
    "first_name": "erick",
    "last_name": "marchetti",
    "is_employee": False,
    "data_nascimento": "2003-04-28",
    "cpf": "36593551007",
    "telefone": "994568321",
    "pontos_de_fidelidade": 0,
}

usuario_comum_login = {"username": "erick", "password": "1234"}

conta_funcionario_mockada = {
    "username": "erick funcionario",
    "password": "1234",
    "email": "user2@email.com",
    "first_name": "erick",
    "last_name": "funcionario",
    "is_employee": True,
    "data_nascimento": "2003-04-28",
    "cpf": "36593551008",
    "telefone": "994568321",
    "pontos_de_fidelidade": 0,
}

usuario_funcionario_login = {"username": "erick funcionario", "password": "1234"}

conta_adm_mockada = {
    "username": "adm",
    "password": "1234",
    "email": "user3@email.com",
    "first_name": "adm",
    "last_name": "é um adm",
    "is_employee": False,
    "data_nascimento": "2003-04-28",
    "cpf": "36593551009",
    "telefone": "994568321",
    "pontos_de_fidelidade": 0,
}

usuario_adm_login = {"username": "adm", "password": "1234"}

usuario_funcionario = {
    "username": "jorge",
    "password": "1234",
    "email": "user4@email.com",
    "first_name": "jorge",
    "last_name": "junior",
    "telefone": "99999999999",
    "cpf": "09596815075",
    "data_nascimento": "1997-01-01",
    "endereco": {
        "rua": "Rua rau ruau",
        "numero": "50",
        "complemento": "bloco 20",
        "cidade": "Belo horizonte",
        "estado": "Minas Gerais",
        "ponto_de_referencia": "Proximo ao aviário 101",
    },
}

usuario_comum = {
    "username": "patrick",
    "password": "1234",
    "email": "user5@email.com",
    "first_name": "patrick",
    "last_name": "junior",
    "telefone": "99999999999",
    "cpf": "32361236052",
    "data_nascimento": "1999-01-01",
    "endereco": {
        "rua": "Rua sim",
        "numero": "50",
        "complemento": "bloco 50",
        "cidade": "Paraná",
        "estado": "Curitiba",
        "ponto_de_referencia": "Proximo ao kilão verduras frescas",
    },
}

endereco_mockado = {
    "rua": "Avenida Brasil",
    "numero": "2256",
    "complemento": "Apartamento 502",
    "cidade": "Bauru",
    "estado": "SP",
    "ponto_de_referencia": "Ao lado do Boteco do Marcinho",
}

produto_mockado = {
    "preco": 10.50,
    "nome": "Bolo de Chocolate",
    "imagem": "só testando",
    "descricao": "Um delicioso bolo de chocolate com morangos.",
}

coxinha_mockada = {
    "categoria": {"nome": "fritura"},
    "preco": 5.00,
    "nome": "Coxinha de Frango",
    "imagem": "https://www.fomitasgourmet.com.br/arquivos/LoginID_321/Blog/receita-tradicional-de-coxinha-1729.jpg",
    "descricao": "Coxinha de frango com catupiry.",
    "estoque": {"quantidade": 5},
}

categoria_mockada = {"nome": "categoria mockada"}
