# Preface from Michael DeBellis

I sometimes find it easy to be pessimistic about the human race. The world gives us plenty of reasons for discouragement. But one thing that illustrates some of the best in people is the open source movement.

It is remarkable how much of the software infrastructure that powers the modern internet is open source. The Linux operating system, Apache web servers, Kubernetes, Kafka, Docker containers, and countless programming languages, libraries, databases, and development tools were created as open-source projects or converted from internal projects to software freely available to all developers. Organizations and individuals understand that software becomes more valuable when it is shared openly so that the developer community can study it, improve it, and build on it. It’s a very positive thing that corporations such as Google and Linked In are motivated to contribute software in which they’ve invested heavily into the open source infrastructure. Even more so that so many individuals will contribute their time to maintain and expand open source tools for the simple joy of seeing things work and providing tools that colleagues will find useful. 

That generosity is not limited to code. Documentation, examples, tutorials, walkthroughs, bug reports, and teaching materials are also essential parts of the open-source ecosystem. They are just as important, because good software is wasted if  no one can understand or learn to use it.

Tutorials are often underappreciated. As I said when I first created my revised version of the Protégé Pizza tutorial, no one gets a PhD for writing a tutorial. Tutorials do not usually receive the same professional recognition as research papers, software frameworks, or commercial products. Yet, for many learners, a good tutorial is the difference between a technology remaining abstract vs. becoming usable.

That is why I am pleased to see Xiaoqi Zhao’s *Mastering Ontology Engineering with Protégé and Pizza.owl: From Semantic Foundations to Executable Knowledge Architecture (EKA)*. It continues a tradition that has always been central to the Semantic Web community: building on prior work, acknowledging intellectual lineage, and helping new learners move from abstract ideas to practical results.

The Pizza tutorial itself has a long history. The original tutorial was developed by members of the Protégé and ontology engineering community.  It became one of the best-known introductions to OWL ontology development. Its genius was the choice of a domain that was familiar enough to get out of the learner’s way. Almost everyone understands pizzas, toppings, bases, vegetarian choices, and spicy ingredients. Because the domain is simple, learners can focus on the real subject: classes, properties, axioms, inference, queries, and rules.

My own revision of the Pizza tutorial was motivated by a practical teaching need. I was preparing a hands-on workshop and realized that the older tutorial no longer matched the current Protégé user interface closely enough for beginners. Especially since the majority of the students in that workshop were Library Science experts, not developers. Experienced OOP developers can translate instruction such as “add superclass” into revised user interfaces such as “add subclassOf”. New learners, especially those coming from fields such as library science and information architecture, should not have to do that translation while also trying to understand the concepts of OWL and other Semantic Web languages. The tutorial needed to match the actual tool.

What began as a small update became a much larger project. I updated the examples for Protégé 5, revised screenshots and instructions, and added material on topics such as SPARQL, SHACL, SWRL, IRIs, namespaces, and WebProtégé. My goal was not just to teach people where to click, but to help them understand why the clicks mattered.

Xiaoqi’s eBook takes that work in a new direction. It uses the Pizza tutorial as a foundation, but it is not simply a transcription or repetition of the older material. It connects OWL ontology engineering to a broader architectural vision that he calls Executable Knowledge Architecture (EKA).The eBook encourages learners to see ontology development not as an isolated academic exercise, but as part of a larger architecture for formal knowledge, knowledge graphs, reasoning, validation, and intelligent systems.

I’ve spent half of my career as a consultant and the other half doing research. One of the most important lessons I learned as a consultant is that the hard part isn’t writing software, the hard part is integration. That’s true whether we’re integrating rules with COBOL programs, LLMs with enterprise data, or ontologies and knowledge graphs into distributed computing environments.

That broader perspective is timely.

For a while, it seemed that the Semantic Web might remain a powerful idea that never achieved its hoped-for impact. The original vision was ambitious: not just a web of documents, but a web of data and meaning, where machines could understand and integrate information across sources. The challenge was that adding semantics requires work. It requires modeling. It requires shared identifiers. It requires explicit commitments about meaning. It requires different groups in large organizations to talk to each other and define shared concepts and domain boundaries.

