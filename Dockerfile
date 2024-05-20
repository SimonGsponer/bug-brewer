FROM registry.access.redhat.com/ubi9/python-312:1-10

USER 1001

COPY src /opt/app-root/src
COPY --chown=1001:0 data /opt/app-root/src/data

CMD ["python", "-m", "main"]