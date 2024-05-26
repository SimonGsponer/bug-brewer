FROM registry.access.redhat.com/ubi9/python-312:1-10

USER 1001

COPY src /opt/app-root/src
COPY .env /opt/app-root/.env
COPY --chown=1001:0 data /opt/app-root/src/data
COPY requirements.txt /opt/app-root/src/requirements.txt
RUN pip3 install -r requirements.txt
CMD ["python", "-m", "main"]