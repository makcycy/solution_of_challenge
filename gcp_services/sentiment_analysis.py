from google.cloud import language_v1

def sample_analyze_sentiment(text_content):
    """
    Analyzing Sentiment in a String

    Args:
      text_content The text content to analyze
    """

    client = language_v1.LanguageServiceClient()

    # text_content = 'I am so happy and joyful.'

    # Available types: PLAIN_TEXT, HTML
    type_ = language_v1.Document.Type.PLAIN_TEXT

    # Optional. If not specified, the language is automatically detected.
    # For list of supported languages:
    # https://cloud.google.com/natural-language/docs/languages
    language = "yue-Hant-HK"
    document = {"content": text_content, "type_": type_, "language": language}

    # Available values: NONE, UTF8, UTF16, UTF32
    encoding_type = language_v1.EncodingType.UTF32

    result = {}

    response = client.analyze_sentiment(request={'document': document, 'encoding_type': encoding_type})
    # Get overall sentiment of the input document
    result['document_sentiment_score'] = response.document_sentiment.score
    result['document_sentiment_magnitude'] = response.document_sentiment.magnitude
    # print(u"Document sentiment score: {}".format(response.document_sentiment.score))
    # print(
    #     u"Document sentiment magnitude: {}".format(
    #         response.document_sentiment.magnitude
    #     )
    # )
    # Get sentiment for all sentences in the document
    sentence_dict = {}
    for i, sentence in enumerate(response.sentences):
        sentence_content = sentence.text.content
        sentence_score = sentence.sentiment.score
        sentence_magnitude = sentence.sentiment.magnitude
        # print(u"Sentence text: {}".format(sentence.text.content))
        # print(u"Sentence sentiment score: {}".format(sentence.sentiment.score))
        # print(u"Sentence sentiment magnitude: {}".format(sentence.sentiment.magnitude))
        tmp_dict = {'sentence_content': sentence_content,
                    'sentence_score': sentence_score,
                    'sentence_magnitude': sentence_magnitude
                    }
        result[f'sentence_{i}'] = tmp_dict

    return result
    # Get the language of the text, which will be the same as
    # the language specified in the request or, if not specified,
    # the automatically-detected language.
    # print(u"Language of the text: {}".format(response.language))

from credential import setEnv
crediential_path = '../../speech-analysis-312306-dec054d17512.json'
setEnv(crediential_path)
