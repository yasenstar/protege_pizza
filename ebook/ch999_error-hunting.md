# Error Found: A Living Document Invitation

- [Chapter Introduction](#chapter-introduction)
- [What Kinds of Errors Might You Find?](#what-kinds-of-errors-might-you-find)
- [How to Report an Error](#how-to-report-an-error)
  - [Step 1: Verify the Error](#step-1-verify-the-error)
  - [Step 2: Choose Your Contribution Method](#step-2-choose-your-contribution-method)
  - [Step 3: Use the Error Report Template](#step-3-use-the-error-report-template)
- [Error Report](#error-report)
  - [Step 4: A Note on Tone](#step-4-a-note-on-tone)
- [What Happens After Your Report?](#what-happens-after-your-report)
  - [For Issues](#for-issues)
  - [For Pull Requests](#for-pull-requests)
  - [Versioning and Updates](#versioning-and-updates)
- [Contributors](#contributors)
- [The Spirit of Open Technical Writing](#the-spirit-of-open-technical-writing)
- [Quick Reference: Error Reporting Links](#quick-reference-error-reporting-links)
- [Final Request](#final-request)

## Chapter Introduction

No technical book is perfect -- including this one.

Despite countless hours of writing, reviewing, testing, and refining, errors inevitably remain still. Some my be typographical. Others may be technical inaccurancies. A few might be conceptual oversights or outdated patterns that better approaches have since clarified.

This chapter exists for one reaon:

> **to invite you, the reader, to help make this book better!**

Ontology engieering is a living discipline. Semantic technologies evolve. Best Practices mature. New tools introduce. And with your help, this book can evolve alongside them.

This chapter serves three purposes:

1. **Acknowledging imperfection** -- No author has all the answers. I have done my best, but I'm certain errors remain.
2. **Providing a structured error reporting process** -- So you know exactly how to contribute.
3. **Celebrating community contributions** -- Because open knowledge grows stronger when many minds refine it together.

## What Kinds of Errors Might You Find?

Before you begin searching ("hunting"), let me help you understand what to look for.

Errors in a book could like this typically fall into below categories:

| Error Category | Description | Sample Types |
| --- | --- | --- |
| Technical Errors | These are factual mistakes about OWL, Protégé, RDF, reasoning, or the EKA framework itself | <li>Incorrect OWL syntax</li><li>Misleading logical statements</li><li>Reasoning behavior errors</li> |
| Conceptual Errors | These are misunderstandings or oversimplifications that might mislead readers about deeper semantic principles. | <li>Oversimplified distinctions</li><li>Missing nuance in OWL</li><li>Confusing concepts</li> |
| Typographical and Grammatical Errors | These are the "small stuff" -- but small fixes improve readability and professionalism. | <li>Misspellings</li><li>Missing words</li><li>Inconsistent terminology</li> |
| Outdated or Deprecated Patterns | Ontology engineerng tools and standards evolve. What was best practice in 2025 may be outdated by 2028. | <li>Deprecated reasoner features</li><li>Outdated plugin names</li><li>Evolving OWL 2 features<li> |
| Structural and Pedagogical Issues | These are not "errors" per se, but opportunities to improve learning effectiveness. | <li>Unclear explanations<li><li>Missing prerequisites</li><li>Exercise ambiguity</li><li>Brokden cross-reference</li> |

## How to Report an Error

Great, you catch one 😊! Your contribution are sincerely appreciated.

Please follow this structured process so I can address your feedback efficiently.

### Step 1: Verify the Error

Before reporting, please:

1. **Check the latest version** -- The error may have already been fixed in a new commit. Visit the repository: https://github.com/yasenstar/protege_pizza
2. **Re-read the relevant section carefully** -- Ensure you haven't misinterpreted the text. OWL semantics can be counter-intuitive, especially around *Open World Assumption*.
3. **Test in Protégé** -- If the error is technical, actually try it in Protégé with a reasoner running. Your real-world testing in invaluable.

### Step 2: Choose Your Contribution Method

You have two options:

| Method | Best for | Link |
| --- | --- | --- |
| GitHub Issue | Reporting errors without proposing specific fixes | [Open an issue $\rightarrow$](https://github.com/yasenstar/protege_pizza/issues) |
| Pull Request | Proposing direct corrections (typos, code examples, clarifications) | [Open a Pull Request $\rightarrow$](https://github.com/yasenstar/protege_pizza/pulls) |

### Step 3: Use the Error Report Template

**For Issues (no fix proposed)**, I've configured this template in repository already:

=== Template Start===

## Error Report

**Chapter:** [e.g., Chapter 14]

**Section:** [e.g., 14.5.2]

**Page/Line:** [if applicable]

**Error Type:** (Technical / Conceptual / Typographical / Outdated / Pedagogical)

**Current Text:**
> [Quote the exact text that contains the error]

**Suggested Correction:**
> [Describe what should replace it, or why it is wrong]

**Reasoning:**
> [Explain why this is an error — cite OWL specification, reasoner behavior, or logical principles]

**Additional Context:**
> [Protégé version, reasoner used, screenshots if helpful]

=== Template End===

**For Pull Request (fix proposed):**

If you are comfortable with Git and Markdown, welcome directly edit the `.md` file in the `ebook/` directory.

Your pull request should:

1. Target the `main` branch
2. Describe what you changed and why
3. Reference any related issue (if applicable)

I will review all pull requests as quickly as possible.

### Step 4: A Note on Tone

All feedback is welcome and appreciated -- including critical feedback. However, please follow the **principle of charitable interpretation.**

- Assume good faith.
- Assume the error was accidental, not intentional.
- Assume I genuinely want to fix it.

Rude or dismissive reports will be closed. Thoughtful, respectful reports will be treasured.

## What Happens After Your Report?

### For Issues

1. **Acknowledgment** -- I will respond within 7 days (try my best) confirming receipt.
2. **Validation** -- I will verify the error independently (re-testing in Protégé, reviewing OWL specifications, or any other tools).
3. **Resolution** -- Depending on severity, I will either:
   - Fix immediately (for minor typos or clear technical errors)
   - Schedule for next revision (for conceptual clarifications or structural improvements)
   - Mark as "won't fix" with explanation (if the report is incorrect or based on misunderstanding)

### For Pull Requests

1. **Review** -- I will test your proposed changes locally.
2. **Feedback** -- If adjustments are needed, I will comment inline.
3. **Merge** -- Once approved, your contribution becomes part of the book.
4. **Attribution** -- Your name (or GitHub handle) will be added to the [`Contributors`](./contributors.md) section below.

### Versioning and Updates

The book is a living document. When errors are fixed:

- A new commit will be pushed to the repository
- The PDF and EPUB will be regenerated (periodically)
- A [`CHANGELOG.md`](./CHANGELOG.md) will track significant corrections

You can always find the latest version at `ebook` folder of https://github.com/yasenstar/protege_pizza.

## Contributors

The following invididuals have contributed error reports, corrections, or improvements to this book. (also in the dedicated contributors file)

| Name / GitHub Handle | Contribution Type | Chapter(s) | Date|
| --- | --- | --- | --- |
| *Your name here* | *Error report / Pull request* | *X* | *YYYY-MM-DD* |

**This space is reserved for you.**

When you report an error that leads to a correction, your name will be added here with my sincere thanks.

## The Spirit of Open Technical Writing

This chapter exists because I believe in a specific philosophy of technical education:

> Books are not monuments. Books are conversations.

When you read a chapter and find an error, you are not "criticizing" the author. You are **contributing the work** of making knowledge clearer, more accurate, and more useful.

Every technical book ever written contains errors. The only question is whether those errors remain hidden or become opportunities for improvement.

By opening this chapter, by inviting you to report errors, by publishing the entire book on GitHub (and fine formatted to LeanPub), I am choosing the second path.

This book is not finished. It will never be finished. And that is exactly as it should be.

Because ontology engineering itself is a living discipline. The Semantic Web evolves continuously. Protégé development keep updates. Reasoners improves. New enterprise challenges emerge. And this book will evolve alongside them -- with your help!

**You are not just a reader. You are a co-creator.**

## Quick Reference: Error Reporting Links

| Action | Link |
| --- | --- |
| Report an error (no fix) | [Open an Issue $\rightarrow$](https://github.com/yasenstar/protege_pizza/issues) |
| Propose a correction | [Open a Pull Request $\rightarrow$](https://github.com/yasenstar/protege_pizza/pulls) |
| View the latest version | [Repository Main $\rightarrow$](https://github.com/yasenstar/protege_pizza) |
| Browse the eBook directory | [ebook/ $\rightarrow$](https://github.com/yasenstar/protege_pizza/tree/main/ebook) |

## Final Request

Before you close this book and move on with your day, please consider:

> **Did you find anything in this book that confused you?**

That confusion -- even if not a "technical error" -- is worth reporting. Unclear explanations are a kind of error too. If something took you three readings to understand, that section could be improved.

> **Did you find a type, a missing word, or an inconsistent term?**

Thos are trivial to fix and make the book more professional. Pleae report them.

> **Did you try an example in Protégé and get a different result than the book described?**

That is the most valuable report of all. Real-world testing trumps theoretical writing every time.

Thank you for reading. Thank you for learning. And thank you, in advance, for helping make this book better.

---

Last updated: 2026-06-12<br>
Repository: https://github.com/yasenstar/protege_pizza<br>
Author contact: GitHub Issues (preferred) or via YouTube channel

*The best books are those are acknowledge they are never truly finished -- only temporarily improved!*