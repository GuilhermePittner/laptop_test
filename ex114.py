import http.client

def check_status_code(domain):
    try:
        conn = http.client.HTTPSConnection(domain)
        conn.request("HEAD", "/")
        response = conn.getresponse()

        if response.status == 200:
            print(f"O domínio {domain} retornou status 200 (OK).")
        else:
            print(f"O domínio {domain} retornou status {response.status}.")

    except Exception as e:
        print(f"Erro ao tentar acessar o domínio {domain}: {e}")

# Exemplo de uso
dominio_teste = "www.youtube.com"
check_status_code(dominio_teste)
