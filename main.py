from login import create_api
import random
import tweepy
import logging
import time
import base64
jogos = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
p2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] # Se p2 = 1 o jogo é contra o BOT  
turno = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
A1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
A2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
A3 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
B1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
B2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
B3 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
C1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
C2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
C3 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
emojis = ["\U000025FB","\U0000274C","\U00002B55"] # Vazio / Xis / Bola #
xis = "\U0000274C"
bola = "\U00002B55"
vazio = "\U000025FB"
vs = "\U0001F19A"

def check_mentions(api, since_id):
    newGame = True
    new_since_id = since_id
    for tweet in tweepy.Cursor(api.mentions_timeline, since_id = since_id).items(5):
        if api.get_status(tweet.id).favorited == False:
            if "|" in tweet.text:
                api.create_favorite(tweet.id)
                print("Tweet de criação de jogo, ignorando")
                return new_since_id
            print("\n\n\n\nTweet não respondido encontrado, ID: ", tweet.id)
            counter = 0
            for user in jogos:
                if user == tweet.user.id:
                    newGame = False
                    break
                counter = counter+1
            if newGame == True:
                counter2 = 0
                for user in p2:
                    if user == tweet.user.id:
                        newGame = False
                        break
                    counter2 = counter2 + 1
                if newGame == False:
                    counter = counter2
            if newGame == True:
                # Começar um novo jogo
                print("Criando um novo jogo para ", tweet.user.screen_name)
                controlador = 0
                for ids in jogos:
                    if ids == 0:
                        break;
                    controlador = controlador+1
                    if controlador == len(jogos):
                        break
                new_txt = tweet.text.replace("@VelhaBOT","")
                new_txt = new_txt + " "
                y = 0
                inicio = 0
                final = 0
                other_player = ""
                for x in new_txt:
                    if x == "@":
                        inicio = y+1
                    if inicio != 0 and x == " ":
                        final = y
                        break
                    y = y+1
                if inicio != 0:
                    other_player = new_txt[inicio:final]
                    print("Segundo jogador encontrado: ", other_player)
                    p2[controlador] = api.get_user(other_player).id
                else:
                    print("Segundo jogador não encontrado, o bot ira assumir controle")
                    p2[controlador] = 1
                    other_player = "BOT"
                jogos[controlador] = tweet.user.id
                limparVariaveis(controlador)
                print("Jogo registrado no slot ", controlador)
                api.create_favorite(tweet.id)
                api.update_status(
                    status= "@" + tweet.user.screen_name + " " + tweet.user.screen_name + "(" + xis + ")   " + vs + "   " + other_player + "(" + bola + ")\n\n"
                    + vazio + "|" + vazio + "|" + vazio + "                 A1 | A2 | A3\n"
                    + vazio + "|" + vazio + "|" + vazio + "                 B1 | B2 | B3\n"
                    + vazio + "|" + vazio + "|" + vazio + "                 C1 | C2 | C3\n\n"
                    + "Vez de " + tweet.user.screen_name + ", para jogar responda esse tweet com o formato: @VelhaBOT A1 (sendo A1 a coordenada para a jogada)",
                    in_reply_to_status_id=tweet.id,
                )
            else:
                pular = False
                # Continuar um jogo
                print("continuando o jogo do slot: ", counter)
                print("Atual estado do jogo: ", A1[counter], A2[counter], A3[counter], B1[counter], B2[counter], B3[counter], C1[counter], C2[counter], C3[counter])
                api.create_favorite(tweet.id)
                print("Verificando se é o usuario correto")
                if turno[counter] == 1:
                    if tweet.user.id != jogos[counter]:
                        print("Turno do primeiro jogador, você não é")
                        # Não é seu turno vei calma ae
                        return new_since_id
                else:
                    if tweet.user.id != p2[counter]:
                        print("Turno do segundo jogador, você não é")
                        # Nao é seu turno vei calma ae
                        return new_since_id
                print("Player verificado, prosseguindo")
                if "A1" in tweet.text:
                    jogada = 1
                elif "A2" in tweet.text:
                    jogada = 2
                elif "A3" in tweet.text:
                    jogada = 3
                elif "B1" in tweet.text:
                    jogada = 4
                elif "B2" in tweet.text:
                    jogada = 5
                elif "B3" in tweet.text:
                    jogada = 6
                elif "C1" in tweet.text:
                    jogada = 7
                elif "C2" in tweet.text:
                    jogada = 8
                elif "C3" in tweet.text:
                    jogada = 9
                else:
                    pular = True
                    api.update_status(
                        status = "Não consegui encontrar a sua escolha de jogada, responda esse tweet me marcando e digite a coordenada (A1, A2, A3...)",
                        in_reply_to_status_id=tweet.id,
                    )
                if pular == False:
                    if updateGame(jogada, counter) == 0:
                        api.update_status(
                            status = "A opção escolhida não esta disponivel, tente novamente",
                            in_reply_to_status_id=tweet.id,
                        )
                    else:
                        print("Jogada validada, prosseguindo com a implementação dela")
                        print("ID do primeiro jogador: ", jogos[counter])
                        print("ID do segundo jogador: ", p2[counter])
                        nome1 = api.get_user(jogos[counter]).screen_name
                        print("@ do primeiro jogador: ", nome1)
                        if p2[counter] != 1:
                            nome2 = api.get_user(p2[counter]).screen_name
                            print("@ do segundo jogador: ", nome2)
                        else:
                            nome2 = "BOT"
                            print("O Segundo jogador é um BOT")
                        if turno[counter] == 1:
                            proximo = nome2
                            turno[counter] = 2
                        else:
                            proximo = nome1
                            turno[counter] = 1
                        # Verificar se alguem ganhou
                        resposta = VerificarJogo(counter)
                        if resposta == 0 and p2[counter] == 1:
                            Casas = [A1[counter], A2[counter], A3[counter], B1[counter], B2[counter], B3[counter], C1[counter], C2[counter], C3[counter]]
                            print("O BOT esta se decidindo para o jogo: ", Casas)
                            jogada = bot(Casas)
                            print("Jogada do BOT: ", jogada)
                            updateGame(jogada, counter)
                            proximo = nome1
                            turno[counter] = 1
                            resposta = VerificarJogo(counter)
                        if resposta == 1: # Caso o player1 ganhe ------------------------------------------------------------------
                            api.update_status(
                                status= "@" + tweet.user.screen_name + " " + nome1 + "(" + xis + ")   " + vs + "   " + nome2 + "(" + bola + ")\n\n"
                                + emojis[A1[counter]] + "|" + emojis[A2[counter]] + "|" + emojis[A3[counter]]  + "                 A1 | A2 | A3\n"
                                + emojis[B1[counter]] + "|" + emojis[B2[counter]] + "|" + emojis[B3[counter]]  + "                 B1 | B2 | B3\n"
                                + emojis[C1[counter]] + "|" + emojis[C2[counter]] + "|" + emojis[C3[counter]]  + "                 C1 | C2 | C3\n\nVitória de " + nome1,
                                in_reply_to_status_id=tweet.id,
                            )
                        elif resposta == 2: # Caso o player2 ganhe ------------------------------------------------------------------
                            api.update_status(                            
                                status= "@" + tweet.user.screen_name + " " + nome1 + "(" + xis + ")   " + vs + "   " + nome2 + "(" + bola + ")\n\n"
                                + emojis[A1[counter]] + "|" + emojis[A2[counter]] + "|" + emojis[A3[counter]]  + "                 A1 | A2 | A3\n"
                                + emojis[B1[counter]] + "|" + emojis[B2[counter]] + "|" + emojis[B3[counter]]  + "                 B1 | B2 | B3\n"
                                + emojis[C1[counter]] + "|" + emojis[C2[counter]] + "|" + emojis[C3[counter]]  + "                 C1 | C2 | C3\n\nVitória de " + nome2,
                                in_reply_to_status_id=tweet.id,
                            )
                        elif resposta == 3: # Empate -------------------------------------------------------------------------------
                            api.update_status(
                                status= "@" + tweet.user.screen_name + " " + nome1 + "(" + xis + ")   " + vs + "   " + nome2 + "(" + bola + ")\n\n"
                                + emojis[A1[counter]] + "|" + emojis[A2[counter]] + "|" + emojis[A3[counter]]  + "                 A1 | A2 | A3\n"
                                + emojis[B1[counter]] + "|" + emojis[B2[counter]] + "|" + emojis[B3[counter]]  + "                 B1 | B2 | B3\n"
                                + emojis[C1[counter]] + "|" + emojis[C2[counter]] + "|" + emojis[C3[counter]]  + "                 C1 | C2 | C3\n\nEmpate!",
                                in_reply_to_status_id=tweet.id,
                            )
                        else: # Continuando o Jogo ---------------------------------------------------------------------------------
                            api.update_status(
                                status= "@" + tweet.user.screen_name + " " + nome1 + "(" + xis + ")   " + vs + "   " + nome2 + "(" + bola + ")\n\n"
                                + emojis[A1[counter]] + "|" + emojis[A2[counter]] + "|" + emojis[A3[counter]]  + "                 A1 | A2 | A3\n"
                                + emojis[B1[counter]] + "|" + emojis[B2[counter]] + "|" + emojis[B3[counter]]  + "                 B1 | B2 | B3\n"
                                + emojis[C1[counter]] + "|" + emojis[C2[counter]] + "|" + emojis[C3[counter]]  + "                 C1 | C2 | C3\n\n Vez de " + proximo,
                                in_reply_to_status_id=tweet.id,
                            )
                        if resposta != 0:
                            jogos[counter] = 0
    return new_since_id

