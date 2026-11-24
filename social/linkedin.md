# LinkedIn gönderisi

Video: video/beril-tr-linkedin-4x5.mp4 / video/beril-en-linkedin-4x5.mp4 (1080x1350)
Kapak: video/cover-tr-4x5.png / video/cover-en-4x5.png

## Türkçe

Gece 03:12. Biri sitenin kapılarını yokluyor. Peki ya o kapıları ilk sen yoklasan?

Bu soruyla Beril'i geliştirdim. Beril, kendi bilgisayarında çalışan, açık kaynak bir siber güvenlik asistanı. Bir site, uygulama ya da kod deposu veriyorsun. Önce okuyup anlıyor, sonra senin izninle küçük ve kontrollü adımlarla kırmayı deniyor. Bulduğu her açık için kanıtı, ne kadar emin olduğunu ve nasıl düzelteceğini yazıyor.

Neler yapabiliyor:
• Pasif web taraması: güvenlik başlıkları, çerezler, TLS, SPF/DKIM/DMARC, açık yollar ve portlar
• Sahiplik doğrulamasından sonra aktif deneme (DNS TXT, .well-known ya da meta etiketiyle)
• APK, IPA, EXE, ELF ve JAR dosyalarını çalıştırmadan inceleme
• Git geçmişinde gizli anahtar taraması, bağımlılıkları KEV ve EPSS ile önceliklendirme, SBOM üretimi
• MCP ayarlarını ve yapay zekâyla yazılmış uygulamaları kontrol etme
• Açık kaynak projelerde ağsız bir sandbox içinde hata avı

Bilerek yapmadıklarını da önemsedim. İzin kaydı yoksa aktif deneme yapmıyor, zararlı exploit üretmiyor, veri dışarı çıkmıyor. Neyi test etmediğini de raporda açıkça yazıyor.

37 komut, 189 test, 10 pratik lab ve 25 haftalık bir eğitim planı var. Raporlar mühendis, bug bounty, KOBİ, bakımcı ve CRA için ayrı çıkıyor. JSON ve SARIF çıktısı da var.

Kod açık, MIT lisanslı: github.com/sheduxdev/beril

Geri bildirimlerinizi çok isterim. İşinize yararsa bir yıldız bırakabilirsiniz ♡

#siberguvenlik #acikkaynak #appsec #pentest #yazilim

## English

3:12 AM. Someone is trying the doors of your site. What if you tried them first?

That question is why I built Beril, an open source cybersecurity assistant that runs on your own machine. You give it a site, an app or a repo. It reads and understands it first, then tries to break it in small, controlled steps, with your permission. For every weakness it finds, it writes the evidence, how confident it is and how to fix it.

What it does:
• Passive web scan: security headers, cookies, TLS, SPF/DKIM/DMARC, exposed paths and ports
• Active checks only after ownership is verified (DNS TXT, .well-known or a meta tag)
• Static review of APK, IPA, EXE, ELF and JAR files, never executed
• Secret scanning across git history, dependency ranking with KEV and EPSS, SBOM generation
• Checks for MCP configs and AI-written apps
• Bug hunting in open source projects inside a networkless sandbox

What it deliberately does not do mattered just as much. No permission record, no active attempt. No weaponized exploits. No data leaves your machine. Every report also states what was not tested.

37 commands, 189 tests, 10 practice labs and a 25 week training plan. Reports for engineers, bug bounty hunters, small businesses, maintainers and CRA, plus JSON and SARIF.

The code is open and MIT licensed: github.com/sheduxdev/beril

I would love your feedback. If it helps you, a star means a lot ♡

#cybersecurity #opensource #appsec #pentest #infosec
