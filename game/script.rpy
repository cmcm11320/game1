# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Ellen",color="#FFC1D7")
define b = Character("Bastidores")
define yn = Character("[yn]")
define y = yn
define m = Character("Motorista")
define anon = Character("??",color="#fff")
define one = Character("[one]")
define two = Character("[two]")
define three = Character("[three]")
define four = Character("[four]")
define five = Character("[five]")
define six = Character("[six]")
define seven = Character("[seven]")
define eight = Character("[eight]")

define priya = Character("Priya")
define sanjit = Character("Sanjit")
define miya = Character("Miya")
define aoi = Character("Aoi")
define xiong = Character("Xiong")
define cheng = Character("Cheng")
define sasha = Character("Sasha")
define igor = Character("Igor")
define alice = Character("Alice")
define miguel = Character("Miguel")
define genevieve = Character("Geneviève")
define tristan = Character("Tristan")
define helena = Character("Helena")
define erick = Character("Erick")
define beatriz = Character("Beatriz")
define pedro = Character("Pedro")
define aiysha = Character("Aiysha")
define kondo = Character("Kondo")
define aiyla = Character("Aiyla")
define halil = Character("Halil")
image pink = "#FFC1D7"

default varbib = False
default varart = False
default vargame = False
default varpool = False

# images

# xiong
image xiong_normal = "/images/Characters/xiong_xue/normal.png"
image xiong_feliz = "/images/Characters/xiong_xue/feliz.png"
image xiong_confusa = "/images/Characters/xiong_xue/confusa.png"
image xiong_medo = "/images/Characters/xiong_xue/medo.png"
image xiong_neko = "/images/Characters/xiong_xue/neko.png"
image xiong_sexy = "/images/Characters/xiong_xue/sexy.png"
image xiong_apaixonada = "/images/Characters/xiong_xue/apaixonada.png"
image xiong_raiva = "/images/Characters/xiong_xue/raiva.png"

# alice
image alice_normal = "/images/Characters/alice_guerrero/normal.png"
image alice_feliz = "/images/Characters/alice_guerrero/feliz.png"
image alice_confusa = "/images/Characters/alice_guerrero/confusa.png"
image alice_medo = "/images/Characters/alice_guerrero/medo.png"
image alice_neko = "/images/Characters/alice_guerrero/neko.png"
image alice_sexy = "/images/Characters/alice_guerrero/sexy.png"
image alice_apaixonada = "/images/Characters/alice_guerrero/apaixonada.png"
image alice_raiva = "/images/Characters/alice_guerrero/raiva.png"

# ayisha
image ayisha_normal = "/images/Characters/ayisha_okoye/normal.png"
image ayisha_feliz = "/images/Characters/ayisha_okoye/feliz.png"
image ayisha_confusa = "/images/Characters/ayisha_okoye/confusa.png"
image ayisha_medo = "/images/Characters/ayisha_okoye/medo.png"
image ayisha_neko = "/images/Characters/ayisha_okoye/neko.png"
image ayisha_sexy = "/images/Characters/ayisha_okoye/sexy.png"
image ayisha_apaixonada = "/images/Characters/ayisha_okoye/apaixonada.png"
image ayisha_raiva = "/images/Characters/ayisha_okoye/raiva.png"

# beatriz
image beatriz_normal = "/images/Characters/beatriz_souza/normal.png"
image beatriz_feliz = "/images/Characters/beatriz_souza/feliz.png"
image beatriz_confusa = "/images/Characters/beatriz_souza/confusa.png"
image beatriz_medo = "/images/Characters/beatriz_souza/medo.png"
image beatriz_neko = "/images/Characters/beatriz_souza/neko.png"
image beatriz_sexy = "/images/Characters/beatriz_souza/sexy.png"
image beatriz_apaixonada = "/images/Characters/beatriz_souza/apaixonada.png"
image beatriz_raiva = "/images/Characters/beatriz_souza/raiva.png"

# genevieve
image genevieve_normal = "/images/Characters/genevieve_dubois/normal.png"
image genevieve_feliz = "/images/Characters/genevieve_dubois/feliz.png"
image genevieve_confusa = "/images/Characters/genevieve_dubois/confusa.png"
image genevieve_medo = "/images/Characters/genevieve_dubois/medo.png"
image genevieve_neko = "/images/Characters/genevieve_dubois/neko.png"
image genevieve_sexy = "/images/Characters/genevieve_dubois/sexy.png"
image genevieve_apaixonada = "/images/Characters/genevieve_dubois/apaixonada.png"
image genevieve_raiva = "/images/Characters/genevieve_dubois/raiva.png"

