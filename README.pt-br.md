# concatvids

**concatvids** é uma ferramenta de linha de comando em Python para concatenar arquivos de vídeo (como .mp4) usando o ffmpeg, ordenando-os automaticamente por data de modificação. Muito útil para juntar clipes gravados separadamente, como vídeos produzidos pela GoPro, de forma simples e rápida.

---

## ✅ Recursos

- Detecta e ordena vídeos pela data (mais antigos primeiro)
- Gera automaticamente um `filelist.txt` no formato aceito pelo `ffmpeg`
- Concatena vídeos via `ffmpeg` usando o modo rápido (`-c copy`)
- Permite definir o nome do arquivo de saída via argumento `-o`
- Upload opcional para o YouTube com autenticação segura via OAuth2
- Reencodificação opcional para garantir compatibilidade de áudio/vídeo
- Corte opcional de vídeo com `--ss` (início) e `--to` (fim)
- Compatível com Windows, Linux e macOS (requer `ffmpeg` instalado)

---

## 🚀 Instalação

### 1. Clone o repositório:

```bash
git clone git@github.com:seu-usuario/concatvids.git
cd concatvids
```

### 2. Instale com `pip`:

```bash
pip install .
```

> Isso instala o comando `concatvids` globalmente, se estiver em um ambiente com permissões apropriadas (ou dentro de um venv).

---

## 🧪 Pré-requisitos

* Python 3.7+
* [`ffmpeg`](https://ffmpeg.org/download.html) instalado e disponível no `PATH`
* Conta Google com acesso ao [YouTube Data API v3](https://console.developers.google.com/)
* Arquivo `client_secrets.json` salvo em ~/.config/concatvids/. Obtenha este arquivo no [Google Cloud Console](https://console.cloud.google.com/) após ativar a **YouTube Data API v3**.

---

## 💻 Como usar

### Comando básico:

```bash
cd pasta_com_videos
concatvids
```

Isso irá:

* Buscar todos os arquivos `.mp4` no diretório atual
* Ordenar pela data de modificação
* Concatenar os arquivos com `ffmpeg`
* Gerar o vídeo final `output.mp4`

### Com nome de saída personalizado:

```bash
concatvids -o meu_video_final.mp4
```

### Com outra extensão de vídeo (ex: `.mov`):

```bash
concatvids --ext mov -o resultado.mov
```

---

### ✂️ Cortando um vídeo

Também é possível cortar um único vídeo informando o **tempo de início** (`--ss`) e o **tempo de fim** (`--to`):

```bash
concatvids -i input.mp4 --ss 00:00:10 --to 00:00:20 -o trecho.mp4
```

Se `-o` não for informado, o arquivo de saída padrão será `output.mp4`.

---

### 📤 Fazer upload para o YouTube e evitar erros com timestamps

Exemplo com upload ativado:

```bash
concatvids --upload --title "Treino 21/07" --description "Descidas com palmar" --tags nado treino gopro
```

Se não fornecer `--title` ou `--description`, será solicitado interativamente. O vídeo será enviado como **não listado** e **não destinado a crianças** por padrão.

Para evitar problemas com timestamps (erros do tipo `Non-monotonic DTS`), use a opção `--reencode`:

```bash
concatvids --reencode -o video_final.mp4
```

---

## 📝 Exemplo de `filelist.txt` gerado

```text
file 'clip1.mp4'
file 'clip2.mp4'
file 'clip3.mp4'
```

---

## 🛠 Desenvolvimento

### Instalar em modo editável:

```bash
pip install -e .
```

### Requisitos de desenvolvimento:

```bash
pip install -r requirements.txt
```

---

## 📄 Licença

[MIT](LICENSE)

---

## 🤝 Contribuições

Contribuições são bem-vindas! Abra uma issue ou pull request se quiser sugerir melhorias ou corrigir problemas.

## ✍️ Créditos

Este projeto foi idealizado por André F. e desenvolvido com suporte técnico do ChatGPT, da OpenAI.
