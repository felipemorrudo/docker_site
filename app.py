from flask import Flask

app=Flask(__name__ )

@app.route('/')
def hello_world():
    return '<h1>Olá diretamente do meu site criado com Docker!</h1><p>Isso está rodando dentro de um container!</p>'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
    