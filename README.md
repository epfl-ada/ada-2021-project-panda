# Gender involvement in ecology

**Abstract**: 
The idea of our project came from observing the people around us in their dailylife: women seem more involved in ecology than men. Indeed, among the people we meet, the proportion of women making ecological efforts seems to be higher than the proportion of men (vegetarianism, waste reduction, second hand, involvement in ecological associations etc...). However, this observation is only the result of our subjective observations, in only one aspect of ecology: everyday actions. It would therefore be interesting to study this phenomenon adopting a more objective point of view in order to determine whether a link can really be established between gender and involvement in ecology. The idea is also to identify sub-fields of ecology and to study whether some are more attributed to men or women. Finally, we want to study if men and women speakers use the same communication tools.

## Project structure :

```bash
.
├── Cleaning_data.ipynb     # Notebook containing data handling pipeline and initial analysis
├── gender_extraction.py    # python file to process speaker_attributes.parquet
└── README.md
```
## Research questions

The goal is to analyse our dataset in order to answer the following research questions: 

1. How the ecology topic evolved between 2015 and 2019? We compare only year 2015 and 2019 because we want to study the evolution between the first year available in the dataset and the most recent and with complete data year. Moreover, we want to see a change on the subject of ecology due to an awareness of individuals these past three years.
2. What are the proportions of men and women talking about ecology between 2015 and 2019 ? Do they differ a lot ?
3. Defining several subfields of ecology (Politics, daily life action etc...), we would like to study which "subfields" are more attributed to men speakers and which ones are more attributed to women speakers.
4. Focusing on the topic of ecology, do men and women share the same communication tools? Which kind of words is more used by men, which one by women (for example: emotional words, pronouns and so on) ? Do we observe an evolution in the words used by each gender between 2015 and 2019 ?
5. Which hypotheses can we make explaining the observations of the previous questions? (for example: women speakers are more involved in ecology of the "daily life" because they are more inolved than men in the housework).

## Additional dataset 
We made use of the speakers_attributes.parquet metadata files extracted from Wikipedia, as suggested in the project description. We simply filtered out all the speakers whose gender wasn’t either binary male or binary female, since the other genders amount to less than 1%. Finally, we merged that dataset with our filtered and cleaned quotes dataset.

## Methods

### Ecology related quotes selection
To select the quotes linked to ecology for our dataset, we perform a "lexical field" analysis as mentionned. We process as following to construct our dataset:

→ First we define an ecology lexical field in order to select all article titles of our interest.

→ Then we take all the quotations found in these articles. Therefore, this constitutes our dataset.

### Some statistics
    
As described in our research questions, the first part of the project is to extract some statistical conclusions on our dataset to explore the distribution of women and men speaking about ecology (question 1 and 2) such as : 

→ Plot general statistics of the quotes number of men and women for this two different years

→ Show the evolution per day of the number of citations of women in our dataset compared to those of men for the years 2015 and 2019. We also plot general statistics of the number of quotes of men and women for this two differents years. 

Finally we will do some statitics to perform some conclusion about the occurences of each "subfields" between men and women once they have been defined (question 3). 
    
### Subtopic selection

  In order to define different subfields of ecology and then try to detect which of them is most attributed to male speakers and which are most attributed to female speakers, the method that we want to use is determined by the Gibbs Sampling Dirichlet Mixture Model (GSDMM) algorithm. GSDMM is a short text clustering topic model which appears to be the most suitable model for finding an answer to our research question 3. GSDMM is essentially a modified version of the Latent Dirichlet Allocation (LDA) algorithm and it starts from the initial assumption that a document (in our case a quotation) encompasses 1 topic, this means that we suppose that the words within a quotation are generated using the same unique topic. Precisely, we want to make use of the `MovieGroupProcess` class of the `gsdmm` library, which is an equivalent procedure of GSDMM.
  
### Word analysis, defining communication tools for each gender

  A first method to use is the word frequency analysis, getting rid of stop words such as "the" or "is", but maybe keeping the pronouns. We will yield the most used verbs/nouns/pronouns for each gender or each subtopics. For each of those words, we could go a step further and use bi-grams to visualize how words are connected. Finally, we can run a general sentiment analysis per quote. Python provides a handy toolkit of Natural Language Processing to perform all these tasks, namely `nltk`.

## Schedule for Milestones 3

| Week            | Stella                  | Philippine              | Blanche                          | Alix                                  |
|-----------------|-------------------------|-------------------------|----------------------------------|---------------------------------------|
| 23 nov - 26 nov | Sub topic selection     | Word frequency analysis | Blog creation                    | Statistics over years                 |
| 26 nov - 3 dec  | Word frequency analysis | Word frequency analysis | Statistics                       | Statistics                            |
| 4 dec - 10 dec  | Sentiment analysis      | Sentiment analysis      | Statistics of subtopic selection | Visualization (make graphs)           |
| 11 dec - 17 dec | Visualisation and blog  | Visualisation           | Visualisation and blog           | Visualisation (make plots and graphs) |
