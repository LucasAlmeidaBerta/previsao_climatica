import azure.functions as func
from azure.storage.blob import BlobServiceClient
import logging
import json
from datetime import datetime
from azure.storage.blob import BlobClient

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

SAS_URL = "https://saengdadoscrescer2.blob.core.windows.net/grupo01/landingzone/cadastros_emails/inscricoes.csv?sp=racw&st=2025-05-25T21:33:52Z&se=2025-06-25T03:00:00Z&spr=https&sv=2024-11-04&sr=c&sig=%2BtdN0g9E6xdxXGVzmRcABz65YQMKFjdjJT61PUs8QVk%3D"

CAPITAIS_BRASIL = [
    "Rio Branco", "Maceió", "Macapá", "Manaus", "Salvador", "Fortaleza", "Brasília",
    "Vitória", "Goiânia", "São Luís", "Cuiabá", "Campo Grande", "Belo Horizonte",
    "Belém", "João Pessoa", "Curitiba", "Recife", "Teresina", "Rio de Janeiro",
    "Natal", "Porto Alegre", "Porto Velho", "Boa Vista", "Florianópolis",
    "São Paulo", "Aracaju", "Palmas"
]

capital_options = "".join(f'<option value="{cidade}">{cidade}</option>' for cidade in CAPITAIS_BRASIL)
html_form = f"""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Aqualert Cadastro de E-mail</title>
    <link rel="icon" type="image/png" href="https://www.svgrepo.com/show/502423/weather.svg" />
</head>
<body style="margin:0; font-family:Arial, sans-serif; background-color:#9dd7e0; color:#0c2a3d; display:flex; justify-content:center; align-items:center; height:100vh;">

    <div style="background-color:white; padding:30px; border-radius:12px; box-shadow:0 4px 8px rgba(0,0,0,0.2); text-align:center; width:300px;">
        <h1 style="color:#0c2a3d; margin-bottom:10px;">Aqualert Newsletter 📰</h1>
        <h2 style="color:#0c2a3d; font-size:16px; margin-bottom:20px;">Inscreva-se Para Receber Alertas</h2>
        
        <form method="post">
            <label for="email" style="font-weight:bold; display:block; margin-top:10px;">E-mail:</label>
            <input type="email" id="email" name="email" required
                   style="padding:8px; width:100%; border:1px solid #23b2c7; border-radius:6px; margin-top:5px;">

            <label for="cidade" style="font-weight:bold; display:block; margin-top:15px;">Cidade:</label>
            <select id="cidade" name="cidade" required
                    style="padding:8px; width:100%; border:1px solid #23b2c7; border-radius:6px; margin-top:5px;">
                <option value="">Selecione uma cidade</option>
                {capital_options}
            </select>
            <div style="margin-top:20px;">
                <button type="submit" name="action" value="inscrever"
                        style="padding:10px 20px; border:none; border-radius:8px; font-weight:bold; color:white; background-color:#0c2a3d; cursor:pointer;">
                    Enviar
                </button>
                <button type="submit" name="action" value="cancelar"
                        style="padding:10px 20px; border:none; border-radius:8px; font-weight:bold; color:white; background-color:#e53935; cursor:pointer; margin-left:10px;">
                    Cancelar Assinatura
                </button>
            </div>
        </form>
    </div>
</body>
</html>
"""

@app.route(route="aqualert/receber_alertas")
def form_inscricao_email(req: func.HttpRequest) -> func.HttpResponse:
    try:
        if req.method == "GET":
            return func.HttpResponse(html_form, mimetype="text/html")

        elif req.method == "POST":
            form_data = req.form
            email = form_data.get("email")
            cidade = form_data.get("cidade")
            action = form_data.get("action")  # 'inscrever' ou 'cancelar'

            if not email:
                return func.HttpResponse("O e-mail é obrigatório.", status_code=400)

            ativo = 1 if action == "inscrever" else 0
            cidade_val = cidade if cidade else ""

            nova_linha = f"{email},{cidade_val},{datetime.now().isoformat()},{ativo}\n"

            blob_client = BlobClient.from_blob_url(blob_url=SAS_URL)

            try:
                blob_bytes = blob_client.download_blob().readall()
                csv_atual = blob_bytes.decode("utf-8")
                novo_conteudo = csv_atual + nova_linha
            except Exception:
                novo_conteudo = "email,cidade,data_inscricao,ativo\n" + nova_linha

            blob_client.upload_blob(novo_conteudo, overwrite=True)

            if action == "cancelar":
                return func.HttpResponse(f"Assinatura do e-mail {email} foi cancelado com sucesso.", status_code=200)
            else:
                return func.HttpResponse(f"Obrigado, {email}! Sua inscrição foi registrada.", status_code=200)

    except Exception as e:
        return func.HttpResponse(f"Erro: {str(e)}", status_code=500)