from fastapi import FastAPI 

from your_module import recognize_face  # Import your face recognition logic 

 

app = FastAPI() 

 

@app.post("/recognize-face/") 

async def recognize(image: bytes): 

    person = recognize_face(image) 

    return {"person_identified": person} 