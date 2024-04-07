# Pronouns in English-language fiction
This project uses the ['Syntactic Ngrams' corpus](https://docs.google.com/document/d/14PWeoTkrnKk9H8_7CfVbdvuoFZ7jYivNTkBX2Hj7qLw/), based on the Google Books corpus and containing parse fragments with [Penn-Treebank part-of-speech (POS) tags](https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html), to discover and validate the pronouns contained and tagged therein and to compare the frequency results between the general English corpus and the partition for fiction.

***

## Results

Based on projections over the respective Syntactic-Ngrams verbargs files, and filtering with a regex (r'sel\[fvl\]'), the following candidate lists of pronouns (PRP) as direct objects (dobj) are obtained and ranked by frequency (see [Methodology](#methodology) for more details):

| **English**      | **English Fiction** |
|------------------|---------------------|
| himself: 8979386 | himself: 8979386    |
| themselves: 5578605
| itself: 3409264
| myself: 3014093
| herself: 2329877
| yourself: 1623751
| ourselves: 1404367
| oneself: 219794
| yourselves: 143277
| thyself: 77279
| himselfe: 4020
| hisself: 3088
| ourself: 1380
| yerself: 1238
| meself: 1079
| yoursell: 866
| imself: 414
| themself: 316
| yo'self: 291
| herselfe: 243
| mademoiselle: 237
| isself: 221
| myselfe: 208
| mysell: 202
| erself: 149
| himsell: 144
| heself: 136
| itselfe: 136
| yoursells: 82
| yoreself: 65
| youself: 61
| theirself: 55
| hymself: 51
| yourselfe: 47
| maself: 44
| itself1: 40
| you'self: 36
| y'self: 30
| hirself: 29
| thyselfe: 29
| yeself: 24
| m'self: 22
| mahself: 21
| yuhself: 16
| yusself: 15
| sheself: 15
| meselfe: 14
| one'sself: 13
| y'rself: 13
| itsselfe: 13
| theeself: 12
| self: 12
| myselffe: 12
| yourselvesf: 12
| aself: 12
| itsell: 11
| inself: 11
| hymselfe: 11
| themselfe: 11
| iself: 10
| weself: 10
| ltself: 10

***

## Methodology
<a id="methodology"></a>
  
The first challenge in approaching this problem is the broken link to the Syntactic Ngrams corpus. It is, however, still contained in a [cache](https://web.archive.org/web/20210621193950/https://storage.googleapis.com/books/syntactic-ngrams/index.html) via the Internet Archive.

***

## Acknowledgements

The Syntactic Ngrams corpus is documented in Goldberg and Orwant (ACL 2013) [[1]](#1).

This analysis was aided by the authors of Hoyle et al., (ACL 2019) [[2]](#2).

***

## References

<a id="1">[1]</a> 
Yoav Goldberg and Jon Orwant (2013). 
A Dataset of Syntactic-Ngrams over Time from a Very Large Corpus of English Books.
In Second Joint Conference on Lexical and Computational Semantics (*SEM), Volume 1: 
Proceedings of the Main Conference and the Shared Task: Semantic Textual Similarity, 
pages 241–247, 
Atlanta, Georgia, USA. 
Association for Computational Linguistics.

<a id="2">[2]</a> 
Alexander Miserlis Hoyle, Lawrence Wolf-Sonkin, Hanna Wallach, Isabelle Augenstein, and Ryan Cotterell (2019). 
Unsupervised Discovery of Gendered Language through Latent-Variable Modeling. 
In Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics, 
pages 1706–1716, 
Florence, Italy. 
Association for Computational Linguistics.

***

## Licenses

<img src="https://mirrors.creativecommons.org/presskit/buttons/88x31/png/by.png" alt="CC-BY 4.0 logo" width="100"/>

This text and its embedded resources are made available under [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/).

All code is made available using the MIT license (contained in the repository).