Many organizations decided that this was too much effort. It was easier to publish documents, tables, and data dumps and let humans, search engines, and especially machine learning systems make sense of them.

Ironically, the rise of Large Language Models (LLMs) has created renewed interest in the very technologies that some people thought machine learning would make unnecessary. LLMs are extraordinary tools. Used well, they can provide enormous productivity benefits. But they also have well-known limitations. Their reasoning is opaque. They can generate fluent but incorrect answers. They may struggle with provenance, controlled terminology, and domain-specific meaning.

These problems are not merely accidental bugs. They follow naturally from the fact that LLMs are statistical models rather than explicit knowledge models. Improvements in scale, training, and architecture will continue to make them more capable, but many practical applications still need complementary structures: curated data, explicit semantics, provenance, and constraints.

That is why knowledge graphs and ontologies are becoming more important. Retrieval Augmented Generation (RAG) was an early response to the problem of grounding LLMs in curated information. But as applications become more demanding, simple document retrieval is often not enough. Many domains require richly interconnected knowledge and automated reasoning. RDF, OWL, SPARQL, SHACL, and reusable ontologies such as Dublin Core, PROV-O, and SKOS provide mature standards for representing and working with exactly that kind of explicit knowledge representation. Explicit knowledge representation based on logic and set theory is the perfect complement to the powerful inductive statistical models that power LLMs.

This renewed interest also means that the word “ontology” is now used in many different ways. Some commercial systems use the term for models that are closer to enterprise object models  than to ontologies in the Semantic Web sense. I understand why some researchers and ontology engineers find that frustrating. I sometimes do too. But I also see it as a sign of progress. I have seen this pattern since the early days of expert system adoption and later with the adoption of Object-Oriented Programming and Agile methods: when ideas move from research to industry, terms such as rule-based, knowledge base, *Rapid Application Development (RAD)*, object model, and ontology are stretched, simplified, and repurposed. That can create confusion, but it also shows that industry has recognized that the underlying ideas matter. Eventually as practitioners understand the core research ideas, they make educated decisions and can separate real technology from marketing hype. Tutorials such as this eBook are an essential part of that process. Learners need to understand not only that ontologies are useful, but what ontologies and other semantic technology provide that is new and why these new capabilities matter.

One of the things I appreciate about this eBook is that it tries to connect beginner-level Protégé modeling with larger architectural questions. A learner begins with classes such as *Pizza*, *PizzaTopping*, *CheeseTopping*, and *VegetableTopping*. But those beginner examples lead naturally to deeper questions. What is the difference between a class and an individual? When should a class be primitive, and when should it be defined? What does a reasoner actually infer? Why does OWL’s open-world assumption behave differently from a database constraint? When should we use OWL reasoning, and when should we use SHACL validation? How do ontologies relate to RDF graphs, triple stores, SPARQL queries, and larger distributed system architectures?

Those are not minor details. They are the conceptual foundation of ontology engineering.

My strongest advice to readers is to keep Protégé open while reading. Do the exercises. Run the reasoner frequently. That last part is really critical. For training ontologies, the reasoner executes immediately. Running it after every change means you’ll see an error as soon as it is created. When that happens, the reasoner can almost always focus you on the specific problem. If you wait until there are several errors the reasoner feedback is usually much less helpful and finding errors can take hours instead of minutes.

When something surprising happens, slow down and understand why. In OWL, surprises are often the most valuable teaching moments. A reasoner that classifies something unexpectedly, fails to classify something you expected, or reports an inconsistency is showing you the difference between what you intended to model and what you actually modeled.

That distinction is at the heart of ontology engineering.

A good ontology is not just a diagram. It is not just a taxonomy. It is not just a data model. It is an explicit, formal model of meaning in a domain. Building one requires careful thought, iteration, testing, and patience. The Pizza tutorial remains useful because it gives learners a simple domain in which to practice those habits before applying them to medicine, finance, manufacturing, enterprise architecture, LLM integration and other business, engineering, and scientific domains.

I am glad to see this new contribution to the Pizza tutorial lineage. It reflects the best spirit of open educational work.

The journey begins with pizza. But the real subject is meaning.

Michael DeBellis<br>
2 July 2026<br>
San Francisco, CA<br>
https://www.michaeldebellis.com/blog