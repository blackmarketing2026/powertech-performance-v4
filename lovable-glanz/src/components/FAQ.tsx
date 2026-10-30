import {
  Accordion,
  AccordionContent,
  AccordionItem,
  AccordionTrigger,
} from "@/components/ui/accordion";

const FAQ = () => {
  const faqs = [
    {
      question: "Wie viel kostet eine Keramikversiegelung?",
      answer: "Die Kosten hängen von Fahrzeuggröße, Lackzustand und Vorbereitung ab. Ein Angebot erstellen wir nach der Besichtigung und Abstimmung des Leistungsumfangs."
    },
    {
      question: "Wie lange hält eine Keramikversiegelung?",
      answer: "Eine Keramikversiegelung kann bei richtiger Pflege mehrere Jahre halten. Die tatsächliche Haltbarkeit hängt von Produkt, Nutzung, Witterung und Waschgewohnheiten ab. Die Bedingungen für Ihr Fahrzeug stehen im Angebot."
    },
    {
      question: "Warum ist eine Keramikversiegelung so teuer?",
      answer: "Der Preis spiegelt den hohen Aufwand wider: Vor der Versiegelung muss der Lack perfekt vorbereitet, poliert und gereinigt werden. Die Materialien sind hochwertig, und die Auftragung erfordert Fachwissen und Präzision. Das Ergebnis ist ein mehrjähriger Schutz, der den Wiederverkaufswert steigert und Pflegeaufwand reduziert."
    },
    {
      question: "Was sind die Nachteile von Keramik?",
      answer: "Keramikversiegelungen bieten enorme Vorteile, haben aber auch gewisse Grenzen: Sie schützen nicht vor Steinschlägen oder tiefen Kratzern. Zudem erfordert die Auftragung Fachwissen – fehlerhafte Anwendung kann Flecken hinterlassen. Bei PowerTech Performance sorgen wir für eine professionelle Auftragung ohne diese Nachteile."
    },
    {
      question: "Wie wäscht man ein Auto mit Keramikversiegelung?",
      answer: "Fahrzeuge mit Keramikversiegelung sollten schonend gewaschen werden: Verwenden Sie pH-neutrale Shampoos, weiche Mikrofasertücher oder Waschhandschuhe und vermeiden Sie aggressive Bürsten. Eine Handwäsche ist ideal – Hochdruckreiniger können genutzt werden, jedoch mit ausreichend Abstand."
    },
    {
      question: "Kann man mit Keramikversiegelung in die Waschanlage?",
      answer: "Ja, Sie können mit einer Keramikversiegelung in die Waschanlage fahren. Allerdings empfehlen wir berührungslose Waschanlagen oder Handwäsche, da rotierende Bürsten und aggressive Chemikalien die Versiegelung auf Dauer beeinträchtigen können. Schonende Reinigung verlängert die Haltbarkeit."
    },
    {
      question: "Welches Autoshampoo nach Keramikversiegelung?",
      answer: "Nach einer Keramikversiegelung sollten Sie ein pH-neutrales, wachsfreies Shampoo verwenden. Produkte mit Wachs oder Versiegelungen können die Keramikschicht überlagern und ihre Wirkung beeinträchtigen. Wir empfehlen spezielle Keramik-Shampoos, die die hydrophoben Eigenschaften unterstützen."
    },
    {
      question: "Welcher Reiniger bei Keramikversiegelung?",
      answer: "Für versiegelte Fahrzeuge eignen sich pH-neutrale Reiniger ohne aggressive Chemikalien. Vermeiden Sie lösungsmittelhaltige oder stark alkalische Produkte. Spezielle Keramik-Reiniger entfernen Schmutz schonend, ohne die Schutzschicht anzugreifen. Wir beraten Sie gerne zu geeigneten Produkten."
    },
    {
      question: "Womit sollte ich mein Auto vor der Keramikversiegelung waschen?",
      answer: "Vor der Versiegelung muss der Lack tiefenrein sein: Eine gründliche Vorwäsche mit Hochdruckreiniger, gefolgt von einer Handwäsche mit pH-neutralem Shampoo, ist ideal. Anschließend erfolgt eine Lackpolitur zur Entfernung von Verunreinigungen. Bei PowerTech Performance übernehmen wir die komplette Vorbereitung für Sie."
    },
    {
      question: "Wie pflege ich meine Keramikversiegelung?",
      answer: "Regelmäßige schonende Wäsche mit pH-neutralem Shampoo, sanftes Abtrocknen mit Mikrofasertüchern und gelegentliche Nachbehandlung mit Keramik-Boostern halten die Versiegelung in Topzustand. Vermeiden Sie aggressive Chemikalien und mechanische Belastungen. Wir beraten Sie gerne zur optimalen Pflege."
    },
    {
      question: "Wie sinnvoll ist eine Keramikversiegelung?",
      answer: "Eine Keramikversiegelung ist hochgradig sinnvoll für alle, die langfristigen Lackschutz und Werterhalt wünschen. Sie reduziert Pflegeaufwand, schützt vor Umwelteinflüssen und bewahrt den Glanz über Jahre. Besonders bei Neuwagen oder nach Aufbereitung lohnt sich die Investition – Sie sparen langfristig Zeit und Geld."
    },
  ];

  return (
    <section className="py-16 md:py-24 bg-background">
      <div className="container px-4">
        <div className="max-w-4xl mx-auto">
          <div className="text-center mb-12">
            <h2 className="text-3xl md:text-5xl font-bold mb-4">
              Häufig gestellte Fragen
            </h2>
            <p className="text-xl text-muted-foreground">
              Alles, was Sie über Keramikversiegelung wissen müssen
            </p>
          </div>

          <Accordion type="single" collapsible className="space-y-4">
            {faqs.map((faq, index) => (
              <AccordionItem
                key={index}
                value={`item-${index}`}
                className="bg-card border border-border rounded-lg px-6 shadow-sm"
              >
                <AccordionTrigger className="text-left text-lg font-semibold hover:text-primary py-6">
                  {faq.question}
                </AccordionTrigger>
                <AccordionContent className="text-muted-foreground leading-relaxed pb-6">
                  {faq.answer}
                </AccordionContent>
              </AccordionItem>
            ))}
          </Accordion>
        </div>
      </div>
    </section>
  );
};

export default FAQ;
