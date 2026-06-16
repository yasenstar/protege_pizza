# Error Tracker

## Error E-001 | Severity: Must Fix | Reporter: Michael DeBellis | Date: 2026-06-16

Issue Description:

The EKA table in Chapter 00 claims that an OWL reasoner "does not modify a graph or database," labeling it "No (read-only inference)." This is overly broad. While true for the normal Protégé workflow (where inferred axioms are displayed rather than asserted into the saved ontology), it is not true as a general statement about semantic systems or graph databases. Triplestores may materialize inferred triples, maintain inferred closures, or expose inferences virtually depending on configuration.

Suggested Fix:

Revise to: "In Protégé, reasoner results are normally shown as inferred axioms rather than automatically saved as asserted axioms. In graph databases and rule-enabled triple stores, inferred triples may be materialized, persisted, or exposed virtually depending on the system and configuration."

Status: Pending | Chapters: 00, 14 | Target Version: v0.37.0

## Error E-002 | Severity: Must Fix | Reporter: Michael DeBellis | Date: 2026-06-16

Issue Description:

The current list of graph database and knowledge graph tools (Neo4j, GraphDB, Stardog, RDFox) omits AllegroGraph by Franz Inc. AllegroGraph is one of the most powerful RDF graph databases, with significant advantages in performance, security, and system integration. The original Pizza.owl tutorial explicitly acknowledges Franz/AllegroGraph/Gruff and uses Gruff in the SHACL discussion. Additionally, Amazon Neptune should be added as it natively supports both Property Graph and RDF graph models.

Suggested Fix:

Add AllegroGraph by Franz Inc. and Amazon Neptune wherever graph databases and knowledge graph tools are discussed. Clarify that OWL ontologies can be loaded into RDF triplestores (AllegroGraph, GraphDB, Stardog, RDFox, Amazon Neptune, Apache Jena/Fuseki) and can also be transformed into property graph systems such as Neo4j, but doing so requires choices about how much OWL semantics, reasoning behavior, and RDF identity structure to preserve.

Status: Pending | Chapters: 08, 14.10 | Target Version: v0.37.0

## Error E-003 | Severity: Must Fix | Reporter: Michael DeBellis | Date: 2026-06-16

Issue Description:

The VegetarianPizza definition contains serious OWL modeling errors. The book uses VegetarianPizza ≡ Pizza AND NOT (hasTopping some MeatTopping), but this is not equivalent to the tutorial's definition—seafood toppings are separate from MeatTopping, so "not meat" would still allow seafood. More critically, the hands-on inconsistency example defines VegetarianPizza as hasTopping only VegetableTopping, which omits both Pizza and CheeseTopping and, due to vacuous truth, any individual with no toppings automatically satisfies this definition, leading to strange over-inferences.

Suggested Fix:

Use the original tutorial definition: VegetarianPizza ≡ Pizza and (hasTopping only (CheeseTopping or VegetableTopping)). Then separately explain that named pizzas need closure axioms such as hasTopping only (MozzarellaTopping or TomatoTopping) before the reasoner can classify them as vegetarian under OWA.

Status: Pending | Chapters: 14.8, 14.9 | Target Version: v0.37.0

## Error E-004 | Severity: Suggested Fix | Reporter: Michael DeBellis | Date: 2026-06-16

Issue Description:

The definition of "executable semantics" is somewhat vague. Chapter 00 provides a useful distinction: EKA requires triggers and actions; without those, a system is a semantic repository, not full EKA. But elsewhere the book says things like "the ontology stops being passive documentation and becomes an executable semantic system" simply because reasoning is involved.

Suggested Fix:

Distinguish between "reasoning-enabled" and "executable" throughout the book. Reserve "executable" for cases where Θ (triggers) and Φ (execution actions) are actually present.

Status: Pending | Chapters: 00, 01, 14.11 | Target Version: v0.37.0

## Error E-005 | Severity: Must Fix | Reporter: Michael DeBellis | Date: 2026-06-16

Issue Description:

The eBook does not include an explicit license statement. Since the original tutorial is under Creative Commons Attribution-ShareAlike 4.0 (CC BY-SA 4.0), a derivative work should clearly state the license and preserve compatible ShareAlike terms.

Suggested Fix:

Add clear CC BY-SA 4.0 license statements to the GitHub repository, eBook file metadata (dcterms:license), and the documentation itself. Being explicit and redundant with license information is good open-source practice.

Status: Pending | Chapters: All | Target Version: v0.37.0

## Error E-006 | Severity: Must Fix | Reporter: Michael DeBellis | Date: 2026-06-16

Issue Description:

The original authors' contributor chain has not been preserved. Michael DeBellis's tutorial states on its first page: "...this version is a revised version of the Protégé 4 Tutorial by Matthew Horridge," and lists previous contributors: Holger Knublauch, Alan Rector, Robert Stevens, Chris Wroe, Simon Jupp, Georgina Moulton, Nick Drummond, and Sebastian Brandt. These names do not appear in the eBook materials.

Suggested Fix:

Add the complete contributor chain in the Acknowledgments section and/or a dedicated Contributors page. Ensure Matthew Horridge and all listed previous contributors receive proper attribution.

Status: Pending | Chapters: Acknowledgments, Contributors | Target Version: v0.37.0

## Error E-007 | Severity: Suggested Fix | Reporter: Michael DeBellis | Date: 2026-06-16

Issue Description:

There are numerous visible typos and awkward expressions throughout the book, including but not limited to: "Classis," "Mearning," "Pallet reasonder," "EAK," "ekecutable," "Standford," "Courese," "concsistency," and so on.

Suggested Fix:

Run the entire manuscript through an LLM or professional proofreading tool and generate a fix report. Consider using spell-checking tools or asking Michael to assist with proofreading.

Status: Pending | Chapters: All | Target Version: v0.37.0