def VerificarJogo(x):
    if (A1[x] == 1 and A2[x] == 1 and A3[x] == 1) or (B1[x] == 1 and B2[x] == 1 and B3[x] == 1) or (C1[x] == 1 and C2[x] == 1 and C3[x] == 1) or (A1[x] == 1 and B2[x] == 1 and C3[x] == 1) or (A1[x] == 1 and B1[x] == 1 and C1[x] == 1) or (A2[x] == 1 and B2[x] == 1 and C2[x] == 1) or (A3[x] == 1 and B3[x] == 1 and C3[x] == 1) or (A3[x] == 1 and B2[x] == 1 and C1[x] == 1):
        # Vitória do P1
        return 1
    elif (A1[x] == 2 and A2[x] == 2 and A3[x] == 2) or (B1[x] == 2 and B2[x] == 2 and B3[x] == 2) or (C1[x] == 2 and C2[x] == 2 and C3[x] == 2) or (A1[x] == 2 and B2[x] == 2 and C3[x] == 2) or (A1[x] == 2 and B1[x] == 2 and C1[x] == 2) or (A2[x] == 2 and B2[x] == 2 and C2[x] == 2) or (A3[x] == 2 and B3[x] == 2 and C3[x] == 2) or (A3[x] == 2 and B2[x] == 2 and C1[x] == 2):
        # Vitória do P2
        return 2
    elif A1[x] != 0 and A1[x] != 0 and A2[x] != 0 and A3[x] != 0 and B1[x] != 0 and B2[x] != 0 and B3[x] != 0 and C1[x] != 0 and C2[x] != 0 and C3[x] != 0:
        # Velha
        return 3
    else:
        return 0

