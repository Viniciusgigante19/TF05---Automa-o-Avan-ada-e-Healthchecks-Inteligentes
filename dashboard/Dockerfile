FROM nginx:alpine

# Remove a página padrão do Nginx
RUN rm -rf /usr/share/nginx/html/*

# Copia os arquivos do seu dashboard para o diretório do servidor
COPY . /usr/share/nginx/html/

# Porta padrão do container (mapeada para 3000 no seu compose)
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]