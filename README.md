This is the solution of the challenge.

The main purpose of the challenge is to address the audio files from the call center with full of background noise.

In this challenge, SOTA model in DNS Challenge held by Microsoft is used, called FullSubNet model.

Reference:
FullSubNet Github Repo: https://github.com/haoxiangsnr/FullSubNet
Paper: https://arxiv.org/abs/2010.15508

Meanwhile, the remaining part is to convert the audio to text with Google Speech To Text API as well as Sentiment
Analysis, Entity Analysis and Text Classification. However, only sentiment analysis will be in the demo. The codes for
entity analysis and text classification are done and included in the folder of 'gcp_services'. The results are printed
in the form of Python Dictionary with the key as filename.
