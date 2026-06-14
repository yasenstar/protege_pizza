
| | Domain and Range | Universal Restriction |
| --- | --- | --- |
| Action | Act like "a schema-level semantic rule" | Evaluate "actual semantic behavior" |
| Meaning | Ontology expects "pizzas should connect to pizza toppings" | Ontology expects "whenever pizza toppings exist, the semantic expectations must be satisfied" |

This distinction is especially important for:

> enterprise knowledge governance.

Because semantic quality is rarely protected by **structure alone**.

Instead, ontology must continuously evaluate **relationship meaning.**

Universal restriction therefore behaves like:

> **semantic runtime governance.**

rather than merely structural design.

### 14.8.3 The Critical Differece -- `some` vs. `only`

At this stage, you should clearly recognize that:

> existential restriction (`some`)

and:

> universal restriction (`only`)

are not interchangeable.

Although their syntax may initially appear similar, they represent fundamentally different forms of semantic logic.

Understanding this distinction is one of the most important milestoners in ontology engineering.

Because many ontology beginners mistakenly assume `some` $\approx$ `only` and simply treat them as:

> different OWL keywords.

In reality, they answer **completely different** semantic questions.

Existential restriction asks:

> **"Does at least one qualifying relationship exist?"**

While universal restriction instead asks:

> **"if relationships exist, do they all satisfy semantic expectations?"**

This distinction may appear subtle.

Yet it fundamentally changes:

- reasoning behavior,
- inference outcomes, and
- semantic interpretation.

The following comparison provides a useful summary:

