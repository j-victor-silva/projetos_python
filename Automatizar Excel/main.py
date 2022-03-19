"""
Esse programa foi pensado para fazer primeiramente automações básicas
para o Excel, já que eu fazia muitas coisas usando ele
O programa vai basicamente copiar coisas que são muito usadas para as células do Excel
"""
import funcoes as func


# Objetivos
objetivos = {
    'EI03EF01CRU': 'Expressar ideias, desejos e sentimentos sobre suas vivências, por meio da linguagem oral e escrita',
    'EI03CG05CRU': 'Coordenar suas habilidades manuais no atendimento adequadro a seus interesses e necessidades',
    'EI03TS02CRU': 'Expressar-se livremente por meio de desenhos, pintura e colagem',
    'EI03ET07CRU': 'Relacionar números a suas respectivas quantidades',
    'EI03CG03CRU': 'Criar movimentos, gestos, olhares e mímicas em brincadeiras, jogos e atividades artísticas como: dança, teatro e música voltadas para a exploração e valorização da cultura regional, local',
    'EI03CG02CRU': 'Demonstrar controle e adequação do uso de seu corpo em brincadeiras, jogos, escuta e reconto de histórias, atividades artísticas e culturais',
    'EI03EF06CRU': 'Produzir suas próprias histórias orais e escritas (escrita espontânea), em situação com função social significativa',
    'EI03TS01CRU': 'Utilizar sons produzidos por materiais, objetos e instrumentos musicais durante brincadeiras de faz de conta',
    'EI03ET03CRU': 'Identificar e selecionar fontes de informações, para responder a questões sobre a natureza',
    'EI03CG05CRU': 'Coordenar suas habilidades manuais no atendimento',
    'EI03ET01CRU': 'Estabelecer relações de comparação entre objetos, observando suas propriedades',
}

func.copiar_colar(objetivos, 'EI03TS01CRU')