def updateGame(x, slot):
    if x == 1: #A1 ---------------------------------------------------
        if A1[slot] == 0:
            if turno[slot] == 1:
                A1[slot] = 1
            else:
                A1[slot] = 2
            return 1
        else:
            return 0
    if x == 2: #A2 ---------------------------------------------------
        if A2[slot] == 0:
            if turno[slot] == 1:
                A2[slot] = 1
            else:
                A2[slot] = 2
            return 1
        else:
            return 0
    if x == 3: #A3 ---------------------------------------------------
        if A3[slot] == 0:
            if turno[slot] == 1:
                A3[slot] = 1
            else:
                A3[slot] = 2
            return 1
        else:
            return 0
    if x == 4: #B1 ---------------------------------------------------
        if B1[slot] == 0:
            if turno[slot] == 1:
                B1[slot] = 1
            else:
                B1[slot] = 2
            return 1
        else:
            return 0
    if x == 5: #B2 ---------------------------------------------------
        if B2[slot] == 0:
            if turno[slot] == 1:
                B2[slot] = 1
            else:
                B2[slot] = 2
            return 1
        else:
            return 0
    if x == 6: #B3 ---------------------------------------------------
        if B3[slot] == 0:
            if turno[slot] == 1:
                B3[slot] = 1
            else:
                B3[slot] = 2
            return 1
        else:
            return 0
    if x == 7: #C1 ---------------------------------------------------
        if C1[slot] == 0:
            if turno[slot] == 1:
                C1[slot] = 1
            else:
                C1[slot] = 2
            return 1
        else:
            return 0
    if x == 8: #C2 ---------------------------------------------------
        if C2[slot] == 0:
            if turno[slot] == 1:
                C2[slot] = 1
            else:
                C2[slot] = 2
            return 1
        else:
            return 0
    if x == 9: #C3 ---------------------------------------------------
        if C3[slot] == 0:
            if turno[slot] == 1:
                C3[slot] = 1
            else:
                C3[slot] = 2
            return 1
        else:
            return 0
        

