def generate_script(trends):
    script = "Hoje vamos falar sobre as tendências de animes no YouTube Brasil!\n\n"
    for trend in trends:
        script += f"Título: {trend['title']}\n"
        script += f"Descrição: {trend['description']}\n"
        script += f"Veja mais em: {trend['url']}\n\n"
    script += "Espero que você tenha gostado das tendências de hoje! Até a próxima!"
    return script
