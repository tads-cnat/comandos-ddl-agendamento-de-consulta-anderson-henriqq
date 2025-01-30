import psycopg2

# Conectar ao banco de dados PostgreSQL
conn = psycopg2.connect(
    dbname="seu_banco_de_dados",
    user="postgres",
    password="postgres",
    host="localhost",  
    port="5432"  
)


cur = conn.cursor()

criar_tabela_pessoa = """
    CREATE TABLE Pessoa (
        cpf CHAR(11) PRIMARY KEY,               
        email VARCHAR(50) NOT NULL,               
        nome VARCHAR(150) NOT NULL,               
        data_nasc DATE NOT NULL,                  
        endereco VARCHAR(300) NOT NULL,          
        telefone VARCHAR(15),                     
        CONSTRAINT unique_1 UNIQUE (email, nome)  
);
    """

create_tabela_paciente = """
    CREATE TABLE IF NOT EXISTS Paciente (
        cpf_pessoa CHAR(11) PRIMARY KEY,
        senha VARCHAR(20) NOT NULL,
        plano_saude BOOLEAN NOT NULL DEFAULT FALSE,
        CONSTRAINT fk_pessoa FOREIGN KEY (cpf_pessoa) REFERENCES Pessoa(cpf)
    );
    """

create_tabela_medico = """
    CREATE TABLE IF NOT EXIT Medico(
        cpf_pessoa CHAR(11) PRIMARY KEY
        CONSTRAINT unique_crm UNIQUE (crm) 
        CONSTRAINT fk_pessoa FOREIGN KEY (cpf_pessoa) REFERENCES Pessoa(cpf)
    );
    """

create_tabela_agendamento = """
    CREATE TABLE IF NOT EXISTS Agendamento (
        cpf_paciente CHAR(11),
        cpf_medico CHAR(11),
        dh_consulta TIMESTAMP,
        dh_agendamento TIMESTAMP NOT NULL,
        valor_consulta FLOAT NOT NULL DEFAULT 0.0,
        PRIMARY KEY (cpf_paciente, cpf_medico, dh_consulta),
        CONSTRAINT fk_paciente FOREIGN KEY (cpf_paciente) REFERENCES Paciente(cpf_pessoa),
        CONSTRAINT fk_medico FOREIGN KEY (cpf_medico) REFERENCES Medico(crm)
    );
    """

create_tabela_especialidade = '''
    CREATE TABLE IF NOT EXISTS Especialidade (
        id SERIAL PRIMARY KEY,
        descricao VARCHAR(300) NOT NULL
    );
    '''
    
    
create_tabela_medico_especialidade = '''
    CREATE TABLE IF NOT EXISTS Medico_Especialidade (
        cpf_medico CHAR(11),
        id_especialidade INT,
        PRIMARY KEY (cpf_medico, id_especialidade),
        CONSTRAINT fk_medico FOREIGN KEY (cpf_medico) REFERENCES Medico(crm),
        CONSTRAINT fk_especialidade FOREIGN KEY (id_especialidade) REFERENCES Especialidade(id)
    );
    '''


cur.execute(criar_tabela_pessoa)
cur.execute(create_tabela_paciente)
cur.execute(create_tabela_medico)
cur.execute(create_tabela_agendamento)
cur.execute(create_tabela_especialidade)
cur.execute(create_tabela_medico_especialidade)


conn.commit()

cur.close()

conn.close()
