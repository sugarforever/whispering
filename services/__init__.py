import tempfile
from openai import OpenAI
from langchain.document_loaders import TextLoader
from langchain.chains.summarize import load_summarize_chain
from langchain.chat_models import ChatOpenAI

class WhisperService:

    def transcribe(audio_file):
        client = OpenAI()

        audio_file = open(audio_file, "rb")
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            response_format="json",
            file=audio_file
        )
        
        return transcript.text

class LLMService:

    def summarize(content):
        with tempfile.NamedTemporaryFile(delete=True, mode="w") as file:
            file.write(content)
            file.seek(0)

            documents = TextLoader(file.name).load()

            chain = load_summarize_chain(ChatOpenAI(), chain_type="stuff")

            summary = chain.run(documents)

            return summary

if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()

    #transcription = WhisperService.transcribe("/Users/wyang14/Desktop/Screen Recording 2023-12-29 at 11.18.24 PM.m4a")
    #summary = LLMService.summarize(transcription)
    #print(summary)

    import whisper
    from whisper.utils import get_writer

    model = whisper.load_model("medium")

    input_file = "/Users/wyang14/Desktop/Screen Recording 2023-12-29 at 11.18.24 PM.m4a"
    output_directory = "./"

    result = model.transcribe(input_file)

    print(result)
    
    txt_writer = get_writer("txt", output_directory)
    txt_writer(result, input_file)