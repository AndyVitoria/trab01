from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

# Palavra que deseja buscar em tweets e nome do arquivo de saida
class listener(StreamListener):
    def on_data(self, data):
        tweet = data[1:-1].split('"text":"')[1].split('",')[0]
        # Caso ocorra erro de caracteres comente o print abaixo.
        print(tweet)
        arq = open('dados/' + data[52:70] + '.txt', 'w')
        arq.writelines(data + '\n')
        arq.close()
        return True

    def on_erro(self, status):
        print("Erro: " + status)


def main():
    ckey = 'A6xpkglYz8yyKXJHcWqBsHph5'
    csecret = 'rIok63xcB5mJLeoAM3jhHYu5AlpKek5YHhnrFl1L4ZIRxSl3Eo'
    atoken = '806490152004685824-913Bhg0iUpqdAvHSc67LkCm5eSOe3PJ'
    asecret = 'oA5E5MIV7YitfvQLssoFLOmxH79jkVmkzDnyAcI3Eao5Y'

    auth = OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)

    kWord = str(input('Informe a palavra-chave da busca: '))
    print('Buscando por ' + kWord + 'no Twitter...\n')
    twitterStream = Stream(auth, listener(kWord))
    twitterStream.filter(track=[kWord])

    return 0


if __name__ == '__main__':
    main()
