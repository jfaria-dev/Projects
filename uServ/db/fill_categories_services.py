
import mysql.connector
from mysql.connector import Error

# Configurações do banco de dados
config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'db_userv'
}

# Dados dos serviços categorizados
serv_categories = {
    'Serviços Residenciais e Manutenção': {
        'Jardineiro': [
            'Visita',
            'Poda de árvores e arbustos', 
            'Manutenção de gramados', 
            'Paisagismo e design de jardins', 
            'Instalação de sistemas de irrigação', 
            'Fertilização e tratamento do solo'
            ],  
        'Manutenção e instalação de ar condicionado': [
            'Visita',
            'Instalação de aparelhos de ar condicionado',
            'Manutenção preventiva e corretiva',
            'Limpeza de filtros e dutos',
            'Recarga de gás refrigerante',
            'Diagnóstico e reparo de falhas',
            ],
        'Montador de móveis': [
            'Visita',
            'Montagem de móveis novos',
            'Desmontagem de móveis para mudança',
            'Ajustes e reparos em móveis',
            'Instalação de prateleiras e suportes',
            ],
        'Eletricista': [
            'Visita',
            'Instalação elétrica residencial e comercial',
            'Reparos em fiação elétrica',
            'Instalação de disjuntores e quadros de luz',
            'Manutenção de sistemas elétricos',
            'Inspeção e conformidade com normas de segurança',
            ],
        'Encanador': [
            'Visita',
            'Reparo de vazamentos',
            'Desentupimento de canos',
            'Instalação e manutenção de torneiras e chuveiros',
            'Manutenção de sistemas de esgoto',
            'Instalação de sistemas de aquecimento de água',
            ],
        'Pedreiro': [
            'Visita',
            'Construção de muros e paredes',
            'Reboco e acabamento',
            'Assentamento de pisos e azulejos',
            'Reparos estruturais',
            'Construção e reforma de edificações',
            ],
        'Pintor': [
            'Visita',
            'Pintura interna e externa de imóveis',
            'Preparação de superfícies',
            'Aplicação de vernizes e texturas',
            'Pintura decorativa',
            'Remoção de papel de parede',
            ],
        'Diarista': [
            'Visita',
            'Limpeza geral de residências',
            'Limpeza de escritórios e espaços comerciais',
            'Lavagem de janelas',
            'Organização de ambientes',
            'Limpeza pós-obra',
            ],
    },
    'Serviços de Transporte e Logística': {
        'Transporte de mudanças':[
            'Visita',
            'Transporte residencial',
            'Transporte comercial',
            'Serviços de embalagem',
            'Desmontagem e montagem de móveis',
            'Armazenagem temporária',
            ],
        'Guincho':[
            'Visita',
            'Reboque de veículos avariados ou acidentados',
            'Remoção de veículos estacionados irregularmente',
            'Transporte de veículos para longas distâncias',
            'Auxílio em pane seca ou bateria descarregada',
            ],
        },
    'Serviços de Beleza e Cuidados Pessoais': {
        'Manicure e pedicure':[
            'Visita',
            'Corte e modelagem de unhas',
            'Aplicação de esmaltes e decorações',
            'Tratamentos para cutículas',
            'Hidratação das mãos e pés',
            'Aplicação de unhas postiças ou em gel',
            ],
        'Cabeleireira/Barbeiro':[
            'Visita',
            'Corte de cabelo feminino e masculino',
            'Coloração e mechas',
            'Tratamentos capilares',
            'Escovação e penteados',
            'Barba e bigode',
            ],
        },
    'Saúde e Bem-Estar': {
        'Fisioterapeuta':[
            'Visita',
            'Reabilitação física',
            'Terapia manual',
            'Exercícios terapêuticos',
            'Fisioterapia respiratória',
            'Pilates clínico',
            ],
        'Massoterapeuta':[
            'Visita',
            'Massagem relaxante',
            'Massagem terapêutica',
            'Drenagem linfática',
            'Massagem desportiva',
            'Reflexologia',
        ],
        'Dentista':[
            'Visita',
            'Limpeza dentária profissional',
            'Restaurações e tratamento de cáries',
            'Tratamentos de canal',
            'Ortodontia',
            'Implantes dentários',
        ],
        'Médico':[
            'Visita',
            'Consultas gerais e especializadas',
            'Prescrição de tratamentos',
            'Exames de diagnóstico',
            'Acompanhamento e gestão de doenças crônicas',
           ' Aconselhamento de saúde preventiva',
        ],
        'Personal Trainer':[
            'Visita',
            'Treinamento personalizado',
            'Avaliação física',
            'Planejamento de treinos',
            'Acompanhamento em academia',
            'Treinos específicos para objetivos variados',
        ],
        'Nutricionista':[
            'Visita',
            'Planos alimentares personalizados',
            'Avaliação nutricional',
            'Acompanhamento de dietas',
            'Educação nutricional',
            'Consultoria em nutrição esportiva',
        ],
        'Psicólogo':[
            'Visita',
            'Psicoterapia individual',
            'Terapia de casal ou familiar',
            'Avaliação psicológica',
            'Orientação vocacional',
            'Terapias de grupo',
            ],        
        },
    'Educação e Treinamento': {
        'Professor Particular':[
            'Visita',
            'Aulas de reforço escolar',
            'Preparação para exames e concursos',
            'Aulas de idiomas',
            'Aulas de música',
            'Tutoria educacional personalizada',
            ]
        },
    'Serviços Automotivos': {
        'Borracharia':[
            'Visita',
            'Troca de pneus',
            'Reparos em pneus furados',
            'Alinhamento e balanceamento',
            'Calibragem de pneus',
            'Serviços de vulcanização',
            ],
        'Mecânico':[
            'Visita',
            'Manutenção automotiva geral',
            'Reparos de motor',
            'Troca de óleo e filtros',
            'Diagnóstico e reparo de sistemas eletrônicos',
            'Revisão preventiva',
            ],
        },
    'Gastronomia e Eventos': {
        'Cozinheiro particular':[
            'Visita',
            'Preparo de refeições diárias',
            'Serviços de chef em eventos',
            'Aulas de culinária',
            'Planejamento de cardápios saudáveis',
            'Consultoria gastronômica',
            ]
        },
    'Arquitetura, Design e Decoração': {
        'Arquiteto/Decorador':[
            'Visita',
            'Design de interiores',
            'Planejamento arquitetônico',
            'Supervisão de obras',
            'Consultoria em decoração',
            'Projetos paisagísticos',
            ]
        },
    'Serviços Domésticos e Cuidados Pessoais': {
        'Babá': [
            'Visita',
            'Cuidados diários com crianças',
            'Acompanhamento de atividades escolares',
            'Preparação de refeições',
            'Atividades lúdicas e educativas',
            'Apoio em rotinas diárias',
            'Cuidado com crianças em eventos específicos',
            'Acompanhamento de crianças em atividades extracurriculares',
            'Assistência em viagens familiares',
            'Cuidados especiais para crianças com necessidades especiais',
            'Primeiros socorros e cuidados de emergência',
            ],
        'Lavagem e passagem de roupas': [
            'Visita',
            'Lavagem a seco e a água',
            'Passadoria de roupas',
            'Tratamento de manchas',
            'Serviço de lavanderia para roupas delicadas',
            'Dobragem e organização de roupas',
            'Serviço de coleta e entrega de roupas',
            'Lavagem de itens especiais, como vestidos de noiva ou ternos',
            'Serviços de tingimento de tecidos',
            'Conservação e restauração de roupas antigas ou delicadas',
            ],
        },
    'Tecnologia e Comunicação':{
        'Serviços de informática':[
            'Visita',
            'Manutenção de computadores e notebooks',
            'Remoção de vírus e malwares',
            'Instalação de software',
            'Configuração de redes',
            'Suporte técnico remoto ou presencial',
            'Diagnóstico e reparo de hardware',
            'Recuperação de dados perdidos ou apagados',
            'Configuração de backup e armazenamento em nuvem',
            'Assistência em upgrades de sistema',
            'Consultoria em segurança da informação',
            ],
        'Design Gráfico':[
            'Visita',
            'Criação de logotipos e identidade visual',
            'Layout de materiais impressos',
            'Design de embalagens',
            'Ilustrações e animações',
            'Edição de imagens',
            'Criação de material para redes sociais',
            'Desenvolvimento de layouts para websites',
            'Criação de material promocional, como flyers e banners',
            'Branding e rebranding para empresas',
            'Diagramação de livros, revistas e e-books',
            ],
        'Desenvolvedor de website':[
            'Visita',
            'Criação de sites responsivos',
            'Manutenção e atualização de sites',
            'Otimização SEO',
            'Integração com redes sociais',
            'Desenvolvimento de e-commerce',
            'Criação de sistemas de gerenciamento de conteúdo (CMS)',
            'Programação back-end e front-end',
            'Desenvolvimento de aplicativos web',
            'Integração com sistemas de pagamento',
            'Suporte e treinamento para a gestão do site',
            'Desenvolvimento de aplicativos para celular',
            ],
        'Design ':[
            'Visita',
            'Criação de gráficos e infográficos',
            'Visualização de dados',
            'Design para relatórios e apresentações',
            'Produção de conteúdo visual para mídias sociais',
            'Animação gráfica',
            'Criação de layouts para jogos e aplicativos',
            'Design de interface de usuário (UI) e experiência do usuário (UX)',
            'Produção de conteúdo para realidade virtual (VR) e realidade aumentada (AR)',
            'Desenvolvimento de identidade visual para eventos e campanhas',
            'Criação de storyboards para produções audiovisuais',
            ],
        },
    'Cuidados com Animais de Estimação':{
        'Serviços de saúde': [
            'Visita',
            'Banho e tosa',
            'Vacinação',
            'Vermifugação',
            'Castração',
            'Consultas veterinárias',
            ],
        'Serviços de bem-estar': [
            'Visita',
            'Alimentação',
            'Acessórios',
            'Hospedagem',
            'Treinamento',
            ],
        'Serviços adicionais': [
            'Visita',
            'Day care',
            'Grooming',
            'Pet sitting',
            'Pet taxi',
            ]
        },
}

# Conectar ao banco de dados
conn = mysql.connector.connect(**config)
try:

    # Criar cursor
    cursor = conn.cursor()   
        
    # Inserir dados 
    for master, categorias in serv_categories.items():
        # Inserir categoria master         
        cursor.execute(f'INSERT INTO category (name, active) VALUES ("{master}", True)')
        
        # Get the ID of the newly inserted master category
        cursor.execute('SELECT LAST_INSERT_ID()')
        master_id = cursor.fetchone()[0]
        for cat_filha, servicos in categorias.items():
            # Inserir categoria filha            
            cursor.execute(f'INSERT INTO category (name, parent_id, active) VALUES ("{cat_filha}", {master_id}, True)')
            cursor.execute('SELECT LAST_INSERT_ID()')
            cat_filha_id = cursor.fetchone()[0]                  
            for s in servicos:
                # Inserir servico                            
                cursor.execute(f'INSERT INTO general_service (description, category_id) VALUES ("{s}", {cat_filha_id})')

    # Commitar as alterações
    conn.commit()

    # Fechar a conexão
    conn.close()

except Error as e:
    # Rollback em caso de erro
    conn.rollback()
    print("Erro ao inserir os serviços:", e)

finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("Conexão ao MySQL foi encerrada.")



