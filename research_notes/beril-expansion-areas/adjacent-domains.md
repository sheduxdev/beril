# Beril core engine: non-cybersecurity domains

Scope note: ~12 web searches, no page fetches. Pricing is mostly quote-only; figures below come from aggregators and are rough. Beril internals were not re-read; fit judgments rely on the engine description in the assignment.

## Which domains fit the engine best, and how fast can each ship?

### Takeaway
Strongest fits: (1) due diligence / supplier / KYB, (2) investigative journalism and fact-checking evidence dossiers, (3) competitive and market intelligence, (4) brand protection / fraud monitoring, (5) open-source project health due diligence, (6) deep-research verification layer. Fastest to ship (inference): open-source project health (data pack plus profile, reuses repo hunt code) and journalism/OSINT evidence dossier (template plus archive step).

### Cited Findings
- Deep-research agents still have citation problems, which is Beril's "every claim linked, confirmed vs inferred" differentiator. An April 2026 preprint found 3-13% of citation URLs hallucinated in OpenAI/Google deep research modes — [arXiv 2604.03173](https://arxiv.org/abs/2604.03173)
- Microsoft's DeepTRACE audit reports citation accuracy of 40-80% across Perplexity, Copilot, Gemini, GPT-based systems, with many statements unsupported by their own sources — [Microsoft Research](https://www.microsoft.com/en-us/research/publication/deeptrace-auditing-deep-research-ai-systems-for-tracking-reliability-across-citations-and-evidence)
- A May 2026 paper "Cited but Not Verified" argues agent citations cannot be reliably verified — [arXiv 2605.06635](https://arxiv.org/html/2605.06635)
- Bellingcat's toolkit lists archiving tools; Hunchly is paid, Wayback Machine free; Bellingcat also built the open-source Auto Archiver — [Bellingcat toolkit](https://bellingcat.gitbook.io/toolkit/categories/archiving.md), [GIJN](https://gijn.org/stories/bellingcat-new-online-investigations-toolkit)
- OpenSSF Scorecard grades repos with 18 risk-weighted checks; used to judge dependency health; public weekly scores omit some checks (CI-Tests, Contributors, Dependency-Update-Tool) — [ossf/scorecard](https://github.com/ossf/scorecard), [Wiz](https://www.wiz.io/academy/openssf-scorecard-overview)

### Inferences (feasibility)
| Domain | Feasibility | Reason |
|---|---|---|
| OSS project health / due diligence | HIGH | Beril already hunts repos and scores deps; add a profile and Scorecard/OSV/maintainer-activity pack. Crowded free tools exist (Scorecard), so the edge is the evidence-linked dossier. |
| Journalism / OSINT evidence dossier | HIGH | Claim-to-source linking and confirmed/inferred labels map directly to verification practice; needs archive/hash step (Auto Archiver overlaps). Low revenue, high credibility. |
| Due diligence / KYB / supplier risk | MED | Best demand and budgets, but value rests on licensed data (sanctions, registries) that open scraping cannot match; GDPR exposure is highest. |
| Competitive / market intel | MED | Stealth harvest plus change tracking fits; incumbents are polished sales-enablement SaaS, and ToS/anti-bot risk is real. |
| Brand protection / counterfeit | MED | Marketplace scraping fits; real product value is takedown workflow and platform relationships, which Beril lacks. |
| Deep-research verification layer | MED | Strong differentiator given 2026 citation findings, but a fast-moving crowded space and needs LLM integration decisions. |
| Compliance/regulatory monitoring | MED | Public-source pages are low legal risk; incumbent vendors sell curated interpretation (not researched here). |
| Price monitoring | LOW | Commodity market, anti-bot arms race, little use for evidence labels. |
| Legal / e-discovery | LOW | Requires chain-of-custody and privilege tooling; web harvest is minor part (inference, not researched). |
| Academic lit review | LOW-MED | Open APIs make stealth scraping unnecessary; dossier format fits (not researched). |
| Recruiting / expert finding | LOW | Highest personal-data and platform-ToS risk, little differentiation. |
| Education / training | MED | Beril's train/labs mode already exists; reusable as generic skills-lab engine; no revenue research done. |

### Gaps
- No searches for recruiting, e-discovery, regulatory-monitoring vendors, or academic tools; ratings for them are inference only.
- No market-size or demand figures found; none stated.

## Competitors, pricing, who pays (top domains)

### Takeaway
Incumbents are quote-based enterprise SaaS. Open pricing figures are third-party estimates. Gap: local-first, open, evidence-linked, auditable output.

### Cited Findings
- Crayon and Klue pricing is not published; third-party blogs estimate roughly $15k-40k+/year; Kompyte described as cheapest (one source: from $300/year). Both Crayon and Klue named Leaders in the 2026 Gartner Magic Quadrant for Competitive and Market Intelligence Platforms per aggregator reporting; one source says SoftwareOne acquired Crayon for $1.4B in July 2025 (unverified) — [Prospeo](https://prospeo.io/s/crayon-pricing-reviews-pros-and-cons), [ZoomInfo Pipeline](https://pipeline.zoominfo.com/sales/crayon-vs-klue), [G2 Kompyte](https://www.g2.com/products/kompyte/pricing). Estimates come from vendors selling competing products.
- Dow Jones Risk & Compliance has no published pricing; marketed for KYC and due diligence on customers and connected parties — [G2](https://www.g2.com/products/dow-jones-risk-compliance/pricing), [TrustRadius](https://www.trustradius.com/products/dow-jones-risk-compliance)
- Sayari: no public price list; offers supplier due diligence and TPRM batch screening — [Sayari TPRM](https://sayari.com/tprm), [G2](https://www.g2.com/products/sayari/pricing)
- Maltego: free Community tier; Professional listed at $6,600/yr (Capterra, TechJockey) vs about EUR/USD 5,000 per user per year (TrustRadius); Organization custom; public-sector pricing separate — [Maltego plans](https://www.maltego.com/pricing-plans/), [Capterra](https://www.capterra.com/p/266210/Maltego/)
- Diffbot paid entry about $299/month (comparison page), credit-based, Knowledge Graph has no published per-query price; Apify Starter about $19-29/month — [Capterra Diffbot](https://www.capterra.com/p/140641/Diffbot/), [G2 compare](https://www.g2.com/compare/apify-vs-diffbot)
- Red Points: flat-fee, scope-based, request pricing; Corsearch Brand Protection: pricing on request — [Red Points pricing](https://www.redpoints.com/pricing/?nab=1), [G2 Corsearch](https://www.g2.com/products/corsearch-brand-protection/pricing)
- Hunchly is the paid evidence-capture tool used by Bellingcat investigators — [Bellingcat toolkit](https://bellingcat.gitbook.io/toolkit/categories/archiving.md)

### Inferences
- Payers: compliance/procurement (KYB, TPRM), product marketing/sales enablement (CI), brand/legal teams (brand protection), newsrooms/NGOs (low budget, high reputational value), OSS adopters/security teams (OSS health).
- Beril's differentiator vs all: local-first, auditable claim-to-source dossiers with confirmed/inferred labels, scope gate, open source. Weak points: no licensed datasets, no managed takedown, no sales-enablement workflow.
- A pricing wedge of free/open core plus paid managed packs is plausible; unvalidated.

### Gaps
- Real list prices for Sayari, Dow Jones, Crayon, Klue, Red Points, Corsearch not found. Prisync/Competera, Kompyte details, Perplexity pricing not found. Snyk Advisor, Socket, CHAOSS not covered.

## Legal and ethical constraints on scraping

### Takeaway
US: public, logged-out scraping has favorable precedent (CFAA narrowed; ToS contract claim failed for logged-off scraping in one district ruling), but this is not blanket permission. EU: GDPR applies whenever personal data is collected; robots.txt and access controls feed the balancing test. Turkey KVKK: no scraping-specific decision found.

### Cited Findings
- hiQ v. LinkedIn: 9th Cir. 2019 held scraping public data likely not a CFAA violation; vacated by SCOTUS after Van Buren (2021); reaffirmed on remand April 2022 — [Jenner](https://www.jenner.com/en/news-insights/publications/client-alert-data-scraping-in-hiq-v-linkedin-the-ninth-circuit-reaffirms-narrow-interpretation-of-cfaa), [TechCrunch](https://techcrunch.com/?p=2165820), [Haynes Boone](https://www.haynesboone.com/news/publications/ninth-circuit-rejects-linkedin-attempt-to-prevent-web-scraping-of-publicly-member-profiles.pdf). Freshfields notes some generally applicable access restriction may matter — [Freshfields](https://www.freshfields.com/en/our-thinking/blogs/a-fresh-take/data-scraping-does-it-again-102hp4o)
- Meta v. Bright Data (N.D. Cal., Jan 23 2024): court held Meta's terms did not bar logged-off scraping of public data; Meta later dropped the case (per MediaPost headline, docket not verified); commentators dispute how far it reaches — [TechCrunch](https://techcrunch.com/2024/01/24/court-rules-in-favor-of-a-web-scraper-bright-data-which-meta-had-used-and-then-sued), [FBM](https://www.fbm.com/technology/publications/major-decision-affects-law-of-scraping-and-online-data-collection-meta-platforms-v-bright-data/), [MediaPost](https://www.mediapost.com/publications/article/393996/None)
- EDPB Guidelines 03/2026 on web scraping for generative AI: GDPR applies to scraping when personal data is processed; legitimate interest is the likely basis and needs a documented three-part test; robots.txt, ai.txt, CAPTCHAs, login walls are relevant to reasonable expectations; special-category data needs Art. 9(2) exception — [Sidley](https://datamatters.sidley.com/2026/07/23/what-do-the-european-data-protection-boards-web-scraping-guidelines-mean-for-ai-training-datasets/), [Reed Smith](https://www.reedsmith.com/our-insights/blogs/technology-law-dispatch/102nbqu/edpb-web-scraping-guidelines-for-ai-making-the-impossible-possible/). Status conflict: EDPB pages show both a July 2026 date and comments due 30 Oct 2026, so confirm if final — [EDPB](https://www.edpb.europa.eu/news/edpb-sheds-light-on-anonymisation-and-web-scraping-for-generative-ai-and-adopts-final-version_en). Scope is generative-AI training, so application to dossiers is by analogy.
- KVKK: law defines processing to include automated collection; no Kurul decision on scraping found; Principle Decision 2026/1095 (OG 1 July 2026) concerns accident victims' data, relevance to scraping unconfirmed — [KVKK decisions](https://www.kvkk.gov.tr/Icerik/5406/kurul-karar-ozetleri)

### Inferences (per domain)
- Due diligence/KYB, recruiting, journalism: heaviest personal-data exposure; need a documented legitimate-interest note per dossier and data-minimization; journalism may rely on public-interest/press exemptions (varies by country, not researched).
- Competitive intel, price monitoring, brand protection: mostly company/product data, so lower GDPR risk, higher ToS and anti-bot risk. Stealth/anti-bot circumvention is untested territory: hiQ/Bright Data concern public logged-off access, not defeating bot detection. Treat Camoufox use against explicit blocks as a risk in commercial settings. Beril's existing scope/ownership gate should become a "source policy gate" (robots, ToS, login state, personal-data flag).
- OSS health: public APIs and repos, lowest risk.
- Not legal advice; no jurisdiction-specific research done beyond above (no CFAA or ToS case after 2024 found in results; absence is a search gap, not proof).

### Gaps
- No post-2024 US scraping rulings found. No source on robots.txt legal weight beyond EDPB. No KVKK scraping authority. No domain-specific rules (FCRA for background checks, press law) researched.

## Fastest path with least code change

### Takeaway
Ship as profiles plus data packs plus report templates, not new engines. Order (inference): OSS due-diligence profile, then journalism evidence dossier, then supplier/KYB-lite, then competitive-watch.

### Cited Findings
- Beril's tiered report profiles, `data/*.json` packs and dossier builder exist per the project README/CLAUDE.md (CLAUDE.md lists `./beril report --profile`, `data/` packs, `scripts/build_dossier.py`) — local files, read from the project instructions in this task.

### Inferences
1. OSS health (days): profile "oss-dd"; pack = Scorecard, OSV (already `osv_seed.json`), release cadence, maintainer count; template = adoption memo. Reuses `deps`, `hunt`.
2. Journalism dossier (about 1-2 weeks): profile "newsroom"; add snapshot/hash step (compare Bellingcat Auto Archiver rather than rebuild); template = claim table with source, archive URL, label.
3. Supplier/KYB-lite: pack of open registries and sanctions lists; strong GDPR note; position as screening aid, not licensed-data replacement.
4. Competitive watch: reuse harvest plus diff; needs change detection and scheduling, more new code.
5. Training mode generalizes (OSINT/verification labs) for a free community hook.
- Differentiated positioning: "verifiable by construction" research output, backed by the 2026 deep-research citation findings.

### Gaps
- Effort estimates are unvalidated guesses; code was not read this session.