| Characteristic | `some` (Existential Restriction) | `only` (Universal Restriction) |
| --- | --- | --- |
| Core Question | "Must at least one relationship exist?" | "If relationships exist, must they all belong to a certain class?" |
| Semantic Meaning | Minimum existence requirement | Semantic limitation / boundary |
| Creates | Requirement | Constraint |
| Logical Role | Participation condition | Semantic governance |
| Reasoner Behavior | Searches for valid evidence | Searches for invalid evidence |
| Behavior with No Relationship | Not satisfied | Satisfied (don't care) |
| Example | `hasTopping some VegetableTopping` | `hasTopping only PizzaTopping` |

One of the most powerful way to understand the distinction is through:

> **reasoner behavior.**

When ontology evaluates `hasTopping some CheeseTopping`, the reasoner behaves almost like:

> a semantic search engine.

Its task becomes **finding evidence.**

More specifically, the reasoner here asks:

> "Can at least one topping be found that belongs to `CheeseTopping`?"

If ontology identifies `MozzarellaTopping` or `ParmesanTopping`, then the condition succeeds.

Means ontology has found:

> qualifying semantic evidence.

Universal restriction behaves very differently.

Consider `hasTopping only PizzaTopping`, here the reasoner is not searching for **evidence of success.**

Instead, it searches for **evidence of violation!**

The reasoner effectively asks:

> "Do any topping violate semantic expectations?"

If ontology discovers `ChocolateBar` connected through `hasTopping`, while `ChocolateBar` does not belong to `PizzaTopping`, then semantic inconsistency may emerge.

A memorable mental model is:

- `some` $\rightarrow$ `search for qualifying evidence`
- `only` $\rightarrow$ `search for violating evidence`

This distinction becomes extremely useful when ontology models grow larger, into the enterprise scale.

Because enterprise semantic systems increasingly depend upon:

> automated validation

rather than:

> manual review.

Another important difference appears when:

> no relationship exists.

Suppose ontology contains `Pizza_B` with no toppings currently defined.

Would the following condition succeed?

`hasTopping some CheeseTopping`

The answer is:

> **NO.**

Because ontology cannot find evidence showing:

> at least one cheese topping exists.

Existential restriction therefore fails.

Now consider:

`hasTopping only PizzaTopping`

Surprisingly:

> ontology still considers the restriction satisfied.

Why?

Because ontology now finds:

> no invalid toppings.

Universal restriction asks:

> "If toppings exist, are they semantically valid?"

When no toppings exist:

> no violation can be observed.

In formal logic, this behavior is called **vacuous truth**.

Meaning:

> a universal condition remains true unless a counterexample exists.

You do not need to memorize this mathematical term immediately. (see Interesting reading for reference)

However, understanding the behavior is extremebly important.

Because it reveals something fundamental:

> OWL reasoners think logically -- not intuitively.

Human may instinctively say:

> "A pizza without toppings should fail pizza rules."

But ontology behaves differently.

Ontology instead says:

> "No invalid topping exists, therefore no contradiction has been observed."

This distinction becomes increasingly important as learners transition from:

> data modeling

toward:

> logical knowledge modeling.

A useful summary is:

- `some` $=$ `at least one valid relationship must exist`
- `only` $=$ `all relationships must remain semantically valid`

Together, these relationships provide ontology with both:

> participation logic

and:

> semantic discipline.

#### ==== Interesting Reading: Vacuous Truth in Formal Logic ===

The behavior of `only` when no relationship exists -- i.e., it is automatically satisfied -- is not an arbitrary design choice. It follows a fundamental principle in formal logic called **vacuous truth**.

<h3>What is Vacuour Truth?</h3>

In classical logic, a statement of the form:

> *"If $P$, then $Q$"* (written as $P \rightarrow Q$)

is considered **true** whenever the condition $P$ is **false** -- regardless of whether $Q$ is ture or false.

This is not a convention.

It is a logical necessity to avoid contradictions and to preserve the integrity of implication.

**Example in everyday reasoning**:

> *"If it rains, then the ground will be wet.*

If it does **not** rain, the statement is still considered **true** (vacuously true). It makes no claim about the ground's wetness when it doesn't rain. It only promises that *whenever* it rains, wetness follows.

<h3>How Vacuous Truth Applies to "only"</h3>

Recall the semantic meaning of `only`:

> *"If a pizza has a topping, then that topping must be `PizzaTopping`.*

This is a logical implication:

> `hasTopping(pizza, topping)` $\rightarrow$ `PizzaTopping(topping)`

| Scenario | Pizza has topping? | Topping is PizzaTopping? | Implication (Vacuous Truth) |
| --- | --- | --- | --- |
| `Pizza` has `MushroomTopping` | ✅ True | ✅ True | **True** (satisfied) |
| `Pizza` has `ChocolateTopping` | ✅ True | ❌ False | **False** (violated) |
| `Pizza` has **no** toppings | ❌ False | (not evaluated) | **True** (vacuously satisfied) |

The third row is **vacuous truth**. Because the condition "pizza has a topping" is false, the overall `only` rule is automatically satisfied. The ontology does **not** compliain about missing toppings.

<h3>Why Does Logic Include Vacuous Truth?</h3>

Without vacuous truth, logical implication would break down.

Consider the statement:

> *"All humans who can fly are astronauts.*

If there are no humans who can fly, the statement is considered **true** still.

It does not falsely claim that some flying humans exist. It simply states a conditional relationship that happens to be trivially satisfied because the condition never occurs.

This same principle allows `only` to act as a **pure constraint**, not an existence requirement. It governs the *type* of relationships *if they exist*, without forcing them to exist.

<h3>Mathematical Form</h3>

In first-order logic, the universal restriction $\forall x \; (R(x) \rightarrow C(x))$ is **vacuously true** when there is no $x$ that satisfies $R(x)$.

This is written as:

> $\forall x \in \phi, \; C(x)$ is always true.

Or equivalently:

> $\neg \exist x \; (R(x) \land \neg C(x))$

No counterexample exists $\rightarrow$ the statement is true still.

<h3>Why This Matters for Ontology Engineering?</h3>

- `only` **does not require existence** -- it only constrains what can exist.
- `some` **requires existence** -- it actively searches for at least one example.

Understanding vacuous truth prevents the common mistake of expecting `only` to behave like `some`.

> *"Vacuous truth is not a loophole! It is a logical feature that allow `only` to be a pure constraint, not a disguised requirement.*

==== END ====

### 14.8.4 Universal Restriction in Protégé -- `only` as a Semantic Guardian

Have understood the semantic meaning of `only` from both "**logical**" and "**mathematical**" perspective, you are now ready to observe how universal restriction behaves inside Protégé.

As first glance, universal restriction may appear very similar to concepts introduced earlier in Chapter (13) -- Domain and Range.

Because both mechanisms seems to control:

> semantic correctness.

However, both their behavior and purpose are fundamentally different.

- Domain and Range primarily define **structural expectations.**
- Universal restriction instead evaluates **logical consistency.**

This distinction becomes easier to understand through experimentation, in our Protégé.

Suppose we define the following restriction for `Pizza` inside **`SubClass Of`** using:

> `hasTopping only PizzaTopping`

*Note: Since our [common RDF workbook (pizza-ebook.rdf)](./rdf/pizza-ebook.rdf) had been already configured `some` when we practice existential constraint, to support this section without misleading, I'm clean unnecessary setting and create in one separate workbook called [pizza-ebook_14.8.4](./rdf/pizza-ebook_14.8.4.rdf).*

![ch14_12_hasTopping-only-PizzaTopping](img/ch14_12_hasTopping-only-PizzaTopping.png)

![ch14_13_hasTopping-only-PizzaTopping-result](img/ch14_13_hasTopping-only-PizzaTopping-result.png)

This expression tells ontology:

> whenever a pizza contains toppings, all toppings must belong to `PizzaTopping`.

Notice again: ontology is **NOT requiring toppings to exist!**

Instead, ontology governs:

> the semantic validity of toppings if they exist.

To better understand this behavior, let us intentionally construct:

> semantically problematic data.

Create an individual such as `StrangePizza` under `NamedPizza`:

![ch14_14_strangepizza](img/ch14_14_strangepizza.png)

Then create another individual `ChocolateBar` that does **NOT** belong to `PizzaTopping`, let's create under our previous class `NoClassDefined` for simplicity:

![ch14_15_chocolatebar](img/ch14_15_chocolatebar.png)

Now connect them through `StrangePizza hasTopping ChocolateBar` relationship:

![ch14_16_strangepizza-to-chocolatebar](img/ch14_16_strangepizza-to-chocolatebar.png)

At first, Protégé may not immediately indicate a problem.

This sometimes indeed surprises beginners.

Because ontology editors often separate:

> assertion

from:

> reasoning.

Protégé first records:

> stated knowledge.

Only after synchronization does the **reasoner** begin:

> evaluating semantic consequences.

Once the reasoner executes:

> ontology starts logically evaluating the restriction.

Importantly, the reasoner does **NOT** ask:

> "Does this pizza have toppings?"

Instead, it asks:

> "Do all toppings satisfy the expected semantic type?"

This distinction matters!

Because ontology validation focuses on **meaning**, not merely **existence**.

Depending on how the ontology is modeled, several outcomes may occur.

The reasoner may identify **inconsistency**, **unsatisfied class membership**, or **classification failure**.

The exact behavior depends upon whether **disjointness**, **equivalent classes**, or **additional constraints** exist elsewhere in the ontology.

This experiment reveals an important ontology engineering principle:

> universal restriction behaves like a semantic quality monitor.

Rather than merely storing connected relationships, ontology continuously evaluates:

> whether relationships remain semantically trustworthy.

For enterprise architects, this idea is particularly important.

Because many enterprise systems fail not because:

> their relationships are absent,

but because:

> relationships become semantically **polluted**.

Let us look at one example:

an enterprise graph may technically allow following relationship:

`Employee belongsToDepartment Server01`

The relationship exists.

The database accepts it. (Base on the schema design.)

Yet semantically, the meaning is incorrect.

Universal restriction provides a mechanism for ontology to detect such kind of:

> **semantic drift**

before invalid meaning propagates throughout enterprise knowledge models.

A useful way to summarize the distinction is:

- `Range` $\rightarrow$ relationship expectation
- `only` $\rightarrow$ semantic validation

This is why `only` often behaves like:

> a semantic guardian.

Protecting ontology not from **missing data**, but from **"incorrect meaning**.

#### === Interesting Reading: Semantic Drift in Enterprise Knowledge Models ===

Universal restriction (`only`) provides a mechanism for ontology to detect **semantic drift** before any invalid meaning propagates throughout enterprise knowledge models.

Semantic drift occurs when a relationship gradually deviates from its intended meaning over time, often through incremental, seemingly harmless assertions.

For example, an ontology initially enforces:

`Application hostedOn only Infrastructure`

Over months of maintenance, a modeler adds:

`Application hostedOn VendorContract`

Because no `only` constraint was defined for `hostedOn`, the ontology silently accepts this new relationship. Over time, the semantic boundary erodes ("poisoned"). Queries that rely on `hostedOn` to locate `infrastructure` now return `VendorContract`s, breaking impact analysis, security compliance, and also dependency tracing.

**Formally**, semantic drift can be defined as:

> *A gradual violation of the universal restriction $\forall R.C$ where the set of observed relationships $R(x,y)$ expands to include individual $y$ that are not in the intended target class $C$, without the ontology detecting the violation.*

Universal restriction acts as a **semantice invariant**.

The reasoner continuously evaluates:

$\forall x,y: (x,y) \in R \rightarrow y \in C$

If a counter-example appears, the ontology flags an inconsistency or prevents the invalid relation ship from being trusted. This transforms ontology from a passive schema into an active **semantic guardian**, capable of detecting and preventing meaning erosion at scale.

In an enterprise environment, where thousands or millions of relationships may be added/updated by different teams over years, universal restriction becomes an essential tool for maintaining **semantic integrity** across the entire knowledge graph.

=== END ===

## 14.9 Combining `some` and `only` -- The Classis `VegetarianPizza` Pattern

At this stage, you may naturally being asking an important question:

> If existential restriction (`some`) and universal restriction (`only`) solve different semantic problems, can ontology combine them?

The answer is:

> **Yes -- and this is where ontology becomes significantly more powerful!**

In practical ontology engineering, meaningful concepts are rarely defined through **a single restriction.**

Instead, ontology begins expressing:

> **semantic identity through combinations of logical constraints.**

One of the most well-known examples appears in `VegetarianPizza`.

Consider the following OWL definition:

`VegetarianPizza EquivalentTo`<br>
`Pizza`<br>
`and (hasTopping some VegetableTopping)`<br>
`and (hasTopping only VegetableTopping)`

Reflect into Protégé, as below setting:

![ch14_17_vegpizza-combine](img/ch14_17_vegpizza-combine.png)

At first glance, this expression may appear repetitive.

After all, both restrictions reference `VegetableTopping`.

However, each restriction performs a completely different semantic role.

- `hasTopping some VegetableTopping` ensures that **at least one** vegetable topping exists.
- `hasTopping only VegetableTopping` ensures that **every** topping must be a vegetable.

Neither alone is sufficient. Only the combination of `some` and `only` creates a complete semantic definition.

To understand why both are necessary, it wold be helpful to first examine:

> why isolated restrictions are incomplete.

### 14.9.1 Why `some` Alone Is Not Enough?

Suppose ontology only defines `hasTopping some VegetableTopping`, this means:

> at least one vegetable topping must exist.

At first glance, this may seem sufficient to describing:

> a vegetarian pizza.

However, consider the following situation:

`PizzaA hasTopping MushroomTopping`<br>
`PizzaA hasTopping PepproniTopping`

Ontology evaluates `hasTopping some VegetableTopping` and immediately **succeeds.**

Why?

Because ontology finds:

> qualifying evidence.

The pizza contains `MushroomTopping`.

Then the existential condition therefore succeeds.

However, the pizza still contains `PepperoniTopping`, which clearly violates **vegetarian meaning.**

This illustrates an important ontology engineering lesson:

> existential restriction validates **participation** -- NOT semantic purity.

Or more simply, `some` ensures:

> something accetable exists.

But it does **NOT** ensure:

> everything remains acceptable.

The reasoner asks:

> "Can qualifying evidence be found?"

It does **NOT** ask:

> "Are there any violations?"

Semantic meaning therefore remains incomplete.

### 14.9.2 Why `only` Alone Is Not Enough

Now consider the opposite situation.

Support ontology defines `hasTopping only VegetableTopping`.

This restriction states:

> if toppings exists, they must all belong to `VegetableTopping`.

At first glance, this appears semantically stronger.

However, a subtle logical problem emerges.

Image `PizzaB` with no toppings at all.

Surprisingly, ontology still consider `hasTopping only VegetableTopping` to be **satisfied.**

Why?

Because ontology searches for:

> violating evidence.

and in this case:

> no violating topping exists.

This follows the mathematical principle introduced earlier:

> **vacuous truth.**

In formal logic, a universal statement remains **true** unless:

> a counterexample exists.

Ontology therefore concludes:

> nothing violates the rule.

However, from a human perspective, an empty pizza may not intuitively feel like:

> a valid vegetarian pizza.

This highlights an important distinction:

> reasoners think **logically** -- **NOT** intuitively.

Universal restriction provides:

> semantic discipline.

But it does **NOT require participation.**

### 14.9.3 Why Logical Compsition Matters

Ontology becomes significantly more expressive when both restrictions are combined.

Consider again:

`VegetarianPizaa EquivalentTo`<br>
`Pizza`<br>
`and (hasTopping some VegetableTopping)`<br>
`and (ahsTopping only VegetableTopping)`

Together, the restrictions now express two independent requirements:

1. **At least one vegetable topping must exist**, and
2. **All toppings must remain vegetable toppings**.

The first restriction guarantees:

> semantic participation.

The second restriction guarantees:

> semantic consistency.

Only together do they express:

> authentic vegetarian meaning.

This reveals one of ontology engineering's most important principles:

> **meaning rarely emerges from a single rule.**

Instead:

> **meaning emerges from the interaction of multiple logical restrictions.**

A useful mental model can be thought as:

- `some` $\rightarrow$ participation
- `only` $\rightarrow$ discipline

Together, they produce:

> **semantic identity.**

Ontology therefore moves beyond:

> relationship storage

toward:

> governed conceptual meaning.

This is one of the reasons ontology differs fundamentally from traditional databases.

Databases typically store **facts**.

Ontology additionally governs **what facts mean**.

## 14.10 Implementing `some` and `only` in Graph Database - A Neo4j Perspective

At this point, you may reasonably ask:

> If existential and universal restrictions are so powerful, can similar logic be implemented in a graph database such as Noe4j?

The answer is:

> **Yes -- but with important limitations.**

This distinction is particularly important because many enterprise practitioners initially assume:

> **Neo4j = Ontology**

or:

> **Knowledge Graph automatically means semantic intelligence.**

In reality, graph databases and ontologies solve fundamentally different problems.

Neo4j primarily manages **connected data.**

Ontology additionally governs **logical meaning**. (note the "additionally" wording)

A graph database excels at:

- relationship storage,
- graph traversal, and
- connected querying.

However, Neo4j does not natively understand $\exist R.C$ or $\forall R.C$, nor does it automatically infer:

- class membership,
- semantic consistency, or,
- logical identity.

Instead, engineers must explicitly implement semantic behavior through:

> **Cypher queries.**

This becomes easiers to understand using `VegetarianPizza`.

Suppose Neo4j contains below relationship:

`(:Pizza)-[:HAS_TOPPING]->(:Topping)`

You can use below Cypher to create these 2 nodes and 1 relationship (note: this is just for demo purpose, using below query you'll create two actual instances as well):

`CREATE (:Pizza)-[:HAS_TOPPING]->(:Topping)`

![ch14_18_neo4j-pizza-relation-topping](img/ch14_18_neo4j-pizza-relation-topping.png)

A pizza may connect to `MushroomTopping`, `TomatoTopping`, or `PepperoniTopping`.

Following Cypher queries are used to create these new relationships:

```sql
MERGE (p1:Pizza {name:"MyPizza1"})
MERGE (p2:Pizza {name:"MyPizza2"})
MERGE (p3:Pizza {name:"MyPizza3"})
MERGE (t1:Topping {name:"MushroomTopping"})
MERGE (t2:Topping {name:"TomatoTopping"})
MERGE (t3:Topping {name:"PepperoniTopping"})
MERGE (p1)-[:HAS_TOPPING]->(t1)
MERGE (p2)-[:HAS_TOPPING]->(t2)
MERGE (p3)-[:HAS_TOPPING]->(t3)
```

Then you may extract them as below:

![ch14_19_neo4j-mypizza](img/ch14_19_neo4j-mypizza.png)

Neo4j itself does not automatically determine:

> whether the pizza qualifies as vegetarian.

Instead, semantic interpretation must be manually implemented.

> Tip: You may find the working Neo4j dump database in ebook's *neo4j* subfolder.

### 14.10.1 Implementing Existential Restriction (`some`) in Neo4j