# Beril'i önce doğrula, sonra büyüt

Beril bugün bir **orkestrasyon ve kanıt zinciri aracıdır, tespit motoru değildir**. Yerel, açık kaynak, kapsam kapılı ve "doğrulandı / çıkarım" etiketli tek bir rapor üretir. Bu birleşimi rakiplerin hiçbiri sunmuyor. Ama her alanda tek tek bakınca rakipler derinlikte çok önde: ~13 bin satır Python, 16 secret sağlayıcısı, 27 kaynak kodu kuralı ve 12 KEV kaydı var (yerel inceleme). TruffleHog 700+ doğrulamalı dedektör taşıyor ([GitHub](https://github.com/trufflesecurity/trufflehog)). **İlk yapılacak iş yeni alan açmak değil, doğruluğu kanıtlamak ve dağıtımı kolaylaştırmaktır:** canlı OSV/KEV/EPSS verisi, SARIF + CycloneDX/VEX çıktısı, SHA-pinli GitHub Action ve ilk benchmark. İkinci adım, Beril'in en savunulabilir üç konumunu derinleştirmek: agent/MCP/skill tedarik zinciri taraması, maintainer dostu doğrulanmış rapor, Minecraft/JAR kötü amaçlı yazılım taraması. Siber dışında en hızlı kazanç, mevcut kodu yeniden kullanan "açık kaynak proje sağlığı" ve "gazetecilik kanıt dosyası" profilleri. Aşağıdaki bulguların çoğu arama özetlerine dayanıyor, fiyat ve pazar büyüklüğü verileri düşük güvenli ve hukuki değerlendirmeler hukuk görüşü değildir.

## Zemin hazır: talep güçlü, ama Beril'in tespit derinliği demo seviyesinde

2025-2026 talebi Beril'in konumuyla örtüşüyor. Tedarik zinciri solucanları AI geliştirici araçlarını hedefliyor: Nisan 2026'da @bitwarden/cli sürümü `~/.claude.json` ve `~/.claude/mcp.json` dosyalarını hedef aldı, Mayıs 2026'da Mini Shai-Hulud yayıldı ve solucan paketleri geçerli SLSA L3 provenance taşıdı ([CSA](https://labs.cloudsecurityalliance.org/research/csa-research-note-shai-hulud-npm-worm-ai-developer-supply-ch/), [Akamai](https://www.akamai.com/blog/security-research/2026/may/mini-shai-hulud-worm-returns-goes-public)). Provenance tek başına yetmiyor, içerik ve davranış analizi gerekiyor. Bu, Beril'in MCP/JAR/deps statik taramasına doğrudan alan açıyor. AI kodu da açık: Veracode'a göre AI kod görevlerinin ~%44'ü riskli zafiyet getiriyor ([Veracode](https://www.veracode.com/blog/2026-genai-code-security-report-ai-risk)). Maintainer tarafında curl, bug bounty'yi 31 Ocak 2026'da kapattı ve "AI slop" raporlarından yakındı ([Stenberg](https://daniel.haxx.se/blog/2026/01/26/the-end-of-the-curl-bug-bounty/)). Yeniden üretilmiş, sandbox kanıtlı rapor üretmek Beril'in `hunt` hattının doğal değer önerisi (güven orta). AB CRA'nın Madde 14 raporlaması 11 Eylül 2026'da başladı, makine-okunur SBOM beklentisi 11 Aralık 2027'de ([Travers Smith](https://www.traverssmith.com/knowledge/knowledge-container/the-eu-cyber-resilience-acts-vulnerability-and-incident-reporting-requirements-are-now-live/), [Goodwin](https://www.goodwinlaw.com/en/insights/publications/2026/09/alerts-lifesciences-technology-preparing-for-eu-cyber-resilience-act)).

Rakip tarafı kalabalık ve parası var: Socket 20 Mayıs 2026'da $60M Series C ve $1B değerleme aldı, Nisan'da eklenti/MCP/AI araç kapsamını genişletti ([Socket](https://socket.dev/blog/socket-raises-60m-series-c-press-release), [Secure Annex](https://socket.dev/blog/socket-acquires-secure-annex)). XBOW $120M Series C topladı ([BusinessWire](https://www.businesswire.com/news/home/20260318258057/en/XBOW-Raises-$120M-to-Scale-its-Autonomous-Hacker)). Truffle Security $25M Series B aldı ([Intel Capital](https://www.intelcapital.com/truffle-security-raises-25-million-series-b-to-expand-nhi-security/)). Bu şirketlerle derinlikte yarışılmaz. Konum, "yerel, ağsız, kanıt bağlantılı, tek komut" olmalı.

## Rakip boşlukları: her kategoride geride, farklılaşma birleşimde

Yerel envanter ve rakip verileri şu tabloyu veriyor. "Zayıf" Beril'in kategori rakibinin belirgin gerisinde olduğu, "eşit" delegasyonla denk olduğu, "yok" özelliğin bulunmadığı anlamına gelir. Rakip özelliklerinin bir kısmı bu oturumda kaynakla doğrulanmadı (genel bilgi, çıkarım).

| Alan | Rakip | Beril durumu | Not |
|---|---|---|---|
| Secret tarama | TruffleHog (700+ doğrulamalı dedektör, AGPL), Gitleaks (31k yıldız, MIT) | **Zayıf** | 16 sağlayıcı; baseline/allowlist ve entegrasyonlar eksik. Gitleaks "bakım modunda" olduğunu söylüyor, bu bir fırsat ([GitHub](https://github.com/gitleaks/gitleaks)) |
| SAST | Semgrep (~24 dil dizini), CodeQL | **Zayıf** | 27 regex kuralı, AST/taint yok; Semgrep çıktısını içeri almak daha ucuz |
| Web zafiyet şablonları | Nuclei (6.468+ `vuln` şablonu, sayı kaynaklara göre değişiyor) | **Zayıf** | web_checks ~1.100 satır ([README](https://raw.githubusercontent.com/projectdiscovery/nuclei-templates/main/README.md)) |
| SCA / SBOM / konteyner | Trivy, Grype, Syft, OSV-Scanner | **Zayıf** | 6 paketlik offline tohum; SBOM minimal CycloneDX; SPDX/VEX üreticisi yok (çıkarım) |
| Aktif web tarama | Burp, ZAP, XBOW | **Zayıf** | active.py 354 satır; kimlikli tarama yok |
| Tersine mühendislik | Ghidra, capa, rizin | **Eşit (delegasyonla)** | Beril sarmalıyor, kurulumu kullanıcı yapıyor |
| MCP/agent tarama | Snyk agent-scan, Cisco mcp-scanner | **Belirsiz, olası farklılaşma** | Snyk aracı MCP sunucularını config'ten çalıştırarak tarıyor ([dev.to](https://dev.to/bawbel/snyk-scans-your-mcp-servers-by-running-them-here-is-what-that-means-a4b)); Beril'in statik/ağsız yaklaşımı net bir fark. Beril'in 12 deseninin etkinliği ölçülmedi |
| Minecraft/JAR | CurseForge'un kendi tarayıcısı, topluluk betikleri | **Olası boşluk** | Ticari rakip bulunamadı ama arama sınırlıydı, güven düşük-orta |
| Maintainer raporu / sandbox | Doğrudan eşdeğer bulunamadı | **Farklılaşma adayı** | Güven orta |
| Kanıt bağlantılı dosya (Camoufox) | Maltego, SpiderFoot, Recorded Future | **Farklı mod** | Grafik, internet ölçeği veri ve ticari feed yok |
| Ekip özellikleri | Snyk, Semgrep, Aikido | **Yok** | Dashboard tek kullanıcı, girişsiz; SSO/RBAC/PR yorumu/ticket yok |

Yapısal zayıflıklar da bunlarla birlikte okunmalı: tek bakımcı ve 40 commit, yayımlanmış benchmark yok, tohum veriler bayatlıyor (README kabul ediyor), Linux dışı platformlar test edilmedi, Camoufox CAPTCHA ve giriş duvarlarına yeniliyor, triyaj kısmen ajan yargısına bağlı. Toplama bir gözlem: bu tabloda Beril'in "yenemediği" her satır, **dışarıdan içeri alma** (Trivy/Grype/Semgrep/Nuclei/ZAP çıktısı → tek normalize bulgu şeması) ile kapatılabilir. Beril'in işi dedektör olmak değil, dedektörlerin sonucunu kanıtla bağlayıp doğrulanmış hale getirmek olmalı.

## Siber içi genişleme: önce çıktı formatları, sonra agent tedarik zinciri

SARIF ve VEX çıktısı en ucuz, talebi en net kazanım. Trivy ve Grype SARIF ile OpenVEX/CycloneDX VEX üretiyor ([Aikido](https://www.aikido.dev/blog/trivy-alternatives)); Beril'de SARIF render'ı ve minimal CycloneDX var, VEX ve SPDX eksik. Kendi GitHub Action'ınızı SHA-pinli ve ağsız varsayılanla yayımlamak ayrı bir pazarlama noktası, çünkü Trivy Action'ı 23 Mart 2026'da ele geçirildi (ikincil kaynak, güven orta-düşük: [tech-insider](https://tech-insider.org/trivy-tutorial-2026/)). "Güvenlik aracının kendisi saldırı hedefi" mesajı bu yüzden güçlü.

Sonraki katman agent/MCP/skill/eklenti taraması (VS Code ve tarayıcı eklentisi dahil): Socket'in aynı yöne genişlemesi talebin kanıtı. CRA odaklı rapor profili (SBOM, erişilebilirlik analizi, zafiyet triyaj kanıtı) AB'deki küçük üreticiler için bir kanca. ISO 27001/SOC2/NIS2 eşlemesi için kaynak bulunamadı, bu yüzden CRA dışı eşlemeler "denenecek varsayım" olarak kalıyor. **Kaçınılacaklar:** tam IaC/K8s motoru (Trivy, Checkov, Kubescape ücretsiz ve yerleşik: [ARMO](https://www.armosec.io/blog/best-kubernetes-dependency-scanners/)), LLM red-team (kalabalık, bu turda araştırılmadı) ve XBOW/ProjectDiscovery ile yarışan otonom pentest. Açık kaynak AI-pentest araçlarının tek bir üçüncü taraf karşılaştırmasında farklı sonuçlar verdiği not edilmeli (Escape %75, Claude %70, Shannon %30, Strix %5), bu tek veri noktası, genelleme yapılmamalı ([Help Net Security](https://www.helpnetsecurity.com/2026/02/02/open-source-ai-pentesting-tools-test/)).

## Siber dışı: aynı motor, yeni profiller, en düşük riskle başla

Beril'in çekirdek yeteneği (stealth harvest, kanıt bağlantılı dosya, doğrulandı/çıkarım etiketi) siber dışında da değerli, çünkü AI araştırma ürünlerinin atıf sorunu ölçülmüş durumda: bir Nisan 2026 ön baskısı OpenAI/Google deep research modlarında atıf URL'lerinin %3-13'ünün uydurma olduğunu buldu ([arXiv](https://arxiv.org/abs/2604.03173)); Microsoft'un DeepTRACE denetimi atıf doğruluğunu %40-80 aralığında raporluyor ([Microsoft Research](https://www.microsoft.com/en-us/research/publication/deeptrace-auditing-deep-research-ai-systems-for-tracking-reliability-across-citations-and-evidence)). Konumlandırma: "tasarım gereği doğrulanabilir araştırma çıktısı".

| Alan | Uygunluk | Gerekçe ve risk |
|---|---|---|
| Açık kaynak proje sağlığı / due diligence | **Yüksek** | `deps`/`hunt` kodunu yeniden kullanır; OpenSSF Scorecard (18 kontrol) ücretsiz rakip, fark kanıt dosyası ([GitHub](https://github.com/ossf/scorecard)). Hukuki risk en düşük |
| Gazetecilik/OSINT kanıt dosyası | **Yüksek** | Arşiv ve hash adımı eklenmeli; Bellingcat Auto Archiver ile çakışıyor, yeniden yazma ([Bellingcat](https://bellingcat.gitbook.io/toolkit/categories/archiving.md)). Gelir düşük, itibar yüksek; kişisel veri riski var |
| Tedarikçi/KYB-lite | Orta | Bütçe en yüksek ama değer lisanslı veriye dayanır (Dow Jones, Sayari fiyat açıklamıyor); GDPR riski en yüksek |
| Rekabet istihbaratı | Orta | Crayon/Klue ücretsiz tahminlere göre yıllık ~$15-40k+ (tahmin, rakip satıcı kaynaklı); ToS ve anti-bot riski gerçek |
| Marka koruma | Orta | Asıl değer takedown iş akışı ve platform ilişkisi, Beril'de yok |
| Fiyat izleme, e-discovery, işe alım | Düşük | Commodity veya chain-of-custody ihtiyacı; kişisel veri/ToS riski (çıkarım, araştırılmadı) |

Bu uygunluk puanları çıkarımdır; pazar büyüklüğü verisi bulunamadı ve verilmedi. Efor tahminleri (profil için gün-hafta) kod okunmadan yapılmış tahminlerdir.

## Öncelik sırası: etki x efor

Aşağıdaki sıralama kanıtlı ölçüm değil, araştırma notlarındaki yargıların birleşimidir.

| Sıra | İş | Etki | Efor |
|---|---|---|---|
| 1 | Canlı OSV/KEV/EPSS çekme + önbellek (OSV API ücretsiz) | Yüksek | Düşük |
| 2 | SARIF doğrulama + CycloneDX tam + SPDX + OpenVEX | Orta-yüksek | Düşük |
| 3 | SHA-pinli GitHub Action, Dockerfile, pipx/PyPI, pre-commit | Yüksek | Düşük |
| 4 | Trivy/Grype/Semgrep/Nuclei/ZAP çıktısı içe alma, tek bulgu şeması | Yüksek | Orta |
| 5 | Halka açık benchmark (OWASP Benchmark/Juliet alt kümesi, bilinen sızıntı derlemleri) | Yüksek | Orta |
| 6 | Secret sağlayıcılarını 16'dan yüzlere çıkarma + baseline/allowlist (lisans: TruffleHog AGPL, gitleaks MIT) | Yüksek | Orta |
| 7 | MCP/skill/eklenti statik taramasını derinleştirme + davranış analizi | Yüksek | Orta |
| 8 | Profiller: `oss-dd`, `newsroom`, CRA raporu | Orta | Düşük-orta |
| 9 | Windows/macOS CI matrisi, sürüm sabitleme, çalışma manifesti | Orta | Düşük |
| 10 | Otomatik yama/PR, ticket dışa aktarımı, çok kullanıcılı dashboard | Orta | Yüksek |

İlk dört madde birlikte yaklaşık bir sürüm döngüsü tutar ve sonraki her şeyin güven zeminini kurar. Madde 4, SAST ve SCA derinliğini sıfırdan yazmadan telafi ettiği için Semgrep'in kural deposuna ayrı bir motor yazmaktan önceliklidir. Madde 10 yalnızca ekip pazarına gidilecekse yapılmalı.

## Dağıtım ve gelir: skills ve PyPI önce, gelir danışmanlık ve rapor

Skill ekosistemi çapraz ajan oldu: `npx skills add` ile yüklenen skills.sh (Vercel Labs, Şubat 2026) kurulum sayacı gösteriyor ve taşınabilirlik için frontmatter'ı `name` ve `description` ile sınırlı tutmak öneriliyor ([Vercel](https://vercel.com/blog/introducing-skills), [Termdock](https://termdock.com/en/blog/cross-agent-skills-new-npm)). Beril zaten Cursor/Windsurf/Copilot/Gemini/AGENTS.md dosyaları gönderiyor. Claude eklenti dizinine başvuru GitHub reposundan yapılıyor, `claude plugin validate` yerelde çalışıyor ve lisans, README, isim benzersizliği kontrol ediliyor ([Anthropic](https://claude.com/docs/plugins/submit.md)). Resmi marketplace'in form başvurusu alıp almadığı kaynaklarda çelişkili ([claude-plugins-official](https://github.com/anthropics/claude-plugins-official)). Homebrew core eşiği 75 yıldız (sahibi gönderirse 225): yeni repo geçemez, kendi tap'i kullanın ([Homebrew](https://docs.brew.sh/Acceptable-Formulae)). Kali "popülerlik ve benimsenme"yi tartıyor ([Kali](https://www.kali.org/docs/tools/submitting-tools/)). Black Hat Arsenal Asya çağrısı 2 Kasım 2026'ya kadardı, yani kapandı; Avrupa etkinliği 9-10 Aralık ([Black Hat](https://blackhat.com/arsenal-resources.html)). Sıra: kendi repo ve self-hosted marketplace, skills.sh, PyPI/pipx, kendi Homebrew tap'i, eklenti dizini formu, sonra Arsenal ve OWASP. Kurulum sayısı veya erişim verisi bu turda bulunamadı.

Para konusunda fonlu emsaller (Semgrep, ProjectDiscovery, Truffle) açık çekirdek + barındırılan bulut + takım başı fiyat modelini izliyor ([TechCrunch](https://techcrunch.com/2023/08/17/projectdiscovery-raises-25m-to-launch-a-cloud-version-of-its-threat-scanning-platform/)). Tek geliştirici bu yolu kopyalayamaz. Fiyat verileri kaynaklar arasında çelişkili ve düşük güvenli (Semgrep $20-40, Socket ~$25-50 katkıcı/ay vb.), sabit rakam olarak kullanılmamalı. Makul model (doğrulanmamış çıkarım): ücretsiz yerel CLI, ücretli tek seferlik/abonelik PDF rapor paketleri, CRA/NIS2 kanıt raporu, yönetilen tarama, eğitim ve danışmanlık. GitHub Sponsors 2026 Temmuz itibarıyla $100M'den fazla aktardı ama çoğu bakımcı geçinemiyor ([Help Net Security](https://www.helpnetsecurity.com/2026/07/21/open-source-github-sponsors-100-million/)). Solo gelir verisi bulunamadı. Bug bounty'yi gelir değil, kanıt olarak görün: HackerOne AI kullanımına izin veriyor ama doğrulanmamış otomatik çıktıyı reddediyor ([The Register](https://www.theregister.com/2026/02/18/hackerone_ai_policy/)), Bugcrowd doğrulanmamış otomatik gönderimlere 30 güne kadar askı veriyor ([Bugcrowd](https://www.bugcrowd.com/blog/bugcrowd-policy-changes-to-address-ai-slop-submissions/)), Intigriti AI kullanımının bildirilmesini istiyor ([Intigriti](https://www.intigriti.com/blog/business-insights/common-misconceptions-debugged)). Beril `hunt` çıktısı yalnızca elle yeniden üretilmiş, PoC'lu bulguyu göndermeli.

Küresel kitle için README İngilizce öncelikli olmalı, çevirileri topluluk yürütmeli ve dashboard metinleri anahtar tabanlı JSON'a taşınmalı. Bunlar kaynaksız öneridir. Türkiye tek bir topluluk çevirisi olarak ele alınmalı: yerel veriler (KVKK idari para cezaları, 7545 sayılı Siber Güvenlik Kanunu, KOBİ saldırı oranı) orta güvenli ve küresel kararı değiştirmiyor.

## Hukuki ve etik riskler: kapsam kapısı Beril'in kalkanı, harvest ise yeni cephe

En büyük risk her yerde izinsiz tarama. ABD DOJ CFAA politikası iyi niyetli güvenlik araştırmasını kovuşturmama yönünde ama eyalet yasalarını ve özel davaları bağlamıyor, EFF yetersiz buluyor ([MoFo](https://www.mofo.com/resources/insights/220525-cyber-crime-charging-policy), [EFF](https://www.eff.org/deeplinks/2022/05/dojs-new-cfaa-policy-good-start-does-not-go-far-enough-protect-security)). Beril'in sahiplik kaydı ve kapsam dosyası bu nedenle ürünün parçası olarak yayımlanmalı: güvenli liman tarzı politika, sürüm notlarında "test edilmedi" listesi. Birleşik Krallık Computer Misuse Act için araştırma savunması konusunda sonuç bulunamadı.

Harvest tarafı ayrı bir risk: ABD'de oturumsuz, herkese açık sayfa taraması lehine emsaller var (hiQ v. LinkedIn, Meta v. Bright Data) ama bunlar bot tespitini aşmayı kapsamıyor ve Bright Data kararının kapsamı tartışmalı ([Jenner](https://www.jenner.com/en/news-insights/publications/client-alert-data-scraping-in-hiq-v-linkedin-the-ninth-circuit-reaffirms-narrow-interpretation-of-cfaa), [FBM](https://www.fbm.com/technology/publications/major-decision-affects-law-of-scraping-and-online-data-collection-meta-platforms-v-bright-data/)). AB'de EDPB'nin web kazıma kılavuzu üretken AI eğitimi içindir, kişisel veri işlendiğinde GDPR devreye girer, robots.txt ve giriş duvarları makul beklenti değerlendirmesine girer; belgenin nihai olup olmadığı kaynaklarda çelişkili, dosya üretimine kıyasla uygulanıyor ([Sidley](https://datamatters.sidley.com/2026/07/23/what-do-the-european-data-protection-boards-web-scraping-guidelines-mean-for-ai-training-datasets/)). Pratik sonuç: mevcut kapsam kapısı genişletilip "kaynak politikası kapısı" olmalı (robots, ToS, giriş durumu, kişisel veri bayrağı) ve Camoufox'un anti-bot aşma özelliği ticari kullanımda varsayılan kapalı, açıkça opt-in olmalı. Kişisel veri ağırlıklı alanlar (KYB, işe alım, gazetecilik) için dosya başına meşru menfaat notu ve veri minimizasyonu gerekir. Kali gibi dağıtım kanalları dual-use araçlara temkinli, bu da bir itibar riski ([Kali](https://www.kali.org/docs/policy/penetration-testing-tools-policy/)). CRA kapsamı (ticari olmayan açık kaynağın dışarıda kalması, steward rejimi) hukuk görüşü gerektiriyor ([Patchstack](https://patchstack.com/articles/launching-managed-cra-article-14-reporting-for-open-source-maintainers/)).

## Araştırılmayanlar ve düşük güvenli noktalar

Bu rapor arama özetlerine dayanıyor, doğrudan vendor sayfaları çoğunlukla okunmadı. Fiyatlar (Snyk, Semgrep, Socket, Aikido, Maltego, Crayon vb.) kaynaklar arasında çelişiyor, kullanmayın. Araştırılmayan veya sonuçsuz kalanlar: ISO 27001/SOC2/KVKK eşleme araçları, MobSF ve LLM red-team (garak/promptfoo) rakipleri, MISP/OpenCTI, OWASP Benchmark sonuçları, Semgrep/CodeQL/Trivy/ZAP güncel sayıları, ENISA/CISA birincil sayfaları, NIS2 KOBİ kapsamı, GDPR ayrıntıları, 2024 sonrası ABD kazıma kararları, kurulum/erişim verileri ve solo gelir rakamları. Beril'in kendi performansı büyük depolarda ölçülmedi, `./beril validate` çalıştırması zaman aşımına uğradı ve sonucu okunmadı. Efor tahminleri yargıdır. "Minecraft'ta rakip yok" iddiası arama sınırlılığı nedeniyle düşük güvenli. Yerel inceleme anında çok sayıda dosya commit edilmemişti; sayılar o anki çalışma ağacını yansıtıyor.

## Sonuç

Araştırmanın değiştirdiği ana fikir: Beril'in rakipleri "daha çok kural" yarışında tutulamaz, ama 2026'nın üç krizi (tedarik zinciri solucanları, AI slop ve AI atıf uydurması) hep aynı eksikliği gösteriyor: **doğrulanmamış çıktı**. Beril'in doğrulandı/çıkarım etiketi, ağsız sandbox ve kapsam kapısı bu eksiğe cevap verdiği ölçüde değerli, ve bu değer ölçülmüş doğruluk olmadan iddiadan öteye geçmez. Bu yüzden benchmark ve canlı veri, her yeni alandan önce gelir.

Siber dışına açılma kararı ikinci sırada: önce açık kaynak sağlığı ve gazetecilik profili ile iki hafta içinde test edilebilir, düşük riskli iki deneme yapılmalı. KYB, rekabet istihbaratı ve marka koruma, lisanslı veri ve hukuki risk nedeniyle ancak ilk iki profil kullanıcı çektikten sonra düşünülmeli.

## Ek: Sızıntı vakalarından eğitim hattı

Fikir: geçmişte sızıntı yaşamış olaylar (WikiLeaks dahil kamusal sızıntılar) için çözümü bulup eğitime çevirmek. Akış: olay, kök neden, tespit yolu, düzeltme, lab. Mevcut `train` ve `labs` modlarına ve kanıt bağlantılı dossier yapısına uyar. Vakalar aynı zamanda yeni tarama kuralı üretir; bu, kural verisinin küçük olması sorununa kısmen cevap verir.

Kaynak politikası: ham sızıntı verisi, kişisel veri ve çalınmış kimlik bilgileri indirilmez veya saklanmaz. Sızdırılmış kaynak kod veya araçlar çalıştırılmaz. Yalnızca yayımlanmış analizler (CISA, DFIR Report, Mandiant, VERIS/VCDB, araştırmacı yazıları) kaynak gösterilerek işlenir. Her kayıtta "doğrulandı" veya "çıkarım" etiketi bulunur. Belge gerçekliği tartışmalıysa not düşülür. Bu bölüm hukuki görüş değildir; araştırılmadı, yalnızca tasarım önerisidir.
