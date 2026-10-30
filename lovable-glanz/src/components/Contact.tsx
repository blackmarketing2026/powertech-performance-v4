import { FormEvent, useState } from "react";
import { MapPin, Phone, Mail, MessageCircle } from "lucide-react";
import { Button } from "@/components/ui/button";

const Contact = () => {
  const offerActive = new URLSearchParams(window.location.search).get("aktion") === "keramik20";
  const [status, setStatus] = useState("");
  const [sending, setSending] = useState(false);

  const handleSubmit = async (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    if (sending) return;
    const form = event.currentTarget;
    if (!form.reportValidity()) return;
    const payload = Object.fromEntries(new FormData(form).entries());
    setSending(true);
    setStatus("Wird gesendet …");
    try {
      const response = await fetch("/api/send-lead", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ ...payload, formName: "Keramikversiegelung Glanz Erfurt" }),
      });
      const result = await response.json().catch(() => ({}));
      if (!response.ok) throw new Error(result.error || "Versand fehlgeschlagen.");
      const tracker = (window as Window & { trackFormSuccess?: (form: HTMLFormElement) => void }).trackFormSuccess;
      if (typeof tracker === "function") tracker(form);
      form.reset();
      setStatus("Danke! Ihre Anfrage wurde gesendet. Wir melden uns zeitnah.");
    } catch (error) {
      setStatus(error instanceof Error ? error.message : "Versand fehlgeschlagen. Bitte versuchen Sie es erneut.");
    } finally {
      setSending(false);
    }
  };

  return (
    <section id="contact" className="py-16 md:py-24 bg-gradient-subtle">
      <div className="container px-4"><div className="max-w-6xl mx-auto">
        <div className="text-center mb-16"><h2 className="text-3xl md:text-5xl font-bold mb-4">Jetzt kostenlos anfragen</h2><p className="text-xl text-muted-foreground">Kontaktieren Sie uns für ein unverbindliches Angebot</p></div>
        <div className="grid md:grid-cols-2 gap-8 lg:gap-12 items-start">
          <div className="space-y-8">
            <div><h3 className="text-2xl font-bold mb-6">PowerTech Performance</h3><p className="text-muted-foreground mb-6">Inhaber: Benjamin Lemmer</p></div>
            <div className="space-y-6">
              <div className="flex items-start gap-4"><div className="w-12 h-12 bg-primary/10 rounded-lg flex items-center justify-center flex-shrink-0"><MapPin className="w-6 h-6 text-primary" /></div><div><h4 className="font-semibold mb-1">Adresse</h4><p className="text-muted-foreground">An der Klinge 10<br />99095 Erfurt</p></div></div>
              <div className="flex items-start gap-4"><div className="w-12 h-12 bg-primary/10 rounded-lg flex items-center justify-center flex-shrink-0"><Phone className="w-6 h-6 text-primary" /></div><div><h4 className="font-semibold mb-1">Telefon</h4><a href="tel:+491737373574" className="text-muted-foreground hover:text-primary transition-colors">+49 173 7373574</a></div></div>
              <div className="flex items-start gap-4"><div className="w-12 h-12 bg-primary/10 rounded-lg flex items-center justify-center flex-shrink-0"><Mail className="w-6 h-6 text-primary" /></div><div><h4 className="font-semibold mb-1">E-Mail</h4><a href="mailto:info@powertech-performance.de" className="text-muted-foreground hover:text-primary transition-colors">info@powertech-performance.de</a></div></div>
            </div>
            <div className="space-y-3"><Button asChild className="w-full" size="lg"><a href="/online-termin-buchen/">Besichtigungstermin buchen</a></Button><Button asChild className="w-full bg-[#25D366] hover:bg-[#20BA5A] text-white" size="lg"><a href="https://wa.me/491737373574" target="_blank" rel="noopener noreferrer"><MessageCircle className="w-5 h-5 mr-2" />WhatsApp: +49 173 7373574</a></Button></div>
          </div>
          <form className="bg-card rounded-xl shadow-lg border border-border overflow-hidden p-6 space-y-4" onSubmit={handleSubmit} data-form-name="Keramikversiegelung Glanz Erfurt">
            {offerActive && <><p className="rounded-lg bg-primary/10 p-3 text-sm font-semibold text-primary">20-%-Aktion für Keramikversiegelung ausgewählt. Wir berücksichtigen sie bei Ihrer Anfrage.</p><input type="hidden" name="aktion" value="20 % Rabatt auf Keramikversiegelung" /></>}
            <div className="hidden" aria-hidden="true"><label htmlFor="glanz-website">Website</label><input id="glanz-website" name="website" tabIndex={-1} autoComplete="off" /></div>
            <div><label className="block font-semibold mb-2" htmlFor="glanz-name">Name *</label><input className="w-full rounded-lg border border-input bg-background p-3" id="glanz-name" name="name" autoComplete="name" required /></div>
            <div><label className="block font-semibold mb-2" htmlFor="glanz-email">E-Mail *</label><input className="w-full rounded-lg border border-input bg-background p-3" id="glanz-email" name="email" type="email" autoComplete="email" required /></div>
            <div><label className="block font-semibold mb-2" htmlFor="glanz-phone">Telefon</label><input className="w-full rounded-lg border border-input bg-background p-3" id="glanz-phone" name="phone" type="tel" autoComplete="tel" /></div>
            <div><label className="block font-semibold mb-2" htmlFor="glanz-vehicle">Fahrzeug</label><input className="w-full rounded-lg border border-input bg-background p-3" id="glanz-vehicle" name="vehicle" /></div>
            <div><label className="block font-semibold mb-2" htmlFor="glanz-message">Nachricht *</label><textarea className="w-full rounded-lg border border-input bg-background p-3 min-h-32" id="glanz-message" name="message" required placeholder="Beschreiben Sie Ihr Fahrzeug und Ihren Wunsch" /></div>
            <Button className="w-full" size="lg" type="submit" disabled={sending}>{sending ? "Wird gesendet …" : "Anfrage senden"}</Button>
            <p className="text-xs text-muted-foreground">* Pflichtfeld · Ihre Angaben verwenden wir zur Bearbeitung Ihrer Anfrage. <a className="underline" href="/pages/datenschutz.html">Datenschutz</a></p>
            <p role="status" aria-live="polite" className="text-sm text-muted-foreground">{status}</p>
          </form>
        </div>
      </div></div>
    </section>
  );
};

export default Contact;
