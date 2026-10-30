import { Award, CheckCircle2 } from "lucide-react";

const Guarantee = () => {
  return (
    <section className="py-16 md:py-24 bg-card">
      <div className="container px-4">
        <div className="max-w-5xl mx-auto">
          <div className="flex flex-col items-center text-center mb-12">
            <div className="w-20 h-20 bg-gradient-primary rounded-full flex items-center justify-center mb-6 shadow-glow">
              <Award className="w-10 h-10 text-primary-foreground" />
            </div>
            <h2 className="text-3xl md:text-5xl font-bold mb-4">
              Qualität & Vertrauen
            </h2>
            <div className="text-4xl md:text-6xl font-bold text-primary mb-6">
              Pflege mit Anspruch
            </div>
          </div>

          <div className="bg-background/50 backdrop-blur-sm rounded-2xl p-8 md:p-12 border-2 border-primary/20">
            <div className="space-y-6 text-lg leading-relaxed">
              <p className="text-muted-foreground">
                Bei <strong className="text-foreground">PowerTech Performance</strong> setzen wir auf höchste Qualität und präzise Handarbeit.
                Jede Keramikversiegelung wird von unserem erfahrenen Team fachgerecht aufgetragen – mit der Sorgfalt,
                die Ihr Fahrzeug verdient.
              </p>

              <div className="grid md:grid-cols-2 gap-6 my-8">
                <div className="flex items-start gap-3">
                  <CheckCircle2 className="w-6 h-6 text-primary flex-shrink-0 mt-1" />
                  <p className="text-muted-foreground">
                    <strong className="text-foreground">Präzise Vorbereitung:</strong> Lackpolitur und Reinigung nach höchsten Standards
                  </p>
                </div>
                <div className="flex items-start gap-3">
                  <CheckCircle2 className="w-6 h-6 text-primary flex-shrink-0 mt-1" />
                  <p className="text-muted-foreground">
                    <strong className="text-foreground">Professionelle Auftragung:</strong> Schichtweise für maximale Haltbarkeit
                  </p>
                </div>
                <div className="flex items-start gap-3">
                  <CheckCircle2 className="w-6 h-6 text-primary flex-shrink-0 mt-1" />
                  <p className="text-muted-foreground">
                    <strong className="text-foreground">Premium-Materialien:</strong> Nur geprüfte Keramikbeschichtungen
                  </p>
                </div>
                <div className="flex items-start gap-3">
                  <CheckCircle2 className="w-6 h-6 text-primary flex-shrink-0 mt-1" />
                  <p className="text-muted-foreground">
                    <strong className="text-foreground">Langzeitschutz:</strong> Passend zu Nutzung und Pflege
                  </p>
                </div>
              </div>

              <p className="text-muted-foreground">
                Unser Anspruch: Ihr Fahrzeug verlässt unsere Werkstatt erst, wenn der Lack perfekt geschützt ist
                und gepflegt glänzt. Die Details zu Leistung und Haltbarkeit besprechen wir vorab mit Ihnen.
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Guarantee;
