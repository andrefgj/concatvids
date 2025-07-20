# concatvids

**concatvids** é uma ferramenta de linha de comando em Python para concatenar arquivos de vídeo (como `.mp4`) usando o `ffmpeg`, ordenando-os automaticamente por data de modificação. Ideal para juntar clipes gravados separadamente de forma simples e rápida.

---

## ✅ Recursos

- Detecta e ordena vídeos pela data (mais antigos primeiro)
- Gera automaticamente um `filelist.txt` no formato aceito pelo `ffmpeg`
- Concatena vídeos via `ffmpeg` usando o modo rápido (`-c copy`)
- Permite definir o nome do arquivo de saída via argumento `-o`
- Compatível com Windows, Linux e macOS (requer `ffmpeg` instalado)

---

## 🚀 Instalação

### 1. Clone o repositório:

```bash
git clone git@github.com:seu-usuario/concatvids.git
cd concatvids
````

### 2. Instale com `pip`:

```bash
pip install .
```

> Isso instala o comando `concatvids` globalmente, se estiver em um ambiente com permissões apropriadas (ou dentro de um venv).

---

## 🧪 Pré-requisitos

* Python 3.7+
* [`ffmpeg`](https://ffmpeg.org/download.html) instalado e disponível no `PATH`

---

## 💻 Como usar

### Comando básico:

```bash
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

## 📝 Exemplo de `filelist.txt` gerado

```text
file 'clip1.mp4'
file 'clip2.mp4'
file 'clip3.mp4'
```

---

## 🛠 Desenvolvimento

Se quiser contribuir ou modificar:

```bash
# Reinstalar localmente após alterações
pip install -e .
```

---

## 📄 Licença

[MIT](LICENSE)

---

## 🤝 Contribuições

Contribuições são bem-vindas! Abra uma issue ou pull request se quiser sugerir melhorias ou corrigir problemas.

✍️ Créditos
Este projeto foi idealizado por André F. e desenvolvido com suporte técnico do ChatGPT, da OpenAI.
