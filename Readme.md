# ConSim
ConSim is a python library for concepts similarity within an ontology. It consists in looking for the most similar problem in terms of concept classification or taxonomy

![Concept similarity](images/simgraph.png "Concept similarity illustration")

Formula: `ConSim(c^*, c) = 2*N_R/(N^*+N+2*N_R)`

Was defined in:

`
@inproceedings{verbssemantics1994,
	author = {Wu, Zhibiao and Palmer, Martha},
	title = {Verbs Semantics and Lexical Selection},
	year = {1994},
	publisher = {Association for Computational Linguistics},
	address = {USA},
	url = {https://doi.org/10.3115/981732.981751},
	pages = {133–138},
	numpages = {6},
	location = {Las Cruces, New Mexico},
	series = {ACL '94}
}
`

# How to use

`` consim(rdf_file, concept1, concept2):numeric``