# Beril: siber içi genişleme alanları ve rakip manzarası (Kasım 2026)

Not: Kaynaklar çoğunlukla WebSearch özetleri; vendor sayfaları doğrudan fetch edilmedi. Fiyatlar için güven DÜŞÜK, doğrulanmalı. Beril README/SKILL.md okunmadı (görev bağlamındaki yetenek listesi kullanıldı).

## 1. Alan bazında rakipler (ne yapar, fiyat, açık kaynak mı)

### Takeaway
AppSec/SCA/secret tarafı kalabalık ve olgun. Ücretsiz OSS çekirdekler (gitleaks, TruffleHog, Trivy, Grype, Nuclei) var; ticari taraf kullanıcı başı veya teklif bazlı. Agent/MCP ve AI-pentest alanı 2026'da hızla para çekiyor.

### Cited Findings
- Snyk: ücretsiz katman (200 OSS test/ay), Team ~$25/geliştirici/ay (3. taraf blog, güven düşük) — [dev.to](https://dev.to/rahulxsingh/is-snyk-worth-the-cost-complete-pricing-breakdown-for-2026-39m1)
- Semgrep: ücretsiz katman; ücretli oran kaynaklar arasında çelişkili ($30 vs $35/katkıcı/ay) — [stackpick](https://stackpick.net/blog/best-snyk-alternatives-2026/), [safeguard.sh](https://safeguard.sh/resources/blog/appsec-and-sca-pricing-compared-what-drives-cost-and-where-the-free-options-stop)
- Aikido: ücretsiz Developer plan, sabit fiyatlı katmanlar; Root'u $70M'e satın aldı (tarih doğrulanmadı) — [aikido.dev](https://aikido.dev/blog/snyk-vs-semgrep), [bankinfosecurity](https://www.bankinfosecurity.com/latest-news/application-security-c-482/p-1)
- Endor Labs: teklif bazlı (katkıcı/yıl), Autonomous Plane'i 13 Şub 2026'da aldı; toplam fonlama kaynaklar arasında $188M vs $208M çelişkili — [sacra](https://sacra.com/research/endor-labs-vs-snyk/), [cbinsights](https://www.cbinsights.com/investor/endor-labs)
- Socket: $60M Series C, $1B değerleme (20 May 2026); Secure Annex alımıyla (28 Nis 2026) tarayıcı eklentisi, editör eklentisi, MCP sunucusu ve AI araçlarına genişledi — [socket.dev](https://socket.dev/blog/socket-raises-60m-series-c-press-release), [socket.dev](https://socket.dev/blog/socket-acquires-secure-annex)
- Secret tarama: gitleaks MIT, ücretsiz, bakım modunda (tek kaynak), GitHub Action org repolarında lisans anahtarı ister; TruffleHog çoğu kaynakta AGPL-3.0 (bir kaynak Apache der, çelişki), Enterprise fiyatı gizli; GitGuardian freemium, katkıcı başı; GitHub Secret Protection $19/aktif katkıcı/ay — [tech-insider](https://tech-insider.org/trufflehog-vs-gitleaks-vs-gitguardian-2026/), [gitguardian.com](https://www.gitguardian.com/pricing), [dev.co](https://dev.co/security/open-source/trufflehog)
- Agent/MCP tarayıcı: Snyk agent-scan (eski Invariant MCP scanner, `uvx snyk-agent-scan`; MCP sunucularını config'ten ÇALIŞTIRARAK tarar, tool açıklamalarını Snyk API'ye gönderir (eski sürüm 0.4.3 için bildirildi); Thoughtworks Radar Nis 2026) — [github.com/snyk/agent-scan](https://github.com/snyk/agent-scan), [dev.to](https://dev.to/bawbel/snyk-scans-your-mcp-servers-by-running-them-here-is-what-that-means-a4b), [thoughtworks](https://www.thoughtworks.com/en-cl/radar/tools/agent-scan)
- Cisco mcp-scanner: açık kaynak (lisans doğrulanamadı), YARA + LLM-judge + Cisco AI Defense API + davranışsal kod analizi; RSAC 2026'da DefenseClaw (MCP Scanner + Skills Scanner + AI BoM + CodeGuard) — [github.com/cisco-ai-defense/mcp-scanner](https://github.com/cisco-ai-defense/mcp-scanner), [cisco blog](https://blogs.cisco.com/ai/ciscos-mcp-scanner-introduces-behavioral-code-threat-analysis), [newsroom](https://newsroom.cisco.com/c/r/newsroom/en/us/a/y2026/m03/cisco-reimagines-security-for-the-agentic-workforce.html)
- Bug bounty/AI pentest: XBOW $120M Series C (18 Mar 2026), >$1B değerleme, Microsoft Security Copilot/Sentinel entegrasyonu; 2025'te HackerOne ABD liderliği (~1060 rapor, insan incelemeli) — [businesswire](https://www.businesswire.com/news/home/20260318258057/en/XBOW-Raises-$120M-to-Scale-its-Autonomous-Hacker), [helpnetsecurity](https://www.helpnetsecurity.com/2025/06/25/xbow-ai-funding/)
- Açık kaynak AI pentest: Shannon (Keygraph, Lite AGPL-3.0, kaynak kod analizi + canlı exploit), Strix (Apache-2.0, Docker sandbox), PentestGPT; tek bir 3. taraf kıyasta Escape %75, Claude %70, Shannon %30, Strix %5 (tek veri noktası) — [helpnetsecurity](https://www.helpnetsecurity.com/2026/02/02/open-source-ai-pentesting-tools-test/), [stingrai](https://www.stingrai.io/blog/open-source-ai-pentest-agents-compared-2026)
- ProjectDiscovery: Nuclei OSS ücretsiz; Cloud Pro ~$2,500/yıl veya $200/koltuk/ay (kaynaklar çelişkili); Neo (AI saldırgan platform) Ağu 2026 GA, kullandıkça öde, BYOK — [docs.projectdiscovery.io](https://docs.projectdiscovery.io/cloud/pricing), [prnewswire](https://www.prnewswire.com/news-releases/projectdiscovery-makes-neo-generally-available-with-pay-as-you-go-pricing-302842104.html)
- Konteyner/IaC OSS: Trivy (imaj/FS/repo/K8s/IaC, SARIF + VEX), Syft+Grype (SBOM + açık eşleştirme, SARIF, OpenVEX), Checkov (IaC, kalitesi tartışmalı), Kubescape (runtime yüklü zafiyet önceliği) — [aikido trivy-alternatives](https://www.aikido.dev/blog/trivy-alternatives), [armosec](https://www.armosec.io/blog/best-kubernetes-dependency-scanners/)

### Inferences
- OSS rakiplerin çoğu tek iş yapar (secret, SCA, MCP). Beril'in "tek kanıt zincirli rapor" birleşimi farklılaştırıcı, ama her alanda tek tek derinlikte kaybeder.
- Agent-scan'in "config'i çalıştırarak tarar" yaklaşımı, Beril'in statik-önce/ağsız prensibi için net bir pozisyon farkı.

### Gaps
- Burp AI (PortSwigger), Semgrep/Socket/Endor net fiyatları, Aikido satın alma tarihi, Cisco lisansı doğrulanamadı. Snyk agent-scan güncel sürümde veri gönderme davranışı doğrulanmadı.

## 2. Boşluklar (yerel, kanıt bağlantılı, OSS, kapsam kapılı)

### Takeaway
En güçlü boşluklar: (a) agent/MCP tedarik zinciri için statik, ağsız, yerel tarama; (b) maintainer dostu doğrulanmış rapor; (c) Minecraft/oyun modu zararlı yazılımı. SMB/KVKK odağı da büyük oyuncuların fiyat/dil dışında bıraktığı alan (çıkarım).

### Cited Findings
- curl, 21 Oca 2026'da bug bounty'yi kapattı (31 Oca'da bitti); tepe dönemde raporların ~%20'si "AI slop"; raporlar GitHub özel zafiyet bildirimine taşındı (kaynaklar ödüllü HackerOne kanalı konusunda çelişkili); Stenberg AI destekli iyi raporları kabul ediyor — [daniel.haxx.se](https://daniel.haxx.se/blog/2026/01/26/the-end-of-the-curl-bug-bounty/), [theregister](https://www.theregister.com/2026/01/21/curl_ends_bug_bounty/)
- Fractureiser (2023): CurseForge/Bukkit modlarında 4 aşamalı Windows/Linux infostealer; ele geçirilmiş geliştirici hesapları; sonrası için 2026 yeni kampanya bulunamadı; CurseForge'un kendi jar tarayıcısı var, topluluk betikleri var — [bitdefender](https://www.bitdefender.com/blog/labs/infected-minecraft-mods-lead-to-multi-stage-multi-platform-infostealer-malware), [kaspersky](https://www.kaspersky.com/blog/curseforge-compromised-fractureiser/48388/), [github](https://github.com/fractureiser-investigation/fractureiser/blob/main/README.md)
- Veracode 2026: AI kod görevlerinin ~%44'ü riskli zafiyet getiriyor, ortalama geçiş %56 (2025: %55), XSS geçiş %15; Escape.tech 1.400 vibe-coded uygulamada 2.038 kritik zafiyet — [veracode](https://www.veracode.com/blog/2026-genai-code-security-report-ai-risk), [CSA note (AI destekli, resmi onaysız)](https://labs.cloudsecurityalliance.org/research/csa-research-note-ai-generated-code-vulnerability-surge-2026/)

### Inferences
- Maintainer'lar düşük kaliteli AI raporlardan bıkmış; yeniden üretilmiş + sandbox kanıtı + ownership gate, Beril'in doğrudan değer önerisi (güven orta).
- Minecraft/JAR tarama: ticari rakip bulunamadı, ama arama sınırlı yapıldı; niş ve düşük rekabet (güven düşük-orta).
- Vibe-coded app review için bulunan rakipler kurumsal (Veracode/Escape); yerel OSS karşılığı arama sonuçlarında çıkmadı (güven düşük).

### Gaps
- SMB/KVKK odaklı OSS araç araması yapılmadı. Minecraft taraması için GitHub OSS rakip envanteri (yıldız/son commit) çıkarılmadı.

## 3. Genişleme fikirleri değerlendirmesi

### Takeaway
En düşük maliyet/en yüksek talep: SARIF + SBOM/VEX çıktısı, GitHub Action, CRA-hazır raporlama. Orta: browser/IDE eklenti taraması, mobil. Yüksek maliyet/doymuş: IaC/K8s, LLM red-team.

### Cited Findings
- Trivy ve Grype SARIF/VEX (OpenVEX, CycloneDX VEX, CSAF) çıkışı destekliyor; VEX üretiminde araçlar arası tutarlılık açık sorun — [arxiv](https://arxiv.org/html/2503.14388v3), [aikido](https://www.aikido.dev/blog/trivy-alternatives)
- Trivy GitHub Action 23 Mar 2026'da TeamPCP tarafından ele geçirildi (SHA pinleme önerisi); CI eklentisi dağıtımı güven sorunu taşır — [tech-insider](https://tech-insider.org/trivy-tutorial-2026/) (ikincil kaynak, güven orta-düşük)
- Socket eklenti/MCP/AI araç kapsamını Nis 2026'da genişletti → browser/IDE eklenti taraması talep kanıtı — [socket.dev](https://socket.dev/blog/socket-acquires-secure-annex)
- IaC/K8s alanı: Trivy, Checkov, Kubescape zaten ücretsiz ve yerleşik — [armosec](https://www.armosec.io/blog/best-kubernetes-dependency-scanners/)
- ProjectDiscovery Neo ve XBOW, sürekli saldırı yüzeyi/otonom pentest alanında kurumsal fiyatlandırma ile konumlanmış — [prnewswire](https://www.prnewswire.com/news-releases/projectdiscovery-makes-neo-generally-available-with-pay-as-you-go-pricing-302842104.html)

### Inferences (öncelik önerisi)
1. SARIF + CycloneDX/OpenVEX çıktısı, tüm `beril scan/deps/secrets/mcp/jar` komutları için (küçük iş, CI/GitHub Code Scanning ve CRA ile uyumlu).
2. Kendi GitHub Action'ı: SHA-pinli, ağsız mod varsayılan (Trivy Action olayı farklılaştırıcı).
3. MCP/agent/skill statik tarama derinleştirme + eklenti (VS Code/browser) taraması.
4. Rapor profilleri: maintainer, SMB, CRA/KVKK eşlemesi (ISO 27001/SOC2 eşlemesi için kaynak bulunamadı).
5. Kaçın: tam IaC/K8s motoru, LLM red-team (kalabalık, cevap yok).
Güven orta, kanıta dayalı sıralama yok; pazar büyüklüğü verilmedi.

### Gaps
- ISO 27001/SOC2/KVKK eşleme araçları, APK/IPA OSS rakipleri (MobSF vb.), LLM red-team (garak/promptfoo), tehdit aktörü/fidye dossier rakipleri (MISP/OpenCTI) araştırılmadı.

## 4. 2025-2026 talep eğilimleri

### Takeaway
Dört güçlü itici: tedarik zinciri solucanları (npm, MCP/AI araç hedefli), AI kod zafiyeti, CRA raporlama, AI slop'un bug bounty'yi bozması.

### Cited Findings
- Shai-Hulud: Eyl 2025 başlangıç; Kas 2025 "2.0" 796 paket/1.092 sürüm; Nis 2026 @bitwarden/cli 2026.4.0 `~/.claude.json` ve `~/.claude/mcp.json` hedefledi; 11 May 2026 Mini Shai-Hulud (TanStack ağacı, Mistral AI, UiPath, OpenSearch), kaynak kodu 12 May'da yayımlandı; 1 Haz 2026 @redhat-cloud-services altında ≥32 paket; SANDWORM_MODE MCP girdilerini saldırgan altyapısına yönlendiriyor; solucan paketleri geçerli SLSA L3 provenance taşıdı — [CSA](https://labs.cloudsecurityalliance.org/research/csa-research-note-shai-hulud-npm-worm-ai-developer-supply-ch/), [Akamai](https://www.akamai.com/blog/security-research/2026/may/mini-shai-hulud-worm-returns-goes-public), [Unit 42](https://unit42.paloaltonetworks.com/monitoring-npm-supply-chain-attacks/)
- Socket'e göre npm 12 Temmuz 2026'da install-hook sorununu kapattı, publish tarafı hâlâ opt-in — [socket.dev glossary](https://socket.dev/glossary/shai-hulud.md)
- EU CRA: Madde 14 raporlama 11 Eyl 2026'da başladı (aktif sömürülen zafiyet, ciddi olaylar; piyasadaki mevcut ürünleri de kapsar); tek raporlama platformu URL'si 8 Eyl itibarıyla yayımlanmamıştı; makine-okunur SBOM 11 Ara 2027; ticari olmayan OSS genelde kapsam dışı, steward rejimi raporlama 11 Ara 2027 — [Travers Smith](https://www.traverssmith.com/knowledge/knowledge-container/the-eu-cyber-resilience-acts-vulnerability-and-incident-reporting-requirements-are-now-live/), [Goodwin](https://www.goodwinlaw.com/en/insights/publications/2026/09/alerts-lifesciences-technology-preparing-for-eu-cyber-resilience-act), [CSA](https://labs.cloudsecurityalliance.org/research/csa-research-note-eu-cra-vulnerability-reporting-20260910-cs/), [EC](https://digital-strategy.ec.europa.eu/en/policies/cra-reporting)
- Trivy Action ve release altyapısı Mar 2026'da ele geçirildi (bkz. §3).

### Inferences
- Güvenlik aracının kendisi saldırı hedefi: "araç tedarik zinciri" güveni (SHA pin, ağsız çalıştırma, imzalı release) pazarlama noktası.
- Provenance tek başına yetmiyor (SLSA L3 solucan paketi) → davranış/içerik analizi gerekli.

### Gaps
- ENISA/CISA birincil sayfaları fetch edilmedi. Gartner/Forrester özetleri bulunamadı. Pazar büyüklüğü verisi bilinçli olarak atlandı.
