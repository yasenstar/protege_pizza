# 🍕 Mastering Ontology Engineering with Protégé and Pizza.owl

[![GitHub stars](https://img.shields.io/github/stars/yasenstar/protege_pizza)](https://github.com/yasenstar/protege_pizza/stargazers)
[![YouTube Course](https://img.shields.io/badge/YouTube-Playlist-red?style=for-the-badge&logo=youtube)](https://www.youtube.com/playlist?list=PL6DEHvciXKeUx4P32B3hKMK1t6mC8RhwW)
![License: GPL-3.0](https://img.shields.io/badge/Code-GPL--3.0-blue.svg) ![License: CC BY-SA 4.0](https://img.shields.io/badge/Content-CC--BY--SA--4.0-lightgrey.svg)
[![Leanpub](https://img.shields.io/badge/Leanpub-Available-brightgreen?style=for-the-badge&logo=leanpub)](https://leanpub.com/pizza-owl-ontology-practice-volume1)
[![Kindle](https://img.shields.io/badge/Kindle-Available-orange?style=for-the-badge&logo=amazonkindle)](https://www.amazon.com/gp/product/B0H9D94LBP)

## Project Vision

This repository is the official engineering environment for the "Mastering Ontology Engineering" project, providing a professional roadmap from semantic foundations to **Executable Knowledge Architecture (EKA)**. This project transforms the legendary Pizza OWL tutorial into a deep-dive professional experience, connecting ontology theory, Protégé operations, and real-world knowledge graph implementation.

---

## 📚 Companion eBook — Now Available in Two Volumes!

The complete companion eBook is now available in two volumes, published on both **Leanpub** and **Amazon Kindle (KDP)**.

### Volume 1: From Foundations to Reasoning

**Build Your First Ontology. Master Semantic Reasoning. Lay the Groundwork for Executable Knowledge.**

- Covers Chapters 00–08: Protégé setup, classes, properties, reasoning, RDF.
- Includes hands-on exercises, Protégé screenshots, and reasoning examples.
- No prior ontology experience required.

| Platform | Link |
|----------|------|
| **LeanPub** | [pizza-owl-ontology-practice-volume1](https://leanpub.com/pizza-owl-ontology-practice-volume1) |
| **Amazon Kindle** | [B0H9D94LBP](https://www.amazon.com/gp/product/B0H9D94LBP) |

### Volume 2: From Class Hierarchy to Semantic Restrictions

**Building Connected, Governed Knowledge Models.**

- Covers Chapters 09–14: Object properties, inverse properties, property characteristics, domain and range, existential and universal restrictions.
- Includes SPARQL queries and Neo4j integration examples.

| Platform | Link |
|----------|------|
| **Leanpub** | [pizza-owl-ontology-practice-volume2](https://leanpub.com/pizza-owl-ontology-practice-volume2) |
| **Amazon Kindle** | [B0H98GY7VZ](https://www.amazon.com/dp/B0H98GY7VZ) |

### Volume 3 (Coming Soon)

The SKDL methodology — Chapters 15–22 (Conceptual Modeling, Semantic Description, Knowledge Reuse, Governance, Validation, Reasoning, Executable Knowledge).

👉 **[Read the Source & Materials](./ebook/markdown)** — All chapters are available for free in this repository under CC BY-SA 4.0.

---

## 🌟 Why Learn Ontology & Protégé?

In the era of AI and Large Language Models (LLMs), **Ontologies** provide the structured "world knowledge" that machines need to reason. By mastering this tutorial, you will learn how to:

- Define complex hierarchies and relationships.
- Use **Reasoners** to automatically classify data.
- Write **SWRL** rules to add intelligent logic.
- Build the backbone of **Knowledge Graphs**.

## 🎓 The Learning Path

This repository is a companion to my **comprehensive video course**. I recommend following the videos while using the snapshot models in this repo to check your work.

### 📺 Watch the Full Course:

- [**Protégé 5.x Pizza Tutorial Video Series (YouTube)** ![YouTube](https://img.shields.io/badge/YouTube-FF0000?logo=youtube&logoColor=white)](https://www.youtube.com/playlist?list=PL6DEHvciXKeUx4P32B3hKMK1t6mC8RhsW)
- [**合集 Ontology Practice - Build pizza.owl in Protégé (BiliBili B站)** ![Bilibili](https://img.shields.io/badge/Bilibili-00A1D6?logo=bilibili&logoColor=white)](https://space.bilibili.com/158390142/lists/2469670)
- [**使用Protege建立Ontology (DouYin 抖音)** ![TikTok](https://img.shields.io/badge/DouYin-000000?logo=tiktok&logoColor=white)](https://www.douyin.com/collection/7298169423012038708/1)

---

## 🛠 Repository Structure

I have tracked my progress step-by-step. You can jump into any stage of the tutorial by using the files in:

- `/snapshot_models`: RDF/OWL files at various stages of the tutorial.
- `/ontology_ref`: Reference materials and SHACL shapes.
- `Protege 5 New OWL Pizza Tutorial V3.2.pdf`: The core manual based on Michael DeBellis' guide.

---

## Acknowledgements & Intellectual Heritage

The evolution of knowledge representation is a collaborative journey. This work is a direct descendant of the **Protégé 4 Tutorial (version 1.3) by Matthew Horridge**, and we honor the foundational contributions of **Holger Knublauch, Alan Rector, Robert Stevens, Chris Wroe, Simon Jupp, Georgina Moulton, Nick Drummond, and Sebastian Brandt**.

We have incorporated revisions by **Michael DeBellis** (bridging Protégé 5.5 transitions and advanced SHACL/SPARQL practices) and acknowledge the critical insights from **Lorenz Buehmann, André Wolski, Dick Ooms, Colin Pilkington, Livia Pinera, Jans Aasman, Yan Xu, and the team at Franz Inc.**. We are honored to feature a foreword and ongoing review by **Timothy W. Cook (Founder of SDC)**.

---

## Licensing & Compliance

To balance educational openness with software governance, this repository utilizes dual licensing:

- **Documentation & eBook Content**: Licensed under **Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)**. This ensures the "share-alike" requirement of the original Pizza Tutorial is strictly honored.
- **Software, Code & Scripts**: Licensed under **GNU General Public License v3.0 (GPL-3.0)**.

For full legal declarations and the detailed attribution chain, please refer to the `LICENSE.md` file in the root of this repository.

---

## 🚀 Getting Started

### 1. Setup

- Download [Protégé](https://protege.stanford.edu/).
- Install a reasoner like **HermiT** or **Pellet** (included in most Protégé versions).

### 2. Modules & Curriculum

| Phase | Topics Covered | Key Videos |
| :--- | :--- | :--- |
| **Foundations** | Classes, Subclasses, and Disjointness | 01 - 09 |
| **Properties** | Object Properties, Domains, and Ranges | 10 - 13 |
| **Logic** | Existential & Universal Restrictions | 14 - 24 |
| **Advanced** | SWRL Rules, SPARQL Queries, and SHACL | 37 - 42 |
| **Cloud** | WebProtégé & WebVOWL | 43 - 45 |

---

## 🧠 Key Concepts Covered

- **Taxonomies vs. Ontologies:** Moving beyond simple hierarchies to complex logic.
- **Open World Assumption:** Understanding how OWL reasoning differs from traditional databases.
- **Description Logic (DL):** Learning to query your knowledge base effectively.
- **SWRL & SQWRL:** Adding "If-Then" rules to your ontology.

---

## 🔗 Resources & Credits

- **Original Guide:** Based on Michael DeBellis' excellent Protégé OWL tutorial.
- **Mind Map:** Use the [pizza.owl tutorial.mm](./pizza.owl%20tutorial.mm) (Open with FreePlane) for a visual overview.
- **Visualization:** View the model via [WebVOWL](https://yasenstar.github.io/protege_pizza/).
- **Official eBook**: Available in the `/ebook` folder.
- **YouTube Playlist**: [Protégé OWL Pizza Tutorial Hands-on Series](https://www.youtube.com/playlist?list=PL6DEHvciXKeUx4P32B3hKMK1t6mC8RhsW).
- **EKA Framework**: Official insights at [xiaoqi.com](https://xiaoqi.com/).

---

## 🤝 Contributing & Support

If you find this tutorial helpful, please:

- ⭐ Star this repository to help others find it.
- 📺 Subscribe to the YouTube Channel for future updates and courses.
- 📘 Buy the Book: Support my work by picking up a copy of the eBook on Leanpub ([Volume-1](https://leanpub.com/pizza-owl-ontology-practice-volume1), [Volume-2](https://leanpub.com/pizza-owl-ontology-practice-volume2)) or Amazon Kindle ([Volume-1](https://www.amazon.com/gp/product/B0H9D94LBP), [Volume-2](https://www.amazon.com/dp/B0H98GY7VZ)). (Volume-3 is on the way...)
- 💬 Feel free to open an Issue if you have questions about the modeling steps.

---

## 👥 Contributors

A heartfelt thank you to all the contributors who have helped improve this project through their issues, discussions, and feedback!

<!--
  IMPORTANT: To keep this list up-to-date, please add your GitHub username below
  if you have opened an Issue or participated in a Discussion.
-->

### Issues & Discussion Participants

| GitHub User | Contribution Type |
|-------------|-------------------|
| [@nikokaoja](https://github.com/nikokaoja) | Kudos! in Issue |
| [@mlungsta89](https://github.com/mlungsta89) | Issue |
| Timothy W. Cook | Foreword for eBook |
| Michael DeBellis | Issues / Foreword for eBook |
| [@LaraAcuna](https://github.com/LaraAcuna) | Question in Discussion |
| *Add your name here* | *Open an Issue or Discussion* |

### How to Contribute

We welcome contributions of all kinds! Here’s how you can help:

1.  **Report Bugs or Ask Questions:** Open a new [Issue](https://github.com/yasenstar/protege_pizza/issues) to report a problem or ask for clarification.
2.  **Start a Discussion:** Join the conversation in [Discussions](https://github.com/yasenstar/protege_pizza/discussions) to share your experiences, suggest improvements, or ask for help.
3.  **Suggest Changes:** If you have a specific improvement in mind, feel free to open a Pull Request.

Happy Pizza Modeling! 🍕

---

*Last updated at 2026-07-26*