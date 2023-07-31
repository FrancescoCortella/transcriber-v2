import whisper

model = whisper.load_model("base")
result = model.transcribe("audio-test-1.m4a", fp16=False)
print(result["text"])