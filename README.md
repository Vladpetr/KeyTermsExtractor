# KeyTermsExtractor


**KeyTermsExtractor** can predict the next word in a pseudo-sentence based on the previous words in the sequence and the data that is used to create a statistical model.

The following operations were performed:
* [x] Read an XML-file containing stories and headlines.
* [x] Extract the headers and the text.
* [x] Tokenize each text.
* [x] Lemmatize each word in the story.
* [x] Get rid of punctuation, stopwords, and non-nouns with the help of NLTK.
* [x] Count the TF-IDF metric for each word in all stories.
* [x] Pick the five best scoring nouns.
* [x] Print each story's headline and the five best scoring nouns in descending order.

## Technologies used

- python - version 3.8


## License

    Copyright [2021] [Vladyslav Petrenko]

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
