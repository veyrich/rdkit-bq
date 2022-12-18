FROM veyrich/rdkit_base:2022_09

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update
RUN apt-get install -y python3 python3-pip
RUN pip3 install flask gunicorn

WORKDIR /app
COPY rdkitmw.py /app/rdkitmw.py
ENV FLASK_APP=/app/rdkitmw.py

EXPOSE 8080/tcp

#use flask dev server
ENTRYPOINT [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "-p", "8080"]

#or a proper WSGI HTTP server
#ENTRYPOINT [ "gunicorn", "-w", "4", "--bind", "0.0.0.0:8080", "rdkitmw:app" ]