# helena
image helena_normal = "/images/Characters/helena_lawson/normal.png"
image helena_feliz = "/images/Characters/helena_lawson/feliz.png"
image helena_confusa = "/images/Characters/helena_lawson/confusa.png"
image helena_medo = "/images/Characters/helena_lawson/medo.png"
image helena_neko = "/images/Characters/helena_lawson/neko.png"
image helena_sexy = "/images/Characters/helena_lawson/sexy.png"
image helena_apaixonada = "/images/Characters/helena_lawson/apaixonada.png"
image helena_raiva = "/images/Characters/helena_lawson/raiva.png"

# priya
image priya_normal = "/images/Characters/priya_chaudhari/normal.png"
image priya_feliz = "/images/Characters/priya_chaudhari/feliz.png"
image priya_confusa = "/images/Characters/priya_chaudhari/confusa.png"
image priya_medo = "/images/Characters/priya_chaudhari/medo.png"
image priya_neko = "/images/Characters/priya_chaudhari/neko.png"
image priya_sexy = "/images/Characters/priya_chaudhari/sexy.png"
image priya_apaixonada = "/images/Characters/priya_chaudhari/apaixonada.png"
image priya_raiva = "/images/Characters/priya_chaudhari/raiva.png"

# sasha
image sasha_normal = "/images/Characters/sasha_petrova/normal.png"
image sasha_feliz = "/images/Characters/sasha_petrova/feliz.png"
image sasha_confusa = "/images/Characters/sasha_petrova/confusa.png"
image sasha_medo = "/images/Characters/sasha_petrova/medo.png"
image sasha_neko = "/images/Characters/sasha_petrova/neko.png"
image sasha_sexy = "/images/Characters/sasha_petrova/sexy.png"
image sasha_apaixonada = "/images/Characters/sasha_petrova/apaixonada.png"
image sasha_raiva = "/images/Characters/sasha_petrova/raiva.png"

# The game starts here.

