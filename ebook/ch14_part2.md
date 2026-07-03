---
export_on_save: true
puppeteer:
  args: ['--no-sandbox']
---

# Chapter 14 -- Semantic Requirements – From Existential Restrictions to Universal Rules (part 2)

Table of Contents:
- [14.5 Existential Restriction in `Pizza.owl` -- Understanding Tutorial 4.10.1 and 4.10.2](#145-existential-restriction-in-pizzaowl----understanding-tutorial-4101-and-4102)
  - [14.5.1 A Detail Look at Existential Restriction](#1451-a-detail-look-at-existential-restriction)
  - [14.5.2 From Semantic Requirements to Executable Queries: The EKA Knowledge Graph Bridge](#1452-from-semantic-requirements-to-executable-queries-the-eka-knowledge-graph-bridge)
  - [14.5.3 Visualized Examine on Tutorial 4.10.1 and 4.10.2](#1453-visualized-examine-on-tutorial-4101-and-4102)
  - [14.5.4 View from Open World Assumption (OWA)](#1454-view-from-open-world-assumption-owa)
- [14.6 Exercise 13 Walkthrough -- Creating Semantic Requirements in Protégé](#146-exercise-13-walkthrough----creating-semantic-requirements-in-protégé)
- [14.7 Understanding Reasoning Outcomes -- Asserted vs. Inferred Semantics](#147-understanding-reasoning-outcomes----asserted-vs-inferred-semantics)
  - [14.7.1 Asserted Semantics -- Explicitly Modeled Knowledge](#1471-asserted-semantics----explicitly-modeled-knowledge)
  - [14.7.2 Inferred Semantics -- Knowledge Derived Through Logic](#1472-inferred-semantics----knowledge-derived-through-logic)
    - [=== Interesting Read: Necessary vs. Sufficient Conditions ===](#-interesting-read-necessary-vs-sufficient-conditions-)
  - [14.7.3 Why Existential Restriction Enables Inference](#1473-why-existential-restriction-enables-inference)
  - [14.7.4 Reasoners Think Logically -- Not Intuitively](#1474-reasoners-think-logically----not-intuitively)


## 14.5 Existential Restriction in `Pizza.owl` -- Understanding Tutorial 4.10.1 and 4.10.2

### 14.5.1 A Detail Look at Existential Restriction

After introducing the conceptual foundation of property restrictions, Michael now transitions toward one of this most important practical modeling techniques in OWL:

> **Existential Restriction**

through the construct `someValuesFrom`.

At this stage in the `Pizza.owl` tutorial, ontology modeling begins changing character.

Earlier chapters largely focused on **describing relationships.**

For example:

> Pizza `hasTopping` PizzaTopping

or:

> Pizza `hasBase` PizzaBase

These statements helped ontology understand:

> semantic structure.

However, ontology still lacked the ability to describe:

> **semantic requirements.**

This distinction is subtle but important.

Because knowing:

> a pizza may have toppings

is fundamentally different from saying:

> a pizza must contain at least one topping.

Ontology therefore begins transitioning from:

> semantic possibility

toward:

> **semantic obligation.**

### 14.5.2 From Semantic Requirements to Executable Queries: The EKA Knowledge Graph Bridge

This transition from "possibility" to "obligation" is not merely an academic logical exercise. Within the EKA framework, it has a very concrete and powerful implication for the **$K$ - Knowledge Graph** layer.

Recall the EKA formalization: $\large{EKA = (K, R, \Theta, \Phi, \Gamma)}$.

- **Without Existential Restrictions ($K$ is a "Descriptive Graph"):** The knowledge graph can only answer "what is" queries. For example, you can ask: *“Which pizzas have a `MozzarellaTopping`?”* This is a simple traversal of asserted relationships.

- **With Existential Restrictions ($K$ becomes an "Intelligent Graph"):** Because the ontology now contains *logical rules* about what *must* exist, the knowledge graph can answer "what should be" and "what is missing" queries.

**Example in a Graph Query (e.g., Cypher or SPARQL):**

You have defined that a `CheesePizza` **must** have at least one `hasTopping` relationship to a `CheeseTopping`. Your knowledge graph contains the following individuals:

1.  `PizzaA` (type: `CheesePizza`) - has a relationship `hasTopping` to `CheddarTopping`.
2.  `PizzaB` (type: `CheesePizza`) - has **no** `hasTopping` relationships.

<div style="page-break-after: always;"></div>

=== Additional Reading, if you have Neo4j on-hand ===

Assume your Neo4j graph contains nodes labeled `Pizza` and `CheeseTopping` (Note: `CheeseTopping` could be member of parent node `PizzaTopping`), connected by a relationship `:HAS_TOPPING`.

Based on above individuals information.

Run this Query 1:

```SQL
MATCH (p:Pizza {type: 'CheesePizza'})
RETURN p.name AS PizzaName
```

You may get result as:

| PizzaName |
| --- |
| PizzaA |
| PizzaB |

Both pizzas are returned, even though `PizzaB` has no toppings.

Then run this Question 2:

```SQL
MATCH (p:Pizza {type: 'CheesePizza'})
WHERE (p)-[:HAS_TOPPING]-(>:CheeseTopping)
RETURN p.name AS ValidCheesePizzaName
```

You should see the result now as:

| ValidCheesePizzaName |
| --- |
| PizzaA |

Only `PizzaA` is returned. `PizzaB` is excluded because it does not satisfy the "must have at least one cheese topping" rule.

From knowledge graph perspective:

- Query 1 represents a **descriptive knowledge graph**: it simply tells you what is asserted, but it cannot distinguish between a valid `CheesePizza` (with toppings) and an invalid or incomplete one.
- Query 2 represents the **existential restriction logic** (`hasTopping some CheeseTopping`) enhancing the knowledge graph: it queries only those individuals that *satisfy the semantic requirement*, this turns your ontology's logical rules into powerful, executable data quality filters.

In an EKA-enabled systems, Query 2 would be the basis for generating trustworthy insights, while Query 1 might be used for auditing or identifying data quality issues (i.e., finding `PizzaB` to flag it for correction).

=== END ===

**Without the existential restriction** (i.e., using only RDFS/SHACL), both `PizzaA` and `PizzaB` are valid members of `CheesePizza`. A query would simply return both.

**With the existential restriction** (using OWL and a reasoner), the semantic layer within EKA ($R$) can first validate the graph. It would identify `PizzaB` as **incomplete** or **inconsistent** based on the logical rule you defined in the ontology.

This allows the **Executable Intelligence ($\Phi$)** layer to trigger actions. A governance workflow could automatically flag `PizzaB` for a data quality issue, or a smart query could be written to exclude it from results.

**Therefore, Chapter (14) is the pivotal moment where your ontology stops being a mere "schema" for your knowledge graph and becomes its "logical guardian."** The existential restriction (`someValuesFrom`) is your first tool to enforce business rules ("a product must have a category", "a critical application must have an owner") directly within your executable knowledge architecture.

### 14.5.3 Visualized Examine on Tutorial 4.10.1 and 4.10.2

Michael introduces existential restriction through a very deliberate modeling progression.

Rather than immediately creating complicated class logic, you first explore a simple but powerful idea:

> classes may be described through required relationships.

This introduces a major ontology engineering concept:

> **logical class definition.**

See below steps which described in Exercise 13 and result `Pizza hasBase some PizzaBase`:

![ch14_02_pizza-some-pizzabase](img/ch14_02_pizza-some-pizzabase.png)

Previously, you manually create classes primarily through naming and hierarchy.

For example:

> `MargheritaPizza`

may simply exist as:

> a subclass of `NamedPizza`.

However, ontology still does not truly understand:

> what semantically makes a `MargheritaPizza` a `MargheritaPizza`.

Existential restriction changes this.

Ontology can now begin expression:

> semantic identity.

For example:

Instead of simply naming:

> `CheesePizza`,

ontology may define:

> a pizza having at least one cheese topping.

See how to implement this in Protégé and resulting `CheesePizza hasTopping some CheeseTopping`:

![ch14_03_cheesepizza-some-cheesetopping](img/ch14_03_cheesepizza-some-cheesetopping.png)

Since `CheesePizza` is SubClass Of `Pizza`, in the result Description screen, you may see the previous Pizza / PizzaBase existential restriction is inherited, as below:

![ch14_04_existential-inherit](img/ch14_04_existential-inherit.png)

This ensure your ontology grows organically base on the known and true knowledge already have.

With such kind of configuration, your ontology is transformed fundamentally.

Meaning becomes:

> computable.

Reasoners may now determine:

> class membership automatically.

Ontology therefore becomes increasingly **inferential** rather than merely **descriptive!**

This represents one of the earliest moment where ontology begins feeling:

> intelligent.

Because class meaning no longer depends entirely upon:

> human categorization then manually configuration.

Instead:

> **logical semantics drive understanding based on machine-understandable rules.**

Within our `Pizza.owl`, existential restriction is intentionally introduced before more advanced logical restrictions because it establishes the foundational reasoning pattern:

> **required existence.**

Ontology first learns:

> something must exist.

Later chapters will teach ontology:

- what is allowed,
- what is limited, and
- how many relationships are acceptable.

This gradual semantic progression is one reason the `Pizza.owl` tutorial remains such an effective learning path.

Because ontology maturity develops incrementally.

### 14.5.4 View from Open World Assumption (OWA)

Interestingly, OWL reasoners do not immediately assume that a restriction has been violated simply because a required relationship has not yet been observed. In many cases, the absence of information does not necessarily imply semantic inconsistency. This behavior is closely related to one of the most important principles in ontology engineering:

> **Open World Assumption (OWA)**

which assumes that knowledge may still be incomplete.

We will explore this important concept in greater detail later in this chapter, as it fundamentally influences how OWL reasoners interpret existential restrictions and semantic requirements.

A quick example:

Suppose the ontology only knows `PizzaA `exists, with no `hasTopping` statements. Under OWA, the reasoner does not conclude `PizzaA` has no toppings. It concludes “unknown”. This is why `PizzaA` does not violate `hasTopping` `some` `CheeseTopping` — *absence of evidence is not evidence of absence.*

We will revisit OWA in detail when discussing vacuous truth (14.8.3) and reasoner behavior (14.7.4).

## 14.6 Exercise 13 Walkthrough -- Creating Semantic Requirements in Protégé

With the conceptual foundation now established, you are fully ready to perform:

> Exercise 13

inside Protégé.

This exercise represents an important turning point.

For the first time, you begin configuring:

> semantic requirements

rather than merely:

> semantic structure (hierarchies and relationships).

Inside the `Pizza.owl` tutorial, you create existential restrictions using:

> `someValuesFrom`

through the Protégé interface (you already see screen samples in previous section).

At first glance, the interface interaction appears simple.

However, conceptually, something profound is happening.

Ontology is beginning to describe:

> **what a class must satisfy.**

rather than merely:

> what relationships **may** exist.

Inside Protégé, you first select the target class.

Typically, Michael demonstrates this through `pizza` subclasses that require particular toppings.

You then navigates to **`Equivalent Classes`** or `**SubClass Restrictions**` depending on modeling preference.

![ch14_05_class-restriction](img/ch14_05_class-restriction.png)

Next, Protégé provides access to:

> Object Restriction Editor.

"Editor" may not the accurate word, see below screen, you may perform more configurations here, including:

- Class expression editor
- Class hierarchy
- Data restriction creator
- Object restriction creator

![ch14_06_restriction-dialog](img/ch14_06_restriction-dialog.png)

At this stage, switch to actual tab name "Object restriction creator", you may perform following steps:

1) Select **Restriction Type**: `Some (existential)` means `someValuesFrom`, it's the default selection when you come to this screen, then
2) Configure **Property** in "Restricted property": `hasTopping`, and finally
3) Configure **Target Class**  in "Restriction filler"

At first encounter, this may look like "Syntax".

However, ontology engineers should resist thinking about this merely as notation.

Because what has actually been created is:

> **semantic logic.**

Ontology now interprets this statement as:

> there must exist at least one topping relationship pointing toward mozzarella topping.

This changes how ontology understands "pizza identity".

A pizza now becomes classified not merely because:

> a human named it,

but because:

> semantic conditions are satisfied.

This subtle shift becomes extremely relies upon:

> inferred meaning.

rather than:

> manually asserted meaning.

=== Mathematical View ===

Let's try to map what you've configured to the previous mathematical formula:

$\exists R.C = \{ x \in \Delta^\mathcal{l} \mid \exists y \in \Delta^\mathcal{l} : (x,y) \in R^\mathcal{l} \land y \in C^\mathcal{l} \}$

The statement:

> `CheesePizza` `hasTopping` some `CheeseTopping`

may have those elements referring to the variables as:

- $\Delta^\mathcal{l}$: the `Pizza` class domain
- $R$: `hasTopping` relationship
- $C$: `CheesePizza` class
- $x,y$: instance of `Pizza` (not `CheesePizza`)

> [!Note] A subtle but important note on x and class definitions:

> In the formula $\exists R.C = \{ x \in \Delta^\mathcal{l} \mid \exists y \in \Delta^\mathcal{l} : (x,y) \in R^\mathcal{l} \land y \in C^\mathcal{l} \}$, the variable x ranges over instances of the class being defined. When you define `CheesePizza` as `Pizza and (hasTopping some CheeseTopping)`, the restriction is evaluated in the context of `Pizza`. This means x is an instance of `Pizza` (not necessarily an instance of `CheesePizza`). The restriction then asks: does this `Pizza` instance have at least one `hasTopping` relationship to a `CheeseTopping`? If yes, the reasoner can infer that the instance is also a `CheesePizza`. This is why x is an instance of `Pizza` in the formula – the restriction acts as a membership test for the subclass, not as a property of the subclass itself.

=== END ===

Exercise 13 therefore marks another maturity transition.

Ontology is beginning to evolve from:

> a semantic graph

toward:

> **semantic intelligence.**

> **Important Note on Inference Materialization**
>
> As you complete Exercise 13 and run the reasoner, you will observe inferred classifications appearing in Protégé's interface. It is important to understand how these inferences are handled.
>
> In Protégé's default desktop workflow, reasoner results are shown as **inferred axioms** -- they are displayed visually (e.g., in the class hierarchy or individuals view) but are **NOT automatically saved as asserted axioms** into the ontology file. This allows you to review and validate reasoning outcomes before deciding whether to make them permanent.
>
> However, this is a tool-specific behavior, not a universal principle of OWL reasoning. In production-grade semantic systems -- including triplestores, rule-enabled graph databases, and enterprise knowledge graph platforms -- inferred triples may be:
> - **Materialized and persisted** (written back to storage),
> - **Maintained as inferred closures** (updated incrementally), or
> - **Exposed virtually** (computed on-the-fly at query time),
>
> depending on the system architecture and configuration.
>
> *The author here gratefully acknowledge **Michael DeBellis** for his expert technical review and clarifying this critical engineering distribution. The corrected wording in this note borrows directly from his suggestions. (Ref: GitHub Issue #9 (https://github.com/yasenstar/protege_pizza/issues/9))*
>
> With this understanding in place, let us now examine how existential restrictions enable reasoning outcomes...

## 14.7 Understanding Reasoning Outcomes -- Asserted vs. Inferred Semantics

After completing Exercise 13 and defining existential restrictions inside Protégé, learners may often encounter an interesting experience:

> the ontology reasoner appears to "know" things that were never manually entered.

At first glance, this may seem surprising.

Especially for readers who are more familiar with **transitional databases** or **graph databases**.

Because in those environments, data generally behaves according to a straightforward principle:

> what is **explicitly** stored is what exists.

Ontology reasoning behaves very differently.

Within OWL, semantic meaning is not limited only to:

> manually asserted facts.

Instead, reasoners are capable of producing:

> **inferred knowledge**

through logical interpretation.

This distinction represents one of the most important conceptual shifts in ontology engineering.

Because ontology gradually moves from:

> storing semantic information

toward:

> **deriving semantic meaning.**

To understand this transformation, you must first distinguish between:

**Asserted Semantics** and **Inferred Semantics**.

### 14.7.1 Asserted Semantics -- Explicitly Modeled Knowledge

Asserted semantics represent:

> information explicitly created by ontology engineers.

In other words:

there are semantic statements that humans intentionally model inside Protégé (or other ontology editors).

For example:

Suppose an ontology engineer manually creates (models):

`PizzaA hasTopping MozzarellaTopping`

This relationship becomes:

> asserted knowledge.

Because it was directly entered into the ontology.

Similarly:

if the ontology engineer manually states:

`PizzaA rdf:type NamedPizza`

this classification is likewise **asserted.**

Ontology does not need to infer it.

The semantic meaning already exists because:

> humans explicitly provided it.

From a modeling perspective, asserted semantics resemble:

> manually curated knowledge.

This is conceptually similar to:

> records stored in a database

or:

> relationships stored in a graph database.

However, ontology does not stop there.

### 14.7.2 Inferred Semantics -- Knowledge Derived Through Logic

Unlike asserted knowledge, inferred semantics are **not manually entered.**

Instead, they emerge through **semantic reasoning.**

> [!Note]
> Scared? Does this mean machine starts dominating semantic creation? Terminator? Skynet?... No worry, this is still the governed logic, rooted from human's initial design!

And, this is where existential restriction becomes especially important.

Consider the following ontology definition:

`CheesePizza EquivalentTo`<br>
`Pizza`<br>
`and (hasTopping some CheeseTopping)`

In Protégé, you may use below steps to add this definition:

![ch14_07_cheesepizza](img/ch14_07_cheesepizza.png)

After confirm, you may see this definition under `Equivalent To`:

![ch14_08_cheesepizza-setting](img/ch14_08_cheesepizza-setting.png)

This statement establishes a semantic condition.

Meaning:

> any pizza containing at least one cheese topping qualifies as a `CheesePizza`.

Note here we have the combination of more than one conditions (restrictions).

Now suppose ontology engineers explicitly model:

`PizzaA hasTopping MozzarellaTopping`

And ontology already understand:

`MozzarellaTopping SubClassOf CheeseTopping`.

Interestingly, magic happens:

ontology engineers never explicitly declare:

`PizzaA rdf:type CheesePizza`

Yet after synchronizing the reasoner, Protégé may automatically infer:

`PizzaA rdf:type CheesePizza`

See from below comparison screen:

|||
| --- | --- |
| Before Reasoning | ![ch14_09_PizzaA-before-reasoning](img/ch14_09_PizzaA-before-reasoning.png) |
| After Reasoning | ![ch14_10_PizzaA-after-reasoning](img/ch14_10_PizzaA-after-reasoning.png) |

This is a significant milestone!

Because ontology has now moved beyond:

> semantic storage

toward:

> **semantic interpretation.**

Meaning becomes **computable**.

The ontology reasoner analyzes:

- subclass hierarchy
- property restrictions
- existential conditions
- logical consistency, and
- **devices new knowledge**

This capability is one of the major distinctions separating ontology from:

> conventional graph data models.

Because ontology is capable of generating:

> **new semantic understanding**

rather than merely retrieving stored relationships.

#### === Interesting Read: Necessary vs. Sufficient Conditions ===

The inference you just witnessed (`PizzaA` automatically classified as `CheesePizza`) depends on a fundamental logical distinction: the difference between **necessary** and **sufficient** conditions.

In Description Logic (the formal language behind OWL):

- **$\texttt{SubClassOf} (\sqsubseteq)$** defines a *necessary* condition.
- **$\texttt{EquivalentTo} (\equiv)$** defines *necessary and sufficient* conditions.

**Mathematical form:**

| Concept | DL Notation | OWL Construct | Logical Direction |
| --- | --- | --- | --- |
| Necessary condition | $C \sqsubseteq D$ | `SubClassOf` | $C(x) \rightarrow D(x)$ |
| Necessary and sufficient condition | $C \equiv D$ | `EquivalentTo` | $C(x) \leftrightarrow D(x)$ |

**Example from this section:**

You defined:

`CheesePizza EquivalentTo`<br>
`Pizza`<br>
`and (hasTopping some CheeseTopping)`

This means:
- **Necessary condition**: If something is a `CheesePizza`, it **must** have a cheese topping.
- **Sufficient condition**: If something has a cheese topping, it **can be inferred** to be a `CheesePizza`.

This is why the reasoner performed *automatic classification*. If you had used `SubClassOf` instead of `EquivalentTo`, the reasoner would **not** perform the reverse inference (from having a cheese topping to classifying as `CheesePizza`).

**Why this matters for your modeling choices:**

| If you want... | Use... |
| --- | --- |
| Only inheritance (one-way) | `SubClassOf` |
| Logical definition with automatic classification (two-way) | `EquivalentTo` |

This distinction is fundamental to ontology engineering. Choosing the wrong construct may lead to unexpected reasoning results (or missed inferences).

=== END ===

### 14.7.3 Why Existential Restriction Enables Inference

At this stage, you may naturally ask an important question:

> Why does existential restriction enable automatic classification?

The answer lies in the semantic meaning of the keyword:

> `some`

which represents:

> **existential quantification.**

Without OWL semantics, the expression `hasTopping some CheeseTopping` does not merely describe:

> a relationship.

Instead, it defines:

> **a logical test condition.**

More specifically, ontology interprets this expression as:

> there must exist **at least one** valid relationship through `hasTopping` pointing to an individual belonging to class `CheeseTopping`.

This subtle distinction is important.

Because ontology is not longer simply storing:

> semantic data,

but rather evaluating:

> **semantic conditions.**

In practice, ontology reasoners perform a process conceptually similar to searching for evidence.

The reasoner examines individuals inside the ontology and asks a logical question:

> "Can I find at least one relationship satisfying this existential condition?"

Suppose ontology contains:

`PizzaA hasTopping MozzarellaTopping`

and ontology already understands:

`MozzarellaTopping SubClassOf CheeseTopping`

The reasoner may then evaluate: `hasTopping some CheeseTopping` and conclude:

> YES - at least one valid successor individual exists.

This reasoning process may feel surprisingly intelligent, since it makes machine alike human.

However, semantically, the reasoner is performing something conceptually similar to:

> an automated semantic query.

Readers with graph databases experience may recognize an interesting parallel.

Inside Neo4j, a developer might write a Cypher query similar to:

```SQL
MATCH (p:Pizza)-[:HAS_TOPPING]->(t:CheeseTopping)
RETURN p
```

or conceptually:

```SQL
WHERE (p)-[:HAS_TOPPING]->(:CheeseTopping)
```

to locate pizzas having cheese toppings.

Ontology reasoners perform a related form of semantic evaluation.

However, instead of merely returning query results, the reasoner may additionally:

> **derive new semantic classifications.**

Meaning:

if a pizza satisfies the logical condition: `hasTopping some CheeseTopping`, the ontology reasoner may automatically conclude:

> this individual belongs to `CheesePizza` (class).

This introduces an important distinction between **graph traversal** and **semantic reasoning.**

- Graph database primarily discover **existing connections**.
- Ontology reasoners additionally derive **new meaning**!

Another important factor enabling inference is `EquivalentTo`.

Consider the following ontology definition:

`CheesyPizza EquivalentTo`<br>
`Pizza`<br>
`and (hasTopping some CheeseTopping)`

The keyword `EquivalentTo` represents:

> **necessary AND sufficient conditions**

This means the semantic rule works in **both directions.**

Ontology understands:

1. If something is a `CheesePizza`, it must satisfy the topping condition, and also
2. If something satisfies the topping condition, it may be classified as `CheesePizza`.

This bidirectional logic is extremely important.

Because it enables:

> **automatic classification.**

By comparison:

`CheesyPizza subClassOf (hasTopping some CheeseTopping)` would only define:

> a one-way semantic rule.

Meaning:

> every `CheesyPizza` must have cheese toppings,

but ontology would **not automatically infer** that:

> every pizza with cheese toppings becomes `CheesyPizza`.

This subtle modeling distinctions has major consequences for reasoning behavior.

And it highlights an important principles of ontology engineering:

> **small changes in logical constructors may produce significant different inference outcomes.**

Existential restriction therefore becomes one of the foundational mechanisms enabling ontology to evolve from:

> semantic structure

toward:

> **semantic intelligence.**

### 14.7.4 Reasoners Think Logically -- Not Intuitively

One of the most important mindset shifts in ontology engineering is learning that:

> ontology reasoners think logically,

not:

> **intuitively.**

From many learners, this initially feel unfamiliar and sometimes difficult to understand.

Because our humans naturally interpret missing information by making assumptions.

Ontology reasoners, however, do not (or we may also say "never") make assumption.

They follow:

> **formal logical evidence.**

This distinction becomes especially visible when working with **existential restrictions.**

Consider the following situation.

Suppose an ontology contains an individual `PizzaB` but no topping information has yet been defined.

A human reader may immediately think:

> "If no topping exists, then `PizzaB` is obviously not a `CheesyPizza`, although it has `Pizza` inside the name."

This conclusion feels natural, to humans.

After all, human reasoning frequently relies on:

> incomplete information and educated assumptions.

However, an OWL reasoner behaves differently.

The ontology reasoner does **not infer**:

> `PizzaB rdf:type CheesyPizza`

Yet importantly: the reasoner also does **not infer**:

> `PizzaB` is *not* a `CheesyPizza`.

Instead, ontology reaches a more conservative conclusion:

> **there is currently insufficient information to determine classification.**

In other words, the ontology simply says:

> **"I do not know yet."**

This behavior often surprises beginners.

Especially those with experience in

> relational databases,

> business rules engines,

or:

> graph databases.

Because many traditional systems implicitly follow a different assumption:

`Missing information = false`

Ontology reasoning, however, follows one of the most important principles in semantic modeling:

> **Open World Assumption (OWA)**

Under OWA: missing information does not imply **falsity.**

Instead, ontology assumes **knowledge may still be incomplete**.

Meaning:

> future information may still arrive, just not available for now yet.

For example:

The ontology may later receive `PizzaB hasTopping MozzarellaTopping` and ontology already understands `MozzarellaTopping SubClassOf CheeseTopping`.

At that moment, the reasoner may suddenly infer:

`PizzaB rdf:type CheesyPizza`

What has been changed?

Not the logical rule.

Only:

> **the available evidence (information).**

Ontology reasoning therefore behaves less like:

> guessing,

and more like:

> **evidence-based semantic evaluation.**

This distinction becomes clearer when comparing **Human Intuition** vs **OWL Reasoning**:

| Human Intuition | OWL Reasoning Logic |
| --- | --- |
| No topping observed $\rightarrow$ probably not cheese pizza | No evidence observed (got) $\rightarrow$ classification postponed |
| Missing information suggest absence | Missing information may simply be incomplete |
| Infer based on assumptions | Infer based on formal evidence |

Notice the key difference?

OWL reasoners do not ask "What is most likely true?"

Instead, they ask "What can be logically justified?"

This distinction becomes especially important when working with:

> existential restrictions.

Earlier in this chapter, we defined:

`CheesyPizza EquivalentTo`<br>
`Pizza`<br>
`and (hasTopping some CheeseTopping)`

The keyword `EquivalentTo` defines:

> **necessary and sufficient conditions.**

Meaning:

> ontology interprets the definition in **both directions.**

This enables the reasoner to conclude:

> if a pizza satisfies the existential condition, then it may be classified as `CheesyPizza`.

However, imagine the ontology instead used:

`CheesyPizza SubClassOf (hasTopping some CheeseTopping)`

This semantic meaning changes significantly.

Now ontology only understands:

> every `CheesyPizza` must satisfy the topping restriction.

But ontology can no longer conclude:

> every pizza satisfying the restriction automatically becomes `CheesyPizza`.

The inference direction becomes **one-way only.**

This subtle distinction between `EquivalentTo` and `SubClassOf` has major consequences for ontology behavior.

It also highlights an important engineering lesson:

> ontology reasoners execute logic exactly as modeled

while NOT:

> as human intended.

For ontology engineers, this carries important practical implications.

Semantic models must be designed **precisely** with careful attentions to:

- logical meaning,
- restriction semantics, and
- inference consequences.

At the same time, Open World Assumption provides an important advantage.

Because enterprise knowledge is often:

- incomplete,
- distributed, or
- continuously evolving.

OWL therefore remains highly suitable for enterprise knowledge graphs, semantic integration, and executable intelligence systems when meaning must gradually emerge from **accumulating knowledge** rather than requiring perfect information from the beginning.

As you continue through this chapter, Open World Assumption will become increasingly important for understanding:

> why ontology reasoners sometimes appear surprisingly conservative,

yet remain remarkably powerful in semantic interpretation.

---

Last Updated at: 2026-07-03