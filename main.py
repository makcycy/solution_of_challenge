from credential import setEnv
from speech_to_text import SpeechToText
from sentiment_analysis import sample_analyze_sentiment
from entities_analysis import sample_analyze_entities
from text_classification_analysis import sample_classify_text
def main():
    stt = SpeechToText()
    result = stt.transcribe_file(speech_file='dataset/origin/flac_example.flac')
    for key in result.keys():
        print(f"{key}: {result[key]}")

    sample_analyze_sentiment(result['Transcript'])
    sample_analyze_entities(result['Transcript'])
    sample_classify_text(result['Transcript'])

if __name__ == '__main__':
    crediential_path = '../speech-analysis-312306-dec054d17512.json'
    setEnv(crediential_path)
    main()
    # test()

