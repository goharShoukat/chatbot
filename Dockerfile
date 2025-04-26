FROM ollama/ollama:latest

WORKDIR /app

RUN ollama serve & \
    sleep 5 && \
    ollama pull gemma3:1b

EXPOSE 11434

ENTRYPOINT ["ollama"]
CMD [ "serve"]
