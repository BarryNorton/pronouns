# Pronouns in English-language fiction
This project uses the ['Syntactic Ngrams' corpus](https://docs.google.com/document/d/14PWeoTkrnKk9H8_7CfVbdvuoFZ7jYivNTkBX2Hj7qLw/), 
based on the Google Books corpus and containing parse fragments with [Penn-Treebank part-of-speech (POS) tags](https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html), 
to discover and validate the reflexive pronouns contained and tagged therein, 
and to compare the frequency results between the general English corpus and the partition for fiction.

***

## Results

Based on projections over the respective Syntactic-Ngrams verbargs files, 
and filtering with a regex (r'sel\[fvl\]') to approximate reflexivity, 
the following candidate lists of pronouns (PRP) as direct objects (dobj) are obtained and ranked by frequency,
truncated to include the gender-neutral singular reflexive pronoun 'themself'
(see [Methodology](#methodology) for more details, and [Appendix A](#appendixA) for the full listings):

| **English**      | **English Fiction** |
|------------------|---------------------|
| **himself**: 8979386 |**himself: 3207256**
| **themselves**: 5578605|**herself: 1408594**
| itself: 3409264|myself: 1296374
| myself: 3014093|**themselves: 931156**
| **herself: 2329877**|yourself: 636914
| yourself: 1623751|itself: 495199
| ourselves: 1404367|ourselves: 255542
| oneself: 219794|yourselves: 41846
| yourselves: 143277|oneself: 27295
| thyself: 77279|thyself: 19193
| himselfe: 4020|hisself: 2384
| hisself: 3088|yerself: 1106
| ourself: 1380|meself: 724
| yerself: 1238|yoursell: 719
| meself: 1079|imself: 533
| yoursell: 866|ourself: 356
| imself: 414|~~mademoiselle: 316~~
| **themself: 316**|isself: 304
| yo'self: 291|yo'self: 281
| herselfe: 243|himselfe: 190
| ~~mademoiselle: 237~~|heself: 165
| isself: 221|erself: 156
| myselfe: 208|himsell: 155
| mysell: 202|hetself: 154
| erself: 149|mysell: 142
| himsell: 144|yoursells: 88
| heself: 136|hymself: 83
| itselfe: 136|**themself: 82**

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