label start:
    #Warning content
    scene pink
    
    $ renpy.movie_cutscene("/images/videos/content-warningfull.webm")

    # Episódio 0 - Introdução

    scene bg room
    scene pink

    "Você está em um local escuro"
    "Barulhos muito altos vem da unica abertura luminosa"
    "Você se aproxima da abertura"
    "Alguem encosta no seu braço e te diz"
    b "Ei, você vai entrar daqui a pouco, depois que chamarem seu nome"
    "Era um homem com uma blusa escrito bastidores"
    anon "Ah, desculpe, estou um pouco nervoso ainda"
    b "Tudo bem, eu entendo, mas você precisa esperar chamarem..."
    $ yn = renpy.input("Seu nome")
    $ yn = yn.strip()
    if yn == "Clara":
        "Você de novo... Sentimos sua falta..."

    menu: 
        "Eu sou:"

        "Homem":
            $ gender = 0

        "Mulher":
            $ gender = 1       


    b "você precisa esperar chamarem '[yn]', aí você vai entrar"
    yn "Ok!"
    b "Nervoso?"
    yn "Um pouco sim"
    b "É eu também estaria"
    e "E agora o bachelor deste ano... [yn]!!!"
    b "ggogogogo"
    "Você entra no palco e vê varias pessoas na plateia"
    "Você se senta na cadeira vazia perto da apresentadora"
    e "Pra quem vive debaixo da terra e ainda não conhece, [yn] vai ser o participante do programa 'Love Game' deste ano"
    e "ele vai ficar uma semana trancado em uma casa com 8 pessoas e vai decidir quem vai se casar!"
    e "então, [yn], você se identifica como o que?"
    menu:
        "Homossexual":
            $sexualidade = 0
        "Heterossexual":
            $sexualidade = 1
        "Bissexual":
            $sexualidade = 2

    if sexualidade==0:
        e "Amooo os gays, povo animado"
    elif sexualidade==1:
        e "legal"
    elif sexualidade == 2:
        e "Adoroo, indecisa, sou"
    
    e "Então, fale mais sobre você!"

    menu:
        "Eu sou uma pessoa..."
        "Calma, gosto de tranquilidade":
            $personalidade = 0
        "Divertida, gosto de festas e rir muito":
            $personalidade = 1
        "Romântica, adoro pensar na vida":
            $personalidade = 2
    e "Uau... Agora me fale, qual seu animal preferido?"

    menu:
        "Gatos!":
            $animal = 0
        "Cachorros!":
            $animal = 1
        "Pássaros":
            $animal = 2

    "A apresentação continua..."
    e "isso ai galera! esse foi [yn], amanha ele vai estar na casa e vamos conhecer os outros candidatos que vão tentar roubar o coracao dele, eu sou a Ellen, boa tarde"
    "vocês vão para os bastidores"
    e "Você foi bem! O público te adorou"
    y "Obrigado..."
    e "Você deve estar nervoso com amanhã, mas se te faz sentir melhor"
    e "Todos os candidatos dos últimos anos encontraram seus esposos no programa, temos uma taxa de 100 porcento de aprovação"
    y "é, isso ajuda um pouco"
    e "Bom, até semana que vem, quando você sair do programa quero ser a primeira a entrevistar você e sua futura esposa...."
    y "haha até"

    # Episódio 1 - O primeiro dia

    "Você acorda de manhã, se arruma e sai do quarto"
    "Fora do prédio um carro está à espera"
    m "Olá, pode entrar"
    "Você está no carro e observando o ambiente à sua volta"
    "As árvores começam a atrapalhar a visão, até que você não sabe mais onde está"
    "Mas sabe que é longe, você sabe que está indo para um lugar e não será facil de voltar"
    "Seu celular foi retirado de você, e  após o que pareceu horas, você chega em um grande portão"
    "O motorista abre o portão com um sistema de segurança forte"
    m "Basicamente, só eu sei onde estamos e só eu posso abrir esse portão"
    "Creepy... Mas faz sentido, o prédio precisa ser à prova de invasões"
    "Nas edições passadas, um fã entrou na casa e contou a todos os integrantes o que acontecia do lado de fora e foi um inferno"
    "ENtão eles  precisaram tomar mais precauções esse ano"
    "Uma delas é que o programa não é mais ao vivo"
    "os 7 dias são gravados e ninguém de fora entra ou sai do programa e nem tem contato com os integrantes"
    "Assim que o programa acaba, eles entram na casa e recuperam as gravações"
    "Mas calma, não ficaremos totalmente sozinhos lá"
    "Um médico, um bombeiro e um técnico ficam os 7 dias em uma cabine separada, mas só podemos entrar em contato com eles em caso de emergência"
    m "Chegamos... Bem vindo a sua nova casa por 7 dias"
    "Uau, a casa é linda"
    "Uma mansão enorme com 9 quartos, uma grande piscina, uma cozinha imensa... Uau!"
    y "Agora eu me lembrei pq eu me inscrevi nesse show"
    m "Sim... QUeria eu poder passar um tempo aqui"
    m "E ainda achar o amor da minha vida... Uau... É o sonho"
    m "Você não sabe a sorte que tem de estar aqui"
    y "É... EU tinha me esquecido do paraíso que é aqui"
    "Você sai do carro e o motorista pega suas malas e instala você no seu quarto"
    "Um quarto lindo, com uma cama enorme e uma decoração maravilhosa"
    m "É isto, está instalado, agora vou me retirar"
    y "Deixa eu te acompanhar até a porta"
    m "Nossa, muito gentil da sua parte, obrigado"
    "Você desce com ele, até que ele entra no carro"
    m "Bom... Até a semana que vem... Boa sorte!"
    "Você observa o motorista dirigir até o portão e o observa fechar atras do carro"
    "É um portão alto e impenetrável, e a unica forma de abri-lo é com a identificação ocular e a senha"
    y "É... Eu não poderia sair daqui nem se eu tentasse"
    "Você volta para o quarto, todos os integrantes da casa devem ficar no quarto até todos chegarem"
    "Você era o último a chegar, então assim que o alarme do dia tocar, vocês todos devem sair e se encontrar na sala"
    "o alarme toca"
    y "Bom... Hora de conhecer o amor da minha vida..."
    
    # if sexualidade==0:
    #     #rota gay
    # if sexualidade==1:
    #     #rota hetero
    # if sexualidade==2:
    #     #rota bi

    "Você desce para a sala, com o coração na mão"

    label primeiro_menu:
    if varart and vargame and varpool and varbib: 
        jump choice_scene
    menu:            
        "Biblioteca" if not varbib:
            $varbib = True
            jump biblioteca_0

        "Sala de Jogos" if not vargame:
            $vargame = True
            jump jogos_0

        "Piscina" if not varpool:
            $varpool = True
            jump piscina_0

        "Sala de Artes" if not varart:
            $varart = True
            jump arte_0


    label biblioteca_0:
    
    "Você entra na casa e vai até a biblioteca"
    "Você entra em um quarto cheio de livros do chão ao teto"
    show sasha_normal
    "Sentada em um dos sofás dessa sala está uma mulher sentada lendo um livro"
    y "Oi... Tudo bem?"
    "A mulher olha para você"
    anon "Olá"
    y "Eai, o que você está lendo?"
    anon "Como fazer amigos e influenciar pessoas"
    y ".... Vc é coach?"
    anon "Não, to brincando, to lendo o Vade Mecum, eu sou advogada"
    "Não sei oq é pior..."
    y "Legal... Qual seu nome?"
    sasha "Sasha Petrova, e você é [yn] o competidor desse ano"
    y "bingo"
    sasha "Legal, vamos conviver muito esses próximos 7 dias"
    y "legal"
    hide sasha_normal
    jump primeiro_menu

    label jogos_0:
  
    "Você vai até a sala de jogos"
    "Você entra no quarto e encontra duas mulheres"
    show alice_feliz at right
    show genevieve_normal at left
    anon "Porra perdi de novo"
    anon "Haha!"
    y "Olá pessoal"
    show alice_normal at right
    hide alice_feliz
    anon "eae"
    anon "Você é [yn] certo?"
    y "Isso mesmo"
    genevieve "Eu sou Geneviève Dubois"
    alice "Eu sou Alice Guerrero"
    y "Muito prazer"
    hide alice_normal
    hide genevieve_normal
    jump primeiro_menu

    label piscina_0:
   
    "Você vai até a área da piscina que existe do lado de fora da casa"
    "É uma área grande, com uma linda piscina e uma área de churrasco"
    "Você encontra duas mulheres na piscina e uma tomando sol nas cadeiras"
    show priya_normal at right
    show helena_normal at left
    show beatriz_normal at center
    anon "AAAA"
    anon "Joga agua nelaa kkk"
    y "Oi pessoal"
    anon "Olá!"
    y "Eu sou..."
    anon "Eu sei quem vc é..."
    y "..."
    anon "Você é [yn] o competidor"
    y "Isso mesmo, e vocês são..."
    helena "Eu sou Helena"
    beatriz "Eu sou Beatriz"
    priya "Eu sou Priya"
    y "prazer"
    hide priya_normal
    hide helena_normal
    hide beatriz_normal

    jump primeiro_menu

    label arte_0:
    
    "Você vai ao segundo andar da casa onde existe uma sala de artes"
    "Entrando na sala existe duas mulheres conversando"
    show xiong_normal at left
    show ayisha_normal at right
    anon "Eu adoro pintar lalalala"
    anon "muito foda"
    y "Oi pessoal"
    anon "Olá, você deve ser [yn]"
    anon "Eai"
    xiong "Oi eu sou Xiong Xuè"
    aiysha "Eu sou Aiysha Okoye"
    hide xiong_normal
    hide ayisha_normal

    jump primeiro_menu

    label choice_scene:

    #Conhecer todos
    "Depois de conhecer todas, você vai até a sala principal e todas já estão lá"
    "O relógio toca mostrando que você precisa escolher uma delas para ir em um encontro naquele dia"
    menu:
        "Quem eu escolho?"

        "Xiong":
            jump date_0_xiong
        "Sasha":
            jump date_0_sasha
        "Geneviève":
            jump date_0_genevieve
        "Alice":
            jump date_0_alice
        "Helena":
            jump date_0_helena
        "Priya":
            jump date_0_priya
        "Beatriz":
            jump date_0_beatriz
        "Ayisha":
            jump date_0_ayisha

    #Primeiro Encontro
    label date_0_xiong:
    $ primeirolove = "Xiong"
    "[primeirolove]!"

    jump noite_0
    
    label date_0_sasha:
    $ primeirolove = "Sasha"
    "[primeirolove]!"

    jump noite_0

    label date_0_genevieve:
    $ primeirolove = "Geneviève"
    "[primeirolove]!"

    jump noite_0
    
    label date_0_alice:
    $ primeirolove = "Alice"
    "[primeirolove]!"

    jump noite_0

    label date_0_helena:
    $ primeirolove = "Helena"
    "[primeirolove]!"

    jump noite_0

    label date_0_priya:
    $ primeirolove = "Priya"
    "[primeirolove]!"

    jump noite_0

    label date_0_beatriz:
    $ primeirolove = "Beatriz"
    "[primeirolove]!"

    jump noite_0

    label date_0_ayisha:
    $ primeirolove = "Ayisha"
    "[primeirolove]!"

    jump noite_0



    label noite_0:
    #A noite...

    "Após o date com [primeirolove] você está deitado na cama, feliz com o que aconteceu"
    y  "Uau... Eu estou mesmo apaixonado depois de um primeiro encontro? Hahah"
    "Você está tão ansioso que não consegue pegar no sono"
    "Quando você está quase pegando no sono, você escuta um barulho vindo do andar debaixo"
    y "Hm, deve ser algum animal, nada demais"
    "Mas o barulho continua na sua cabeça"
    "Você está com sede"
    y "Acho que vou pegar uma água, aproveito e vejo o que é esse barulho"
    "Você desce as escadas, chega a cozinha, pega um copo de água"
    "Você escuta outro barulho vindo da biblioteca"
    "Você decide ir ver o que é"
    "Você vai em silêncio até o quarto"
    "A porta está entreaberta"
    "Você abre a porta do quarto"
    #imagem da morte
    y "Não... Não..."
    y "NÃÃÃO"
    "Você grita, acordando todo mundo"
    one "MEU DEUS O QUE ACONTECEU?"
    two "O QUE É ISSO!"
    three "Eu estou ficando enjoada......"
    "[three] vai no banheiro vomitar"
    "Você est;a paralizado, não sabe o que fazer"
    y "Eu não acredito... O que aconteceu?"
    four "Vamos chamar o médico, qualquer um, olhar as cameras"
    y "Vamos"
    "Você e [four] vão até a van que fica no meio da floresta onde ficam os outros"
    four "Alô!!!! Precisamos de ajuda!!!"
    "[four] bate na porta da van, até que a porta se abre"
    "Vocês entram na van"
    #morte dos produtores 
    y "Não... Isso não está acontecendo"
    four "Olha na camera! Vê se gravaram o que aconteceu"
    "Você checa as gravações, tudo foi quebrado, tudo foi perdido"
    y "Não Não, precisa ter gravado alguma coisa, precisa ter alguma coisa funcionando"
    y "Vê se eles tem celular, qualquer coisa, pra pedirmos ajuda"
    four "EU não quero encostar neles"
    y "Eu também não, mas precisamos pedir ajuda!"
    "Você procura nos bolsos deles... Nada..."
    y "Eles deixam os celulares fora, pra ninguem ter contato dentro da casa..."
    four "Eu não acredito nisso.... Eu não acredito que isso está acontecendo...."
    "Vocês voltam pra casa e contam a todas o que está acontecendo"
    five "ENtão... Estamos presos aqui... Com um assassino?"
    seven "Você não sabe se isso é realmente o que aconteceu"
    five "É claro que é isso! Ninguem consegue entrar aqui, nem sair, estamos presos com a pessoa que matou [primeirolove]" 
    y "Nào... Isso não está acontecendo..."
    six "está... E nós podemos ser os proximos...."
    seven "precisamos descobrir quem de nós fez isso, deixar essa pessoa presa até o final dos 7 dias, quando eles vão vir nos buscar"
    seven "pra nossa proteção..."
    y "e como vamos descobrir quem fez isso?"
    four "precisamos investigar, procurar pistas"
    y "Certo... Vamos fazer isso..."
    menu:
        "Onde vou investigar primeiro?"

        "Na biblioteca":
            jump biblioteca_1
        "Na sala de jogos":
            jump game_1
        "Na cozinha":
            jump cozinha_1
        



    label biblioteca_1:
    
    four "Também estou indo para lá, vamos procurar pistas juntos"
    "Vocês vão para a biblioteca, onde o corpo de [primeirolove] está"
    "Você chega mais perto do corpo, "







    # This ends the game.

    return
