./scripts/activate



uvicorn main:app --reload

uvicorn test:app --reload




docker save [image] -o file.tar


docker load file.tar


docker run -p 8000:80 demo