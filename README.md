# Who does really care about climate change ?
## A gender driven analysis to ecology related topics through the media from 2015 to 2020

_Abstract_: 

The idea of our project came from observing the people around us in their dailylife: women seem more involved in ecology than men. Indeed, among the people we meet, the proportion of women making ecological efforts seems to be higher than the proportion of men (vegetarianism, waste reduction, second hand, involvement in ecological associations etc...). However, this observation is only the result of our subjective observations, in only one aspect of ecology: everyday actions. 

By reviewing scientific litterature, we found a study (1) which showed that men in Sweden have a larger carbon footprint than women. In line with the thesis that women are more involved in ecology than men, another study (2) conducted in 11 industrialised countries showed that women are more concerned about environmental issues and that a major difference between men and women is their willingness to take action against climate change. However, a final study (3) found that in 2010, women in the US had less scientific knowledge than men on the subject.

Therefore, the involvement of gender in ecology seems to differ from one field to another. Thus, it would be interesting to study this phenomenon in order to determine whether a link can really be established between gender and involvement in ecology. The idea is to identify sub-fields of ecology and to study whether some are more attributed to men or women. Finally, we want to study if men and women speakers use the same communication tools.

- Study 1: [https://onlinelibrary.wiley.com/doi/10.1111/jiec.13176#jiec13176-bib-0044](https://onlinelibrary.wiley.com/doi/10.1111/jiec.13176#jiec13176-bib-0044)

- Study 2: [https://www.pewresearch.org/fact-tank/2015/12/02/women-more-than-men-say-climate-change-will-harm-them-personally/](https://www.pewresearch.org/fact-tank/2015/12/02/women-more-than-men-say-climate-change-will-harm-them-personally/) and [https://www.weforum.org/agenda/2015/12/climate-friendly-men-or-women/](https://www.weforum.org/agenda/2015/12/climate-friendly-men-or-women/)

- Study 3: [https://climatecommunication.yale.edu/publications/gender-differences-in-public-understanding-of-climate-change/](https://climatecommunication.yale.edu/publications/gender-differences-in-public-understanding-of-climate-change/)

## Do you really want to know more about the climate change 🌳? 
If you are really interested in our ADAdventure, don't wait, run and visit our site ▶️ [Who does really care about climate change ?](https://phictl.github.io/Panda-final-project/).

## Project structure

```bash
.
├── Cleaning_data.ipynb     # Notebook containing data handling pipeline and initial analysis
├── gender_extraction.py    # python file to process speaker_attributes.parquet
└── README.md
```

## Research questions
The goal is to analyse our dataset in order to answer the following research questions: 

1. How has the topic of ecology evolved from 2015 to 2020? We want to underline the evolution of the theme of ecology within these 5 years. Furthermore, we want to see a change on the topic of ecology due to the awareness of individuals in recent years.
2. What is the proportion of men and women talking about ecology between 2015 and 2020? Is it possible to notice a significant difference?
3. Defining several sub-topics from the main ecology-topic (politics, daily life action etc...), we would like to study which "sub-topics" are more attributed to men speakers and which ones are more attributed to women speakers?
4. Focusing on the topic of ecology, do men and women share the same communication tools? Which types of words are used most by men and which by women (for example, we want to study: verbs, adjectives, pronouns, adverbs, ...)?
5. Which hypotheses can we make explaining the observations of the previous questions? (for example: women speakers are more involved in ecology of the "daily life" because they are more inolved than men in the housework).

## Additional dataset
Additionally, we used the _speakers_attributes.parquet_ metadata files extracted from Wikipedia, as suggested in the project description. We simply filtered out all the speakers whose gender wasn’t either binary male or binary female, since the other genders amount to less than 1%. Finally, we merged that dataset with our filtered and cleaned quotes dataset.

## Methods

### Ecology related quotes selection
To select the quotes linked to ecology for our dataset, we perform a "lexical field" analysis as mentionned. We process as following to construct our dataset:

→ First we define an ecology lexical field in order to select all article titles of our interest.

→ Then we take all the quotations found in these articles. Therefore, this constitutes our dataset.

### Some statistics
    
As described in our research questions, the first part of the project is to extract some statistical conclusions on our dataset to explore the distribution of women and men speaking about ecology (question 1 and 2) such as: 

→ Plot general statistics of the quotes number of men and women for this two different years

→ Show the evolution per month of the number of citations of women in our dataset compared to those of men from the 2015 to the 2020. We also plot general statistics of the number of quotes of men and women for this two differents years. 

Furthermore, we have done some statitics to underline the topic evolution among all the years taking into consideration. 
    
### Subtopic selection

 In order to define different subfields of ecology and then try to detect which of them is most attributed to male speakers and which are most attributed to female speakers, we use two models to cluster our quotes into topics, namely Top2Vec and LDA. Each technique is rather used in large document topic modelling, but it works quite well in our setting (small text, namely quotations). For a more short text topic modelling approach, we also explored GSDMM, which is essentially a modified version of the LDA algorithm, but we decide to focus on LDA and Top2Vec to get each quote assigned with more than one topic.
Our goal is first to explore the topics discussed by each speaker in the environmental field, across time and gender. Then we aimed at detecting whether the quote was uttered by a male or a female based on the topic the quote was assigned to.
  
### Word analysis, defining communication tools for each gender

  A first method to use is the word frequency analysis. We will yield the most used verbs/nouns/pronouns for each gender or each subtopics. For each of those words, we could go a step further and use bi-grams to visualize how words are connected. Finally, we can run a general sentiment analysis per quote. Python provides a handy toolkit of Natural Language Processing to perform all these tasks, namely `nltk`.
  
## Contribution to the project
Each member of the Panda 🐼 team, consisting of Philippine des Courtils, Blanche Brognart, Alix Louvet and Stella Petronio contributed and helped to find an answer to each research question using the methods listed above.