def limparVariaveis(x):
    A1[x] = 0
    A2[x] = 0
    A3[x] = 0
    B1[x] = 0
    B2[x] = 0
    B3[x] = 0
    C1[x] = 0
    C2[x] = 0
    C3[x] = 0
    turno[x] = 1

def bot(Casas):
    r = 0
    ataque = False
    # Possibilidades na horizonal ------------------------------------------
    check = 0
    last = -1
    for loop1 in range(3):
        for loop2 in range(3):
            if Casas[loop2 + (loop1 * 3)] == 1:
                check = check + 1
            if Casas[loop2 + (loop1 * 3)] == 0:
                last = loop2 + (loop1 * 3)
        if check == 2 and last != -1:
            print("Foi encontrado uma possivel jogada horizontal de defesa na casa: ", last+1)
            print("Check de defesa: ", check)
            r = last
        check = 0
    # Possibilidadaes na vertical ------------------------------------------
    check = 0
    last = -1
    for loop1 in range(3):
        for loop2 in range(3):
            if Casas[loop1 + (loop2 * 3)] == 1:
                check = check + 1
            if Casas[loop1 + (loop2 * 3)] == 0:
                last = loop1 + (loop2 * 3)
        if check == 2 and last != -1:
            print("Foi encontrado uma possivel jogada vertical de defesa na casa: ", last+1)
            print("Check de defesa: ", check)
            r = last
            break
        check = 0
    # Possibilidades na diagonal ----------------------------------------
    check = 0
    last = -1
    for loop in range(3):
        if Casas[loop * 4] == 1:
            check = check+1
        if Casas[loop * 4] == 0:
            last = loop * 4
    if check == 2 and last != -1:
        print("Foi encontrado uma possivel jogada diagonal de defesa na casa: ", last+1)
        print("Check de defesa: ", check)
        r = last
    check = 0
    last = -1
    for loop in range(3):
        if Casas[2 + (loop * 2)] == 1:
            check = check+1
        if Casas[2 + (loop * 2)] == 0:
            last = 2 + (loop * 2)
    if check == 2 and last != -1:
        r = last
        print("Foi encontrado uma possivel jogada diagonal de defesa na casa: ", last+1)
        print("Check de defesa: ", check)
    # Atacar ---------------------------------------------------------------------
    # Possibilidades na horizonal ------------------------------------------
    check = 0
    last = -1
    for loop1 in range(3):
        for loop2 in range(3):
            if Casas[loop2 + (loop1 * 3)] == 2:
                check = check + 1
            if Casas[loop2 + (loop1 * 3)] == 0:
                last = loop2 + (loop1 * 3)
        if check == 2 and last != -1:
            print("Foi encontrado uma possivel jogada horizontal de ataque na casa: ", last+1)
            print("Check de ataque: ", check)
            r = last
        check = 0
    # Possibilidadaes na vertical ------------------------------------------
    check = 0
    last = -1
    for loop1 in range(3):
        for loop2 in range(3):
            if Casas[loop1 + (loop2 * 3)] == 2:
                check = check + 1
            if Casas[loop1 + (loop2 * 3)] == 0:
                last = loop1 + (loop2 * 3)
        if check == 2 and last != -1:
            print("Foi encontrado uma possivel jogada vertical de ataque na casa: ", last+1)
            print("Check de ataque: ", check)
            r = last
            break
        check = 0
    # Possibilidades na diagonal ----------------------------------------
    check = 0
    last = -1
    for loop in range(3):
        if Casas[loop * 4] == 2:
            check = check+1
        if Casas[loop * 4] == 0:
            last = loop * 4
    if check == 2 and last != -1:
        print("Foi encontrado uma possivel jogada diagonal de ataque na casa: ", last+1)
        print("Check de ataque: ", check)
        r = last
    check = 0
    last = -1
    for loop in range(3):
        if Casas[2 + (loop * 2)] == 2:
            check = check+1
        if Casas[2 + (loop * 2)] == 0:
            last = 2 + (loop * 2)
    if check == 2 and last != -1:
        r = last
        print("Foi encontrado uma possivel jogada diagonal de ataque na casa: ", last+1)
        print("Check de ataque: ", check)
    # Não encontrou nenhuma possibilidade:
    if r == 0:
        print("Nenhuma jogada encontrada")
        while(True):
            r = random.randint(0,8)
            if Casas[r] == 0:
                break
    return r+1
